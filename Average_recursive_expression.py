import matplotlib.pyplot as plt
import random
#########################################################################
def Average_recursive_expression(before_mean, next_number, index):

    alpha = (index-1)/index

    mean = alpha * before_mean + ( 1 - alpha ) * next_number

    return mean

#########################################################################
# ex).1

mean = 0

for i in range(1,10):
    mean = Average_recursive_expression(mean, i, i)
    print(i)

print('Average is : %f ' % mean)
#########################################################################
# ex).2

def random_num():
    w = 0 + 4 * random.random()
    z = 14.4 + w
    return z

x=[]
y=[]
means=[]
mean=0

for i in range(1,101):
   x.append(i)
   num = random_num()
   y.append(num)
   mean = Average_recursive_expression(mean, num, i)
   means.append(mean)

plt.plot(x,y,'ro--', label='Measured')
plt.plot(x,means, 'g^', label='Average')

plt.legend()
plt.show()
