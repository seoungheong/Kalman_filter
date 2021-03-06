# 영상 속의 물체 추적하기

> 평면 상의 표적 추적에 칼만 필터를 적용하기 위해서 위치-속도 모델을 2차원으로 확장해야 한다.
> x = {X_위치, X_속도, Y_위치, Y_속도}

> ![image](https://user-images.githubusercontent.com/65435447/165943620-18b1a18e-f4d6-4d77-b60f-8d60def8bcb6.png)
>
> ![image](https://user-images.githubusercontent.com/65435447/165944410-5cb8eb19-5d40-4d53-a96c-0351a35f25a0.png)

[링크](objecttracking_kalmanfilter.py)


### Q, R 행렬 변경

Q의 값이 커지면 칼만 이득이 커지면서, 결과적으로 측정값의 반영 비율이 더 높아진다. 즉 추정 결과가 측정값에 더 가까워진다.
Q의 값이 작아지면 칼만 이득이 작아지면서, 결과적으로 추정 결과는 측정값의 영향을 덜받고 이전 추정값과 비슷해진다.

R의 값이 커지면 칼만 이득이 작아지면서, 결과적으로 추정 결과는 측정값의 영향을 덜받고 이전 추정값과 비슷해진다.
R의 값이 작아지면 칼만 이득이 커지면서, 결과적으로 측정값의 반영 비율이 더 높아진다. 즉 추정 결과가 측정값에 더 가까워진다.

추정값이 커지면 부드러워지며 부드러워진다.

[링크](objecttracking_kalmanfilter.py)
