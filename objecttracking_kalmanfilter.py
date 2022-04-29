import matplotlib.pyplot as plt
import numpy as np

class Kalman_filter():

    def __init__ (self):
        # 초기 설정값
        self.dt = 1
        self.A = np.array([[1, self.dt, 0, 0 ], [0, 1, 0 , 0],[0 ,0 ,1, self.dt],[0, 0, 0, 1]])
        self.H = np.array([[1, 0, 0, 0],[0, 0, 1, 0]])
        self.Q = np.eye(4)
        self.R = 50*np.eye(2)

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

    X += 15*np.random.rand()
    Y += 15*np.random.rand()

def main():

    global X, Y

    X = 0
    Y = 0

    true_X = []
    true_Y = []

    k_X = []
    k_Y = []

    K = Kalman_filter()

    for i in range(50):
        Ball_pos()
        true_Y.append(Y)
        true_X.append(X)

        tmp_x , tmp_y = K.filtering([X,Y])

        k_X.append(tmp_x)
        k_Y.append(tmp_y)

    plt.plot(true_X, true_Y, 'ro', label = 'true')
    plt.plot(k_X, k_Y, 'bv', label='k')
    plt.legend()
    plt.show()


if __name__ == '__main__':

    main()