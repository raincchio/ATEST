import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['axes.unicode_minus'] = False
def sigmoid(x):
    return 1.0/(1.0+np.exp(-x))
def tanh(x):
    return (np.exp(x) - np.exp(-x))/(np.exp(x)+np.exp(-x))
x = np.linspace(-8,8)
fig = plt.figure(figsize = (12,4))

plt.plot(x, tanh(x))
plt.plot(x, sigmoid(x))
plt.show()