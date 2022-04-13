import random
import matplotlib.pyplot as plt

#1차 저주파 통과 필터(=지수 가중 이동평균 필터)

def Exponentially_weighted_moving_average_filter(before_average, new_value, alpha):

    average = alpha * before_average + ( 1 - alpha ) * new_value

    return average

###################################################################################
#ex).1

def randomgen(count):
    return count + (100 * random.random()) * random.random()

x = range(1, 101)
real = []
y1 = []
y2 = []

mean1 = 0
mean2 = 0

alpha1 = 0.9
alpha2 = 0.3

count = 0

for i in range(1, 101):

    if i%20 == 0:
        print('in')
        count += (100 * random.random()) * random.random()

    value = randomgen(count)

    mean1 = Exponentially_weighted_moving_average_filter(mean1, value, alpha1)
    mean2 = Exponentially_weighted_moving_average_filter(mean2, value, alpha2)

    y1.append(mean1)
    y2.append(mean2)
    real.append(value)

plt.plot(x, real, label = 'real')
plt.plot(x, y1, label = 'alpha = 0.6')
plt.plot(x, y2, label = 'alpha = 0.4')

plt.legend()
plt.show()