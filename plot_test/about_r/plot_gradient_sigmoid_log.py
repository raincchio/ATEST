import matplotlib.pyplot as plt
import numpy as np

r = np.arange(0,10,0.01)

def sigmoid(x):
    return 1/(1+np.exp(-x))

y = sigmoid(np.log(r))*(1-sigmoid(np.log(r)))*1/r



plt.plot(r,y)
plt.xlabel('r')
plt.ylabel(r'$\nabla_r L$')
plt.show()