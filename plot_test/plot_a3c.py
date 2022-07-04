import os
path = 'plot/a3c'
files = [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
datas = []
for file in files:
    with open(file, 'r') as f:
        datas.append(f.read())

import matplotlib.pyplot as pt

for data, file in zip(datas, files):
    returns = [float(e.split(',')[3][16:]) for e in data.split('\n')]
    pt.plot(returns, label=file[5:])
pt.legend()
pt.show()