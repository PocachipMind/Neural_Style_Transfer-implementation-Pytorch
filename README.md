# Neural Style Transfer-implementation-Pytorch
A Neural Algorithm of Artistic Style ( a.k.a Neural Style Transfer ) [ CVPR2016 ] 논문을 Pytorch 로 구현합니다.

# 선정 이유
- 데이터셋을 특별히 준비 해 둘 필요가 없다
- 아키텍쳐링이 쉽고 논문 구현 난이도가 높지 않다
- Generative Model로 결과가 시각적으로 볼 수 있다.

# 학습 내용
LBFGS optim 사용 방법 (closure 구현) 학습

Transfer 논문 모델 원리 이해

# 의문점 ( 고찰 )

내적을 통해 유사도를 파악할 수 있음. 즉 Style 손실을 계산하기 위해 내적을 하는 것은 알수 있음.

그러면 왜 style image , gen image 의 손실을 구할때 Gram Matrix를 활용하는가? 

즉 style image 와 gen image 끼리 내적하고 손실을 구하는게 아니라 (stlye image 내적 stlye image) 와 (gen image 내적 gen image) 끼리 비교하는 것인가?

다시말해, 스타일 변환(Style Transfer)에서 스타일 손실(Style Loss)을 계산할 때 스타일 이미지와 생성된 이미지의 특징 맵을 직접 내적해서 비교하지 않고, 각각의 Gram Matrix를 만들어 비교하는 이유는 무엇인가?

## 1. Gram Matrix가 캡처하는 정보

Gram Matrix **𝐺**는 **특징 맵(Feature Map) 간의 상관관계(Correlation)를 나타내는 행렬**

![image](https://github.com/user-attachments/assets/9a1b1a81-1166-4513-b957-d909b8f948e1)

즉, 특징 맵의 채널(필터) 간 **유사도(Style Information)** 를 저장하는 역할. 스타일이란 개별적인 픽셀의 값이 아니라, 전체적인 패턴과 질감에 대한 정보이기 때문.

## 2. 직접 내적하지 않는 이유

### (1) 스타일은 위치 정보가 중요하지 않음
- 콘텐츠 손실(Content Loss)은 픽셀 단위로 유사성을 측정하지만, 스타일은 픽셀이 어디에 위치하는지보다는 전체적인 질감과 패턴을 유지하는 것이 중요.
- 만약 스타일 이미지와 생성된 이미지의 특징 맵을 직접 비교하면, 스타일이 비슷하지만 위치가 다를 경우에도 큰 손실이 발생할 수 있음.
### (2) Gram Matrix는 공간 정보를 제거함
- 스타일 이미지와 생성된 이미지의 특징 맵을 각각 Gram Matrix로 변환하면, 특징 간의 **공간적 배치 정보(Position Information)** 가 사라지고, 전체적인 통계적 특성만 남게 됨.
- 즉, 스타일의 전체적인 분포가 유지되는지 확인하는 역할을 함.
### (3) 예제: 색깔을 섞어도 같은 스타일로 인식
예를 들어, 스타일 이미지가 붓 터치 질감이 강한 인상파 그림이라고 가정한다면

- 스타일 이미지의 붓 터치가 어디에 있느냐보다는 전체적으로 얼마나 강하게, 어떤 패턴으로 분포하는지가 중요.
- 생성된 이미지도 같은 붓 터치 패턴을 가지면, 위치가 다르더라도 같은 스타일로 간주해야 함.
- 이를 위해, 특징 맵의 Gram Matrix를 비교하여 스타일을 학습하는 것.

## 3. 정리
- 스타일은 "특징의 상대적인 강도"를 표현하는 것이지, "특징이 어디에 있는가"가 중요하지 않음.
- Gram Matrix를 사용하면 공간적 배치를 무시하고 스타일의 통계적 특성을 비교할 수 있음.
- 스타일 이미지와 생성된 이미지를 직접 비교하는 것이 아니라, 각각의 Gram Matrix를 비교해야 진짜 스타일을 유지할 수 있음.
