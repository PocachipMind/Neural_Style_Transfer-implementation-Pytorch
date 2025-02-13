# content loss
# vgg19 feature map -> deep image representation
# MSE

# style loss
# gram matrix -> function
# MSE

import torch
import torch.nn as nn
import torch.nn.functional as F

class ContentLoss(nn.Module):
    def __init__(self,):
        super(ContentLoss, self).__init__()

    def forward(self, x:torch.Tensor, y:torch.Tensor):
        # x torch.Tensor shape (b,c,h,w)
        # MSE loss
        loss = F.mse_loss(x,y)
        return loss

class StyleLoss(nn.Module):
    def __init__(self,):
        super(StyleLoss, self).__init__()

    def gram_matrix(self, x:torch.Tensor):
        """
        x: torch.Tensor, shape (b,c,h,w)
        reshape (b,c,h,w) -> (b,c,h*w)
        dim (b, N, M)
        transpoe
        matrix mul
        """
        
        b, c, h, w = x.size()
        # reshape
        features = x.view(b, c, h*w) # (b, N, M)로 변경
        features_T = features.transpose(1, 2) # 바꿀 이레이 디멘션 인덱스 입력 # (b, M, N)
        G = torch.matmul(features, features_T) # (b, N, N)

        return G.div(b*c*h*w) # 스켈링 팩터 나누기


    def forward(self, x, y):
        # gram matrix style representaion
        # MSE
        Gx = self.gram_matrix(x)
        Gy = self.gram_matrix(y)
        loss = F.mse_loss(Gx, Gy) # 이미 gram_matrix 에서 노멀라이징 했음
        return loss