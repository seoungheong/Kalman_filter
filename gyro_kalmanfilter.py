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

    def sinPhi(self):

        return np.sin(self.Phi)

    def cosPhi(self):

        return np.cos(self.Phi)

    def cosTheta(self):

        return np.cos(self.Theta)

    def tanTheta(self):

        return np.tan(self.Theta)

    def filtering(self, p, q, r):

        self.Phi = self.Phi + self.dt * (p + q * self.sinPhi() * self.tanTheta() + r * self.cosPhi() * self.tanTheta())
        self.Theta = self.Theta + self.dt * (q * self.cosPhi() - r * self.sinPhi())
        self.Psi = self.Psi + self.dt * ( q * self.sinPhi() / self.cosTheta() + r * self.cosPhi() / self.cosTheta())

        return self.Phi * 180/np.pi, self.Theta* 180/np.pi, self.Psi* 180/np.pi

def get_data():
    input_mat = io.loadmat('./ArsGyro.mat')


    data_set = np.zeros([Nsamples, 3])

    for k in range(Nsamples):
        ax = input_mat['wx'][k][0]  # (41500, 1)
        ay = input_mat['wy'][k][0]  # (41500, 1)
        az = input_mat['wz'][k][0]  # (41500, 1)

        data_set[k]=[ax, ay, az]

    return data_set

def main():

    data_set = get_data()

    K = kalman_filter()

    t_p = []
    t_q =[]

    p_data = []
    q_data = []

    X = np.array(range(Nsamples)) * 0.01

    for i in range(Nsamples):
        p, q, r =K.filtering(data_set[i][0],data_set[i][1],data_set[i][2])

        t_p.append(data_set[i][0])
        t_q.append(data_set[i][1])

        p_data.append(p)
        q_data.append(q)


    plt.plot(X, p_data, 'r', label = 'phi')
    plt.legend()
    plt.show()
    plt.plot(X, q_data, 'r', label='theta')
    plt.legend()
    plt.show()
    plt.plot(X, t_p, 'r', label='psi')
    plt.legend()
    plt.show()
    plt.plot(X, t_q, 'r', label='psi')
    plt.legend()
    plt.show()

if __name__ == '__main__':

    main()