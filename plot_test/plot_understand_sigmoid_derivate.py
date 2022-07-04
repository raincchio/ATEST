import numpy as np

def sigmoid(x):
    return 1/(1+ np.exp(-x))


def derivate(x):
    return sigmoid(x)*(1-sigmoid(x))


x= np.arange(-3, 3,0.01)

y1 = sigmoid(x)
y2 = 2*sigmoid(2*x)
y3 = sigmoid(4*x)

z1 = derivate(x)
z2 = derivate(2*x)*2*2
z3 = derivate(4*x)*4

from matplotlib import pyplot as plt

fig, ax = plt.subplots(1,2)
ax[0].plot(x,y1, label='y1')
ax[0].plot(x,y2, label='y2')
ax[0].plot(x,y3, label='y3')

ax[1].plot(x,z1, label='z1')
ax[1].plot(x,z2, label='z2')
ax[1].plot(x,z3, label='z3')

ax[0].legend()
ax[1].legend()
plt.show()

