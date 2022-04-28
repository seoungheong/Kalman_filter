import matplotlib.pyplot as plt
import numpy as np
from scipy import io

#속도가 일정하지 않을 경우 위치 추정

input_mat = io.loadmat('SonarAlt.mat')

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

def get_sonar(i):
    """Measure sonar."""
    global z

    z = input_mat['sonarAlt'][0][i]  # input_mat['sonaralt']: (1, 1501)

def main():

    global z

    K = kalman_filter()

    X = np.array(range(0, 500))*0.1

    pos = []
    vel = []
    Z = []

    for i in X:
        get_sonar(int(i*10))

        Z.append(z)

        a, b = K.filtering(z)
        pos.append(a)
        vel.append(b)

    plt.subplot(1, 1, 1)
    plt.plot( X, Z, "ro--", label='Measurements',markersize=2)
    plt.plot( X, pos, "bv--", label='Kalman Filter',markersize=2)
    plt.legend()
    plt.show()

    plt.subplot(1, 1, 1)
    plt.plot(X, pos, "ro--", label='distance', markersize=2)
    plt.plot(X, vel, "bv--", label='velocity', markersize=2)
    plt.legend()
    plt.show()


if __name__ == "__main__":
	main()