import matplotlib.pyplot as plt
import numpy as np

r = np.arange(0,10,0.01)

def sigmoid(x):
    return 1/(1+np.exp(-x))

y = sigmoid(r)*(1-sigmoid(r))*1/sigmoid(r)


plt.plot(r,y)
plt.xlabel('r')
plt.ylabel(r'$\nabla_r L$')
plt.show()