import numpy as np

# R = np.random.randn(1,20)
# V = np.random.randn(1,20)

# R = np.random.randint(1,100,20)
# V = np.random.randint(1,100,20)
#
# A = R - V
# B = (A - A.mean())/A.std()
# A_ = 2*R -V
# C = A - A_.mean()
#
# print(A.var(), np.sum(A**2))
# print(B.var(), np.sum(B**2))
# print(C.var(), np.sum(C**2))


R = np.random.randint(-100,0,10)
R_mean = (R- R.mean())
print(R)
print(R.std(), R.mean())
print(R_mean//R.std())
print(R//R.std())
print(R.mean()//R.std())