import matplotlib.pyplot as plt
import random
import numpy as np

# 속도가 일정할 경우 위치 추정

class kalman_filter:

    def __init__(self):
        # 초기 설정값
        self.dt = 0.1
        self.A = np.array([[1, self.dt],[0,1]])
        self.H = np.array([1,0])
        self.Q = np.array([[1,0],[0,3]])
        self.R = np.array([10])

         # 초기 값
        self.X = np.array([0, 20])
        self.P = 5*np.eye(2)

    def filtering(self, value):
        x_p = self.A @ self.X
        P_p = self.A @ self.P @ self.A.T + self.Q

        K = (P_p @ self.H.T) / (self.H @ P_p @ self.H.T + self.R)

        self.X = x_p + K * (value - self.H @ x_p)


        self.P = P_p - (K @ self.H) * P_p


        return self.X

def get_pos():

    global Pos_true, Vel_true, z

    w = 0 + 10*np.random.randn()
    v = 0 + 10*np.random.randn()

    z = Pos_true + Vel_true * 0.1 + v

    Pos_true = z - v
    Vel_true = 80 + w

def main():

    global Pos_true, Vel_true, z
    Pos_true = 0
    Vel_true = 80

    K = kalman_filter()

    X = np.array(range(0, 100))*0.1
    Posps = []
    Velps = []

    pos = []
    vel = []
    Z = []

    for i in X:

        get_pos()
        Posps.append(Pos_true)
        Z.append(z)
        Velps.append(Vel_true)

        a, b = K.filtering(z)
        pos.append(a)
        vel.append(b)

    plt.subplot(2, 2, 1)
    plt.plot( X, Posps, "ro--", label='Measurements',markersize=2)
    plt.plot( X, pos, "bv--", label='Kalman Filter',markersize=2)
    plt.legend()

    plt.subplot(2, 2, 2)
    plt.plot(X, Velps, "r--", label='Measurements')
    plt.plot(X, vel, "b--", label='Kalman Filter')
    plt.legend()
    plt.show()

if __name__ == "__main__":
	main()