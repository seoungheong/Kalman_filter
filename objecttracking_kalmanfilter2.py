import matplotlib.pyplot as plt
import numpy as np

class Kalman_filter():

    def __init__ (self, R, Q):
        # 초기 설정값
        self.dt = 1
        self.A = np.array([[1, self.dt, 0, 0 ], [0, 1, 0 , 0],[0 ,0 ,1, self.dt],[0, 0, 0, 1]])
        self.H = np.array([[1, 0, 0, 0],[0, 0, 1, 0]])
        self.Q = Q*np.eye(4)
        self.R = R*np.eye(2)

        # 초기 값
        self.X = np.array([0, 0, 0 ,0])
        self.P = 100 * np.eye(4)

    def filtering(self, value):

        xp= self.A @ self.X
        Pp = self.A @ self.P @ self.A.T + self.Q

        self.K = Pp @ self.H.T @ np.linalg.inv(self.H @ Pp @ self.H.T + self.R)

        self.X = xp + self.K @ (value - self.H @ xp)
        self.P = Pp - self.K @ self.H @ Pp

        print(self.X)

        return self.X[0], self.X[2]

def Ball_pos():

    global X, Y

    X += 10*np.random.rand() + 7*np.random.randn()
    Y += 10*np.random.rand() + 7*np.random.randn()

def main():

    global X, Y

    X = 0
    Y = 0

    true_X = []
    true_Y = []

    X1 = []
    Y1 = []
    X100 = []
    Y100 = []

    K1 = Kalman_filter(R=50, Q=0.1)
    K2 = Kalman_filter(R=50, Q=100)

    for i in range(50):
        Ball_pos()
        true_Y.append(Y)
        true_X.append(X)

        x1 , y1 = K1.filtering([X,Y])
        x100, y100 = K2.filtering([X, Y])

        X1.append(x1)
        Y1.append(y1)
        X100.append(x100)
        Y100.append(y100)


    plt.plot(true_X, true_Y, 'ro', label = 'true')
    plt.plot(X1, Y1, 'bv', label='1')
    plt.plot(X100, Y100, 'gv', label='100')
    plt.legend()
    plt.show()


if __name__ == '__main__':

    main()