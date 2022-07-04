import numpy as np
# import matplotlib
# matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
import matplotlib
from util import arrowed_spines

rc_fonts = {
    'xtick.direction': 'in',
    'ytick.direction': 'in',
    'xtick.labelsize':8,
    'ytick.labelsize':8,
    "lines.linewidth":1.2,
    "font.family": "times",
    # "font.size": 11,
    'axes.titlesize':8,
    "legend.fontsize":8,
    'figure.figsize': (3, 2.5),
    # 'figure.figsize': (5, 5/2.0*0.75),
    # "text.usetex": True,
    # 'text.latex.preview': True,
    # 'text.latex.preamble':
    #     r"""
    #     \usepackage{times}
    #     \usepackage{helvet}
    #     \usepackage{courier}
    #     """,
}
matplotlib.rcParams.update(rc_fonts)




def sigmoid(x):
    return 1/(1+ np.exp(-x))

def gradient(x):
    return 4*sigmoid(2*x - 2)*(1-sigmoid(2*x -2))

def operator(x):
    return 2*sigmoid(2*x -2)

begin=0
end = 3

fig, ax = plt.subplots()

ax.xaxis.tick_top()

plt.plot(np.arange(0,3.1, 0.01),[-1]*310,'-.',c='black',zorder=1)
x = np.arange(0, end, 0.01)
g = gradient(x) * -1

# l2 = plt.plot(x,g, c='#ff7f0e', label='sigmoid preconditioning function')
# plt.scatter(1,-1, c='red')


x = np.arange(0.7, 3, 0.01)
y = np.ones_like(x) * -1

l1 = plt.plot(x,y,'--', label="CLIP",zorder=2)
plt.plot([0.7]*100,np.arange(-1, 0, 0.01),'--',c='#1f77b4',zorder=2)
plt.plot(np.arange(0,0.7, 0.01),[0]*70,'--',c='#1f77b4',zorder=2)

ax.set_ylim(0, -1.1)
ax.set_xlim(0, 3.1)
ax.set_xticks([0,0.7, 1])
ax.set_xticklabels([0,r'$1-\epsilon$',r'$1$'])
ax.set_yticks([-1])

ax.spines['right'].set_color('none')
ax.spines['bottom'].set_color('none')


ax.set_xlabel(r'$r$')
ax.xaxis.set_label_coords(0.95, 1.1)
ax.set_ylabel(r'$\nabla_{r} \; J$', rotation=0)
ax.yaxis.set_label_coords(0.17, -0.07)

ax.text(1.3, .07, r'$A<0$')
ax.tick_params(axis="x")
ax.tick_params(axis="y")


ax.invert_yaxis()

for direction in ["xzero", "yzero"]:
    ax.xaxis.set_axisline_style("-|>")
    ax.xaxis.set_visible(True)


fig.legend(edgecolor='None', facecolor='None',loc='center right')
# plt.savefig('gradient.pdf')
plt.show(bbox_inches='tight')
#