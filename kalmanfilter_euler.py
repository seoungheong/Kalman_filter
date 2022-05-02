import matplotlib.pyplot as plt
import numpy as np
from scipy import io

Nsamples = 41500

class kalman_filter:

    def __init__(self):
        self.H = np.eye(4)
        self.Q = 0.0001 * np.eye(4)
        self.R = 10 * np.eye(4)
        self.X = np.array([1,0,0,0]).T
        self.P = np.eye(4)

    def filtering(self, A, z):

        Xp = A @ self.X
        Pp = A @ self.P @ A.T + self.Q

        K = (Pp @ self.H.T) @ np.linalg.inv(self.H @ Pp @ self.H.T + self.R)

        self.X = Xp + K @ (z - self.H @ Xp)
        self.P = Pp - K @ self.H @ Pp

        phi = np.arctan2(2 * (self.X[2] * self.X[3] + self.X[0] * self.X[1]), 1 - 2 * (self.X[1] ** 2 + self.X[2] ** 2))
        theta = -np.arcsin(2 * (self.X[1] * self.X[3] - self.X[0] * self.X[2]))
        psi = np.arctan2(2 * (self.X[1] * self.X[2] + self.X[0] * self.X[3]), 1 - 2 * (self.X[2] ** 2 + self.X[3] ** 2))

        return phi, theta, psi

def EulerAccel(ax, ay, az):
    g = 9.8
    theta = np.arcsin(ax / g)
    phi = np.arcsin(-ay / (g * np.cos(theta)))
    return phi, theta

def get_data():
    input_gyro = io.loadmat('./ArsGyro.mat')
    input_accel = io.loadmat('./ArsAccel.mat')

    data_gyro = np.zeros([Nsamples, 3])
    data_accel = np.zeros([Nsamples, 3])

    for k in range(Nsamples):
        ax = input_gyro['wx'][k][0]  # (41500, 1)
        ay = input_gyro['wy'][k][0]  # (41500, 1)
        az = input_gyro['wz'][k][0]  # (41500, 1)
        data_gyro[k]=[ax, ay, az]

        ax = input_accel['fx'][k][0]  # (41500, 1)
        ay = input_accel['fy'][k][0]  # (41500, 1)
        az = input_accel['fz'][k][0]  # (41500, 1)
        data_accel[k]=[ax, ay, az]

    return data_gyro, data_accel

def generater_A(p,q,r,dt) :
    return np.eye(4) + dt * 0.5 *np.array([[0,-p,-q,-r],[p,0,r,-q],[q,-r,0,p],[r,q,-p,0]])

def generater_z(phi, theta, psi):
    sinPhi = np.sin(phi/2)
    sinTheta = np.sin(theta/2)
    sinPsi = np.sin(psi/2)
    cosPhi = np.cos(phi/2)
    cosTheta = np.cos(theta/2)
    cosPsi = np.cos(psi/2)

    return np.array([cosPhi*cosTheta*cosPsi + sinPhi*sinTheta*sinPsi,
                     sinPhi*cosTheta*cosPsi - cosPhi*sinTheta*sinPsi,
                     cosPhi*sinTheta*cosPsi + sinPhi*cosTheta*sinPsi,
                     cosPhi*cosTheta*sinPsi - sinPhi*sinTheta*cosPsi])

def main():
    print('start')

    data_gyro, data_accel = get_data()

    dt = 0.01

    K = kalman_filter()

    phi_save = []
    theta_save = []
    psi_save = []

    X = np.array(range(Nsamples))*0.01

    for i in range(Nsamples):

        p,q,r = data_gyro[i]

        A = generater_A(p,q,r,dt)

        a,b,c = data_accel[i]
        phi, theta = EulerAccel(a,b,c)

        z = generater_z(phi, theta, 0)

        phi, theta, psi = K.filtering(A,z)

        phi_save.append(phi)
        theta_save.append(theta)
        psi_save.append(psi)

    phi_save = np.array(phi_save) * 180 / np.pi
    theta_save = np.array(theta_save) * 180 / np.pi
    psi_save = np.array(psi_save) * 180/np.pi

    plt.plot(X, phi_save, 'r', label='phi')
    plt.legend()
    plt.show()

    plt.plot(X, theta_save, 'r', label='theta')
    plt.legend()
    plt.show()

    plt.plot(X, psi_save, 'r', label='psi')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()