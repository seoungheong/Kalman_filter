from collections import deque
import matplotlib.pyplot as plt
import random

def Moving_average_filter( before_data_deque, before_Moving_average, new_data ):

    if len(before_data_deque)!=0:

        size = len(before_data_deque)

        if(before_data_deque.maxlen > size):
            size += 1
            oldest_data = before_data_deque.popleft()
            before_data_deque.appendleft(oldest_data)

        else:
            oldest_data = before_data_deque.popleft()

    else:
        size = 1
        oldest_data = 0


    Moving_average = before_Moving_average + (new_data - oldest_data)/size

    before_data_deque.append(new_data)

    return Moving_average, before_data_deque

#####################################################################################
#ex).1
data_queue =deque( maxlen = 10 )

def random_num(count):
    w = 0 + 10 * random.random()
    z = count + w
    return z

x=[]
y=[]
means=[]
mean=0

count = 0

for i in range(1,101):

    x.append(i)
    num = random_num(count)
    y.append(num)
    mean, data_queue = Moving_average_filter(data_queue, mean, num)
    means.append(mean)



    if i % 5 == 0:
        count += 100 * random.random()

    print(data_queue)

plt.plot(x,y,'ro--', label='Measured')
plt.plot(x,means, 'g^', label='Average')

plt.legend()
plt.show()

#####################################################################################

