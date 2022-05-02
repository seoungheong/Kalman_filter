import matplotlib.pyplot as plt
import numpy as np
from scipy import io

Nsamples = 41500

class kalman_filter:

    def __init__(self):
        self.Phi = 0
        self.Theta = 0
        self.Psi = 0
        self.dt = 0.01
        self.g = 9.8

    def filtering(self, ax, ay, az):

        self.Threta = np.arcsin(ax/self.g)
        self.Phi = np.arcsin(-ay/(self.g*np.cos(self.Threta)))

        return self.Threta * 180/np.pi, self.Phi * 180/np.pi


def get_data():
    input_mat = io.loadmat('./ArsAccel.mat')


    data_set = np.zeros([Nsamples, 3])

    for k in range(Nsamples):
        ax = input_mat['fx'][k][0]  # (41500, 1)
        ay = input_mat['fy'][k][0]  # (41500, 1)
        az = input_mat['fz'][k][0]  # (41500, 1)

        data_set[k]=[ax, ay, az]

    return data_set

def main():

    data_set = get_data()

    K = kalman_filter()

    X = np.array( range(Nsamples) )* 0.01

    t_p=[]
    t_t=[]

    Phi=[]
    Theta=[]

    for i in range(Nsamples):

        x, y, z = data_set[i]

        p, t = K.filtering(x, y, z)

        t_p.append(x)
        t_t.append(y)

        Phi.append(p)
        Theta.append(t)

    plt.plot(X, Phi, 'r', label='phi')
    plt.legend()
    plt.show()
    plt.plot(X, Theta, 'r', label='theta')
    plt.legend()
    plt.show()
    plt.plot(X, t_p, 'r', label='psi')
    plt.legend()
    plt.show()
    plt.plot(X, t_t, 'r', label='psi')
    plt.legend()
    plt.show()


if __name__ == '__main__':

    main()