import numpy as np

pdvals = np.random.randint(1,100,5)
pdA = pdvals/pdvals.sum()

pdvals = np.random.randint(1,100,5)
pdB = pdvals/pdvals.sum()

def entropy(pd):
    # -E[p(x)log(q(x))]
    e = 0
    for p in pd:
        e += p * np.log(p)
    return -e

def relative_entropy(pdA, pdB):
    # E[p(x)log(p(x)) - p(x)log(q(x))]
    e = 0
    for pa, pb in zip(pdA, pdB):
        e += pa * np.log(pa) - pa * np.log(pb)
    return e

def cross_entropy(pdA, pdB):
    # - E[p(x)log(q(x))]
    e = 0
    for pa, pb in zip(pdA, pdB):
        e += pa * np.log(pb)
    return -e


print(pdA)
print(pdB)
print(entropy(pdA), relative_entropy(pdA, pdB), cross_entropy(pdA, pdB))
