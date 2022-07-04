import numpy as np

mymeans = [13,5]
# stdevs = sqrt(5),sqrt(2)
# corr = .3 / (sqrt(5)*sqrt(2) = .134
mycov = [[5,.3], [.3,2]]
print(np.cov(np.random.multivariate_normal(mymeans,mycov,500000).T))

print(np.corrcoef(np.random.multivariate_normal(mymeans,mycov,500000).T))