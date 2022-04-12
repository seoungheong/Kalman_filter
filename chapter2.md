# 이동평균(Moving average) 필터

## 이동평균(Moving average)?
> 평균을 취하면 측정 데이터에서 잡음을 제거할 수 있다. 하지만 측정하려는 물리량이 시간에 따라 변하는 경우 평균선을 취하는건 적절하지 않습니다. 평균은 데이터의 동적인 변화를 모두 없애버리고 측정 데이터를 뭉뜽그려 하나의 값만 내놓기 때문이다. 따라서 잡음을 없애는 동시에 시스템의 동적인 변화를 재대로 반영하는 방법이 이동평균이다.

![image](https://user-images.githubusercontent.com/65435447/162951503-0058c873-a1f6-418e-bd21-e465b7a7ba3d.png)

<출처 wiki: [링크](https://ko.wikipedia.org/wiki/%EC%9D%B4%EB%8F%99%ED%8F%89%EA%B7%A0)>

## 재귀식

![image](https://user-images.githubusercontent.com/65435447/162952017-0cc34ed3-9de4-4c3f-add3-e6adbe1ec845.png)

<출처 wiki: [링크](https://ko.wikipedia.org/wiki/%EC%9D%B4%EB%8F%99%ED%8F%89%EA%B7%A0)>

>하지만 이통평균 재귀식을 구현하면 평균필터와 달리 재귀식을 사용하는 이점이 별로 없다. 직전 이동 평균과 가장 오래된 데이터가 필요

>[코드 샘플](Moving_average_expression.py)
