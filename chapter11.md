# 칼만필터 기울기 자세 측정하기

> #### 가속도계(accelerometer),  자이로스코프(gyroscope)로 수평자세를 찾아내는것
>
> 오일러 각도와 각속도의 관계
> 
> ![image](https://user-images.githubusercontent.com/65435447/166209114-f897aeac-ea1c-4ef1-8f85-7c2035733cbe.png)
>
> 코드 1

> #### 가속도계를 이용하여 자세 결정하기
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
> 움직이는 속도가 충분히 느리거나 속도의 크기와 방향이 빠르게 변하지 않는다면 위의 식으로 수평 자세를 구할 수 있습니다.
> 
> 코드2

> #### 센서 융합을 통해 자세 결정하기
> 
> 앞의 두 센서가 상호 보완 관계임을 알 수 있다. 자이로 구한 자세는 자세 변화를 잘 감지하지만, 시간이 지남에 따라 오차가 누적되어 발산하는 문제가 있었습니다. 반면 가속도계로 구한 자세는 시간이 지나도 그 오차가 커지지 않고 일정 범위로 제한되는 장점을 가지고 있다. 즉 단기적으로는 자이로 자세가 더 낫지만, 중장기적으로는 가속도 자세가 더 좋다. 따라서 자이로의 누적 오차 문제를 가속도계로 보정하면 된다.
> 
> ![image](https://user-images.githubusercontent.com/65435447/166234367-fe828a6c-520c-40e0-a349-8ba718b0faef.png)
> 
> 우리가 관심있는 물리량은 자세이다. 따라서 자세를 상태 변수로 잡아야한다.
> 
> ![image](https://user-images.githubusercontent.com/65435447/166236438-d780d44c-ccd6-41fe-9a5b-f069f14c4664.png)
> 
> 여기서 수평 자세인![image](https://user-images.githubusercontent.com/65435447/166236487-9c148bbc-8485-4efe-b191-2466f3a35890.png)만 관심이 있다.
> 
> 앞에서 이미 자이로 각속도와 오일러 각도 사잉의 관계식을 설명했다.
> 
> ![image](https://user-images.githubusercontent.com/65435447/166236606-f402c1b0-f983-419f-aaa6-6d71b082371e.png)
> 
> 하지만 해당 모델을 사용하려면 식을 다음과 같이 표현할 수 없다.
> 
> ![image](https://user-images.githubusercontent.com/65435447/166236782-a6f7f040-7917-41c0-be17-56cb78f98d87.png)
> 
> 이러면 행렬 안에 있는 오일러 각도를 밖으로 빼낼 방법이 없다. 따라서 상태 변수를 다르게 잡아 식을 변경하는 것이다.
> 
> 오일러 각도 대신 쿼더니언(quaternion)을 상태 변수로 잡아보자. 
> 
> ![image](https://user-images.githubusercontent.com/65435447/166236999-fb17d9a8-6ca4-4f67-aef9-4aea014ce567.png)
>
> 쿼터니언의 각속도 관계 식
> 
> ![image](https://user-images.githubusercontent.com/65435447/166237102-7b5946f0-7c5f-4e78-b0b8-cd734514eea0.png)
>   
> 이렇게 하여 칼만 필터의 시스템 모델에 필요한 요구조건을 만족할 수 있다. 식을 정리하면 다음과 같이 쓸 수 있다.
>     
> ![image](https://user-images.githubusercontent.com/65435447/166237269-29003412-49e2-4ec8-a37c-406b5128b0b1.png)
>
> 측정 관계식을 유도하면 오리러 각도를 쿼터니언으로 바꾸는 공식은 다음과 같다.
>   
> ![image](https://user-images.githubusercontent.com/65435447/166237706-bfd44dd8-9f3d-4a28-b9d1-93eeeeeff374.png)
>
>  코드3

























