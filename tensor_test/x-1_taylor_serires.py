def gx():
    x = 0.1
    while x<=1:
        x += 0.1
        yield x

def x_1_t_s(x):
    return x -1 - (x-1)**2/2

for x in gx():
    print(x, x_1_t_s(x))
