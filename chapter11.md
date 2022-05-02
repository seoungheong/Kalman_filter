# 칼만필터 기울기 자세 측정하기

> 가속도계(accelerometer),  자이로스코프(gyroscope)로 수평자세를 찾아내는것
>
> 오일러 각도와 각속도의 관계
> 
> ![image](https://user-images.githubusercontent.com/65435447/166209114-f897aeac-ea1c-4ef1-8f85-7c2035733cbe.png)
>
> 코드 1

> 가속도계를 이용하여 자세 결정하기
> 
> 가속도계로 측정한 가속도(f_x, f_y, f_z)에는 중력 가속도와 속도의 크기나 방향이 바뀔 때 생기는 가속도 등 다양한 종류의 가속도가 포함되어 있다. 이런 특성을 수식으로 표현하면 다음과 같다.
> 
> ![image](https://user-images.githubusercontent.com/65435447/166228601-18a3378f-50b9-4302-bea4-599989cfdd07.png)
> 
> u,v,w 는 이동 속도를 의미하고 p, q, r은 회전 각속도를 의미한다. 그리고 g는 중력 가속도를 나타낸다.
> 
> ![image](https://user-images.githubusercontent.com/65435447/166228895-1c72b401-c518-46e3-887b-161870212064.png)
>
> 따라서 나머지 항의 값을 모두 알면, 이 식으로 수평 자세를 계산할 수 있다.
> 
> 먼저 시스템이 정지해 있을 때를 생각해보자. 움직이지 않으면 이동 속도와 이동 가속도는 모두 0이 됩니다.
> 
> ![image](https://user-images.githubusercontent.com/65435447/166229222-57c000b1-1f50-4f56-9ad5-99681add1c16.png)
> 
> 만약 일정한 속도로 직진하근 경우 이동가속도는 0이 된다 그리고 자세의 변화가 없으니 각속도도 0이 된다.
> 
> ![image](https://user-images.githubusercontent.com/65435447/166229222-57c000b1-1f50-4f56-9ad5-99681add1c16.png)
> 
> 두 경우 모두에서 식의 우변에 있는 첫 번째 항과 두 번째 항이 0이 된다. 그러면 다음과 같이 식이 변형된다.
> 
> ![image](https://user-images.githubusercontent.com/65435447/166229515-e5cb06a9-e553-46a4-9d4f-48c2a358f163.png)
> 
> 이 식에서 다음과 같은 롤각과 피치각의 공식을 유도해 낼 수 있다.
> 
> ![image](https://user-images.githubusercontent.com/65435447/166229593-244555ac-25ae-4691-9ed0-187235eb5cf2.png)

> 
> 
> 
> 
> 
> 
> 
> 
> .
