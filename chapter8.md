# 칼만 필터 예제

## ex1)

>전압을 0.2초 간격으로 측정한다. 이때 전압을 안정적으로 만드는 칼만 필터를 구해라.

> ![image](https://user-images.githubusercontent.com/65435447/165508030-fdfd41d0-3c72-4257-ba8d-6b94d6cdacf0.png)
> 
> <시스템 모델>

> 식의 의미 배터리 전압이 일정하게 유지되고 있으며, 그 값은 14볼트라는 뜻이다. V_k는 잡음을 의미한다.(표준편차 2인 정규분포를 따르는 신호)

> ![image](https://user-images.githubusercontent.com/65435447/165509443-bff55886-ee49-4d95-98f3-0d13f5df0fb3.png)
> 
> Q가 0인 이유는 W_k가 없기 때문이다. 이 말은 분산이 0이라는 말이다.

> 초기값에 대한 정보가 전혀 없다면 오차 공분산을 크게 잡는 게 좋다.
> 
> ![image](https://user-images.githubusercontent.com/65435447/165509740-35ed3de5-3caf-4b42-badc-e7a2d0bc7714.png)


