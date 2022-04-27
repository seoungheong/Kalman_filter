import matplotlib.pyplot as plt
import random
import numpy as np

class kalman_filter:

    def __init__(self):
        # 초기 설정값
        self.A = np.array([1])
        self.H = np.array([1])
        self.Q = np.array([0])
        self.R = np.array([4])

         # 초기 값
        self.X = 14
        self.P = 6

    def filtering(self, value):
        x_p = self.A * self.X
        P_p = self.A * self.P * self.A.T + self.Q
        K = P_p * self.H.T / (self.H * P_p * self.H.T + self.R)

        self.X = x_p + K * (value - self.H * x_p)

        self.P = P_p - K * self.H * P_p

        P_x = self.P

        return self.X, K, P_x

def volt_generater():
    return 14.4 + 4 * np.random.randn(1, 1)

def main():
    K = kalman_filter()

    X = range(30)
    vol = []
    Vol = []
    Ks = []
    Ps = []

    for i in X:
        tmps = float(volt_generater())
        vol.append(tmps)
        vol_val, K_val, P_val = K.filtering(tmps)
        Vol.append( vol_val )
        Ks.append(K_val)
        Ps.append(P_val)

    plt.subplot(2, 2, 1)
    plt.plot( X, vol, 'ro--', label='Measured' )
    plt.plot( X, Vol, 'g^--', label='Measured')
    plt.legend()

    plt.subplot(2, 2, 2)
    plt.plot(X, Ks, 'ro--', label='Kalman_benefit')
    plt.legend()

    plt.subplot(2, 2, 3)
    plt.plot(X, Ps, 'ro--', label='error_covariance')
    plt.legend()

    plt.show()


if __name__ == "__main__":
	main()