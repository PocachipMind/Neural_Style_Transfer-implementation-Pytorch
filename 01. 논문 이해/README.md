# 논문 읽어보기 Abstract 읽기 전 팁

abstract은 논문 전체 내용을 짧은 문단으로 요약한 요약본이다. 
그렇기 때문에 여기에 어떤 연구를 진행했는지 그리고 뭘 새롭게 제시했는지 결과가 어떻게 나왔는지 등 내용이 축약되어서 적혀있으므로 중요합니다. 

이 abstract만 보고도 논문의 전체 내용이 이해가 되어야 합니다. 

만약 그렇지 못한다고 한다면 이 논문을 이해할 사진 지식이 부족한 것일 수 있습니다.

그러면 사전지식을 공부하고 논문을 다시 읽거나 아니면 다른 사람들도 많이 보는 유명한 논문인지 먼저 체크하시오.

# Abstract 
![image](https://github.com/user-attachments/assets/883aaa3e-eb94-4ce6-9358-74efcf2c3bf5)

# Introduction 읽기 전 팁

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

