# VGG19 pre train load
# VGG19 conv layer 분리
# deep image repre

import torch
import torch.nn as nn
from torchvision.models import vgg19

conv = {
    'conv1_1' : 0, # style
    'conv2_1' : 5, # style
    'conv3_1' : 10, # style
    'conv4_1' : 19, # style
    'conv5_1' : 28, # style
    'conv4_2' : 21, # content
}

# forward 부분
class StyleTransfer(nn.Module):
    def __init__(self,):
        super().__init__()
        #TODO: VGG19 load
        self.vgg19_model = vgg19(pretrained=True)
        self.vgg19_features = self.vgg19_model.features

        #TODO: conv layer 분리
        self.style_layer = [conv['conv1_1'], conv['conv2_1'], conv['conv3_1'], conv['conv4_1'], conv['conv5_1']]
        self.content_layer = [conv['conv4_2']]
        pass

    def forward(self, x, mode:str):
        #TODO: style, content 마다 conv layer slicing 해서 사용하기
        features = []
        if mode=='style':
            for i in range(len(self.vgg19_features)):
                x = self.vgg19_features[i](x)
                if i in self.style_layer:
                    features.append(x)
        elif mode=='content':
            for i in range(len(self.vgg19_features)):
                x = self.vgg19_features[i](x)
                if i in self.content_layer:
                    features.append(x)

        return features




    






































