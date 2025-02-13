# Abstract 읽기 전

abstract은 논문 전체 내용을 짧은 문단으로 요약한 요약본이다. 
그렇기 때문에 여기에 어떤 연구를 진행했는지 그리고 뭘 새롭게 제시했는지 결과가 어떻게 나왔는지 등 내용이 축약되어서 적혀있으므로 중요합니다. 

이 abstract만 보고도 논문의 전체 내용이 이해가 되어야 합니다. 

만약 그렇지 못한다고 한다면 이 논문을 이해할 사진 지식이 부족한 것일 수 있습니다.

그러면 사전지식을 공부하고 논문을 다시 읽거나 아니면 다른 사람들도 많이 보는 유명한 논문인지 먼저 체크하시오.

# Abstract
![image](https://github.com/user-attachments/assets/883aaa3e-eb94-4ce6-9358-74efcf2c3bf5)

# Introduction 읽기 전

Introduction은 보통 크게 세가지를 포함하고 있습니다.

1. 인트로덕션 Introduction은 이 연구를 시작하게 된 계기를 소개합니다. 그리고 이 연구가 왜 흥미로운지도 설명하면서 본문을 읽는 사람이 뒷내용을 읽고 싶게끔 흥미 유발하는 역할 합니다.

2.  보통은 이 과정에서 이 연구와 관련되어 있는 다른 연구들이 지금까지 어떻게 진행되어 왔는지를 소개하고 그리고 그 과거의 연구들의 한계점이 무엇이었는지를 설명하는 Related Work 소개가 있습니다.

3.  이 연구를 통해서 어떤 것을 실험했고 어떤 결과가 나왔고 이런 결과들을 간략하게 소개를 하고 이 연구가 이 분야에서 어떤 컨트리뷰션이 있었는지 즉 이 연구가 얼마나 임팩트 있는 결과를 갖고 왔는지 소개 합니다.

인트로덕션을 읽는 이유는 이 연구에 대한 흐름이나 저자가 제시하고자 하는 문제점을 이해하고 싶을 때 보는데, 그래서 논문의 주요한 기능 부분을 이해하려고 논문을 본다고 한다면 보통 인트로덕션 부분은 그냥 건너 뜁니다. 

예를들어 지금 같은 경우 논문을 구현할 것인 경우 인트로덕션 부분은 크게 필요가 없습니다. 

### Tip

논문 리뷰를 해야 된다거나 이제 논문을 좀 자세하게 이해해야 된다 그런게 아니라면 사실 인트로덕션은 그냥 건너뛰고 봐도 큰 문제가 없습니다. 

# Introduction

### Introduction
style transfer 라는 task에 대한 간략한 소개
### Related Works
- 이전의 style transfer는 image의 texture를 합성하는 방식이고 non-parametric 알고리즘과 같은 방식이 존재한다.
- 이전의 대부분의 style transfer 알고리즘은 근본적인 한계가 있다.
  - target image의 low-level feature만 활용
  - 이미지의 유의미한 content와 style을 각기 분리해야 하지만 한계가 있음
### Our Works
- CNN의 발전으로 high-level semantic information extraction 이 가능
- 이 연구에서 CNN을 활용한 A Neural Algorithm of Artistic Style 을 새롭게 제시
- 이미지의 content와 style을 독립적으로 처리하며 또한, 분리하거나 재결합 할 수 있음

# Method 읽기 전

Figure 1 같이 이미지가 나 올 경우 해당 이미지가 쓰이는 곳까지 독해를 하고 읽고난 이후 이미지를 보는것이 이해에 좋다.

보통 Method 라고 해서 논문의 가장 중요한 알고리즘이 되는 방법론을 제시하는 부분이 여기입니다. 

2. Deep image representations 부분 부터 논문의 가장 중요한 부분입니다.

# Deep Image Representation

![image](https://github.com/user-attachments/assets/75b41881-e33d-4314-95a8-733dc05e32d4)

### VGG19
![image](https://github.com/user-attachments/assets/ddcbe245-d40e-4d55-b17a-feb83a5db4d1)

VGG19란 네트워크는 클래스 분류 테스크를 수행하는 네트워크.

미리 학습되어 있는 프리트레인된 모델. 

파란색이 컨볼루셔널 네트워크의 엑티베이션 함수

노란색이 Pooling 레이어.

5개의 CNN 블럭으로 존재하는 이카텍쳐


# Content representation

Deep Image Representation이 VGG 네트워크의 Feature Map으로 표현된다는 것을 알았습니다.

그러면 Content representation과 Style Representation도 VGG 네트워크의 Feature Map으로 표현된다고 예상할 수 있을것입니다.

기호가 등장하면 절때 대충 읽지 말고 그 기호가 무엇을 의미하는지 정확하게 이해하고 넘어가도록 할 것.

기호만 잘 이해해도 논문이 다 이해가 되고 기호만 잘 이해하고 있어도 논문 구현이 쉽습니다. 

반대로 만약 어떤 새로운 기호가 등장했는데 이 기호에 대한 정의가 논문에서 설명이 안 되어있다면 논문의 잘못임. 논문엔 특정 기호에 대해 모두 설명을 해야합니다. 

기호를 정확하게 이해하고 그 다음에 수식을 보면 어떻게 구현할지 다 보입니다.

![image](https://github.com/user-attachments/assets/0a9d42fe-2e53-430f-a3d3-d85d9c7519ad)

![image](https://github.com/user-attachments/assets/7cb99a8c-9042-4bbd-8f95-1f15386cac93)

마지막 나온 F가 컨텐츠 레프레젠테이션( Content Representation )

# Content representation - Loss

![image](https://github.com/user-attachments/assets/4c41598d-d81c-46a1-a85f-137c61b459b2)

![image](https://github.com/user-attachments/assets/0022b01e-6d6d-438d-b2b5-43cfcc73280d)

아래부분은 그래디언트 디센트 구하는 부분

# Style representation

![image](https://github.com/user-attachments/assets/25573e95-9fb0-4788-9020-fc5991c416b3)

초록색 부분은 모두 같은 것을 호칭

# Style representation - Gram Matrix

Gram Matrix = 자기 자신의 내적. 매트릭스의 자기 자신의 내적

![image](https://github.com/user-attachments/assets/1f5e04b8-2201-469e-9848-4fdf10ac6d89)


Gram Matrix가 Correlation을 표현하므로 

선형대수의 내적 Correlation

# Style representation - Loss

![image](https://github.com/user-attachments/assets/1a73a2dd-c259-49ad-aaf7-e4559a87b186)

# Train

알파와 베타는 하이퍼파라미터입니다. 학습할때 하이퍼파라미터 튜닝을 해야합니다. 

아래 Result 부분에 하이퍼파라미터 비율 참고하면서 하이퍼파라미터 튜닝합니다.

# Figure 2 ) Style transfer algotithm

![image](https://github.com/user-attachments/assets/5acfd21e-761f-4108-99df-145f2e7259ba)

해당 논문의 전체 파이프라인 보여주는 모식도.

해당 그림이 이해 되어야 Style transfer 논문이 이해되었다 볼 수 있음.

우린 처음에 노이즈였던 저 이미지를 업데이트 해갈 것임
