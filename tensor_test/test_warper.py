def betafn(val):
    def f(frac):
        return val*frac
    return f

beta = 10
beta = betafn(beta)
print(beta(0.1))