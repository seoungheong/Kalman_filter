# 확장 칼만 필터(extended Kalman filter, EKF)

> 단점: 알고리즘이 발산할 위험이 있다.

### 선형화 칼만 필터(Linearized Kalman filter)

> ![image](https://user-images.githubusercontent.com/65435447/167803159-d9eec843-2557-4bde-80a4-16748f5b1729.png)
>
> ![image](https://user-images.githubusercontent.com/65435447/167803241-ff09e687-fb25-4935-9ce7-112b36cc831e.png)
>
> ![image](https://user-images.githubusercontent.com/65435447/167803329-b812afe6-9f8a-4702-9238-742c583320a4.png)
>
> ![image](https://user-images.githubusercontent.com/65435447/167803820-daedfcd0-fc22-4ccb-99d3-6b7cd09b3f10.png)
>
> 첫번째가 EKF의 관계식, 두번째가 선형 칼만 필터식
>
> ![image](https://user-images.githubusercontent.com/65435447/167804056-e3a0491f-d62b-4647-a7a8-140233be1dc5.png)
>
> 다음과 같이 우변이 서로 다른것을 확인할 수 있다.
>
> ![image](https://user-images.githubusercontent.com/65435447/167804274-44c76494-8086-4b70-a4ff-26ded3cc2a52.png)
>
> ![image](https://user-images.githubusercontent.com/65435447/167804354-241ad484-751b-4d80-9dcb-1455675fdc6c.png)
>
> 마지막 항이 다른것을 확인할 수 있다.
>
> ![image](https://user-images.githubusercontent.com/65435447/167804610-f6ccfcd5-b81a-486a-a6eb-e7e87dde28d7.png)
>
> 두 식의 차이를 비교해보면 다음 그림과 같다.
> 기존 위치에 비선형 모델의 관계식을 사용한다.
> 
> ![image](https://user-images.githubusercontent.com/65435447/167805875-e37e5843-2cb8-4c55-8883-a02632b11679.png)
>
>.




