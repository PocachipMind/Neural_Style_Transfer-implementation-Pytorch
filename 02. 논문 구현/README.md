# 논문 구현

논문을 코드로 구현합니다.

구현하며 학습한 진행 사항을 기록합니다.

기본적으로 논문 구현은 4파트로 진행합니다.

### 1. Modeling 

torch.nn.modeule로 구현될 실제 forward 부분
### 2. Dataset
  
현 논문은 특별히 데이터셋이 필요 없긴 하지만, 보통 데이터셋이 있고 그리고 각각의 데이터 셋을 preprocessing , postprocessing , load, save... 등등 이런 작업들이 엔지니어링적인 작업들이 필요. 
### 3. Loss

해당 파트는 개인취향이긴 하지만 Loss Function이 복잡한 경우가 있습니다. 그런 경우 따로 빼서 구현하는게 좀 더 깔끔하다. 
### 4. Train

1~3 구현 파트를 합친 다음에 Main Train loop 를 설정하고 매 스탭마다 모델을 업데이트하고 결과 저장하고 이런 것들을 할 부분입니다.


### 현 논문은 dataset이 필요없으니 3 part로 나누어서 구현합니다.

# 1. Modeling

![image](https://github.com/user-attachments/assets/edb433d2-c1f1-41b8-9e32-3d39e48de008)

VGG19에서 슬라이싱을 통해 각각 합성곱 레이어를 갖고오는 작업을 합니다.

![image](https://github.com/user-attachments/assets/08bf879e-906a-4987-b334-d85e5b9deb27)

![image](https://github.com/user-attachments/assets/ba7259a5-d1d2-4314-b0c8-6c9109f3309a)


# 2. Loss

ContentLoss와 StyleLoss를 나눠 구현

# 3. Train 

코드가 어떻게 구현되어가는지 파악하자.

### train 01~02 로 기본적인 구조 구현 완.

01 : 코드 구조 구현

02 : 데이터 device로 옮겨 효과적인 학습 진행

### train 03 부터
train 03 부터 하이퍼 파라미터 튜닝을 위한 구조 변경

03 : 폴더를 생성하고 파라미터값을 바꾸며 실험

04 : 이니셜라이징을 컨텐트 이미지에서 시작하도록 시도. 매우 성공적

### train final

논문에 구현되어있는 optimizer 적용 -> closure 필요

### train final 최종 코드

# 하이퍼파라미터 테스트

### content input : 

![l_2019010201000247800015641](https://github.com/user-attachments/assets/08c4821e-8a3c-4ce3-b153-c525c0b1d9ff)

### style input :

![style](https://github.com/user-attachments/assets/4e926526-b97e-4f71-ae5c-2b6cda233b32)

## 1. alpha = 1, beta = 1e8 , lr = 1
epoch 1 :

![0](https://github.com/user-attachments/assets/a17a2ea0-5a50-46c0-92d1-7cc27dfe0b27)

epoch 200:

![200](https://github.com/user-attachments/assets/e7f13efd-f115-479e-a5b5-1bd5021943fa)


## 2. alpha = 1, beta = 1e5 , lr = 1

epoch 1 : 

![0](https://github.com/user-attachments/assets/dad50f7f-c9ae-4ca4-a716-6451d4ccd6df)

epoch 200:

![200](https://github.com/user-attachments/assets/2a59d6e8-ba12-4fba-bc73-e2077777fb30)
