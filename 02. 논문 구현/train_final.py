'''
구현 로드맵

# import 

# Load data
## pre processing
## prost processing 

# Load model

# Load Loss

# setting optimizer

# train Loop
## Loss print
## image gen output save

'''

# import
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import torchvision.transforms as T
import os

import numpy as np
from PIL import Image

from models import StyleTransfer
from loss import ContentLoss, StyleLoss
from tqdm import tqdm

# 어떤 프리트레인된 모델을 사용할 경우 그 모델을 사용할 때 그 모델이 학습할 때 사용했었던 모든 프리프로세싱을 똑같이 따라해야합니다.
# 그래야 아웃풋이 정확히 나옵니다.
mean = [0.485, 0.456, 0.406]
std = [0.229, 0.224, 0.225]

def pre_processing(image:Image.Image) -> torch.Tensor:
    
    # 이미지 resize (512,512)
    # Image -> Tensor
    # Normalize : VGG pretrained 된 모델이 학습할 때 사용한 preprocessing
    preprocessing = T.Compose([
        T.Resize((512,512)),
        T.ToTensor(),
        T.Normalize(mean, std) # lambda x : (x-mean) / std
    ]) # (c, h ,w)

    # (1, c, h ,w) 원래 데이터 로더를 구현하면 이게 자동으로 되지만, 
    # 현 논문에서 데이터 로더를 사용하지 않음. 고로 1 batch 붙이기
    image_tensor:torch.Tensor = preprocessing(image)

    return image_tensor.unsqueeze(0)

def post_processing(tensor:torch.Tensor) -> Image.Image:

    # shape (b)1,c,h,w
    image:np.ndarray = tensor.to('cpu').detach().numpy() # cpu로 보내고 그래디언트 계산 제거, 넘파이로 변환
    # shape c,h,w
    image = image.squeeze()
    # shape h,w,c
    image = image.transpose(1, 2, 0)
    # de norm
    image = image*std + mean
    # clip
    image = image.clip(0,1)*255
    # dtype uint8
    image = image.astype(np.uint8)
    # numpy -> Image
    return Image.fromarray(image)


def train_main():
    # load data
    content_image = Image.open('./content.jpg')
    content_image = pre_processing(content_image)

    style_image = Image.open('./style.jpg')
    # style_image = Image.open('./style2.jpg')
    style_image = pre_processing(style_image)

    # load model
    style_transfer = StyleTransfer().eval()

    # load loss
    content_loss = ContentLoss()
    style_loss = StyleLoss()

    # hyper parameter
    alpha = 1
    beta = 1e6
    lr = 1

    save_root = f'{alpha}_{beta}_{lr}_initContent_style2_LBFGS'
    os.makedirs(save_root, exist_ok=True)

    # device setting
    device = 'cpu'
    if torch.cuda.is_available():
        device = 'cuda'


    style_transfer = style_transfer.to(device)
    content_image = content_image.to(device)
    style_image = style_image.to(device)
    
    # noise
    # x = torch.randn(1,3,512,512).to(device)
    x = content_image.clone()
    x.requires_grad_(True)


    # setting optimizer
    optimizer = optim.LBFGS([x], lr=lr)

    # closure -> LBFGS optim을 쓰려면 필요함.
    def closure():
        # gradient 계산
        # return loss 하나
        optimizer.zero_grad()
        x_content_list = style_transfer(x, 'content')
        y_content_list = style_transfer(content_image, 'content')

        x_style_list = style_transfer(x, 'style')
        y_style_list = style_transfer(style_image, 'style')

        ## loss_content, loss_style
        loss_c = 0
        loss_s = 0
        loss_total = 0

        for x_content, y_content in zip(x_content_list, y_content_list):
            loss_c += content_loss(x_content, y_content)
        loss_c = alpha*loss_c

        for x_style, y_style in zip(x_style_list, y_style_list):
            loss_s += style_loss(x_style, y_style)
        loss_s = beta*loss_s

        loss_total = loss_c + loss_s
        loss_total.backward()
        return loss_total



    # train loop
    steps = 1000
    for step in tqdm(range(steps)):
        ## content representation (x, content_image)
        ## style representation (x, style_image)

        ## optimizer step
        optimizer.step(closure)

        ## loss print
        if step%100==0:
            with torch.no_grad():
                x_content_list = style_transfer(x, 'content')
                y_content_list = style_transfer(content_image, 'content')

                x_style_list = style_transfer(x, 'style')
                y_style_list = style_transfer(style_image, 'style')

                ## loss_content, loss_style
                loss_c = 0
                loss_s = 0
                loss_total = 0

                for x_content, y_content in zip(x_content_list, y_content_list):
                    loss_c += content_loss(x_content, y_content)
                loss_c = alpha*loss_c

                for x_style, y_style in zip(x_style_list, y_style_list):
                    loss_s += style_loss(x_style, y_style)
                loss_s = beta*loss_s

                loss_total = loss_c + loss_s

                print(f"loss_c: {loss_c.cpu()}")
                print(f"loss_s: {loss_s.cpu()}")
                print(f"loss_total: {loss_total.cpu()}")

                ## post processing
                ## image gen output save
                gen_img:Image.Image = post_processing(x)
                gen_img.save(os.path.join(save_root, f'{step}.jpg'))

if __name__=="__main__":
    train_main()