import numpy as np
# import matplotlib
# matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
import matplotlib

rc_fonts = {
    'xtick.direction': 'in',
    'ytick.direction': 'in',
    'xtick.labelsize':8,
    'ytick.labelsize':8,
    "lines.linewidth":1.5,
    "font.family": "times",
    # "font.size": 11,
    'axes.titlesize':10,
    "legend.fontsize":10,
    'figure.figsize': (8.5, 2.5),
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

from util import arrowed_spines
def sigmoid(x):
    return 1/(1+ np.exp(-x))

def gradient(x):
    return 4*sigmoid(2*x - 2)*(1-sigmoid(2*x -2))

def operator(x):
    return 2*sigmoid(2*x -2)



fig, axs = plt.subplots(1,2)
fig.subplots_adjust(wspace=0.7, left=0.15, right=0.85)


x = np.arange(0, 2.5, 0.01)
g = operator(x)

axs[0].plot(x, g,c='#ff7f0e',label='P3O')
# axs[0].plot(x, x, linestyle='--',c='#1f77b4')
axs[0].plot(x, x, linestyle='--',c='black')

x = np.arange(0, 1.2, 0.01)
axs[0].plot(x, x, linestyle='-.',c='#1f77b4',label="PPO")
x = np.arange(1.2, 2.5 ,0.01)
axs[0].plot(x, [1.2]*130, linestyle='-.',c='#1f77b4')


axs[0].scatter(1,1, c='red')
axs[0].arrow(0.5,1 ,0.25, 0,width=0.025, length_includes_head=True, fc='black', ec='black')
axs[0].arrow(1.5,1 ,-0.25, 0,width=0.025, length_includes_head=True, fc='black', ec='black')
axs[0].set_ylim(0, 2.5)
axs[0].set_xlim(0, 2.5)
axs[0].spines['right'].set_color('none')
axs[0].spines['top'].set_color('none')

axs[0].set_xlabel(r'$r$')
axs[0].xaxis.set_label_coords(0.95, -0.02)
axs[0].set_ylabel(r'$J$', rotation=0)
axs[0].yaxis.set_label_coords(0.07, 0.95)
# legend= axs[0].legend(loc='upper right', edgecolor='None', facecolor='None')


axs[0].tick_params(axis="x")
axs[0].tick_params(axis="y")
arrowed_spines(axs[0], locations=('bottom right', 'left up'))
# Todo


axs[1].xaxis.tick_top()

x = np.arange(0, 2.5, 0.01)
g = operator(x) * -1
axs[1].plot(x, g,c='#ff7f0e')
axs[1].plot(x, -x, linestyle='-.',c='black')
axs[1].scatter(1,-1, c='red')
axs[1].arrow(0.5,-1 ,0.25, 0,width=0.025, length_includes_head=True, fc='black', ec='black')
axs[1].arrow(1.5,-1 ,-0.25, 0,width=0.025, length_includes_head=True, fc='black', ec='black')

# x = np.arange(0, 1.2, 0.01)
# axs[1].plot(x, -x, linestyle='-.',c='#1f77b4')
# x = np.arange(1.2, 2.5 ,0.01)
# axs[1].plot(x, [-1.2]*130, linestyle='-.',c='#1f77b4')

x = np.arange(0, 0.8, 0.01)
axs[1].plot(x, [-0.8]*80, linestyle='--',c='#1f77b4')
x = np.arange(1.2, 2.5 ,0.01)
axs[1].plot(x, -x, linestyle='--',c='#1f77b4')




axs[1].set_ylim(0, -2.5)
axs[1].set_xlim(0, 2.5)
axs[1].set_xticks([0, 1])

axs[1].set_yticks([-1])
axs[0].set_xticks([0, 1,])

axs[0].set_yticks([1])
axs[1].spines['right'].set_color('none')
axs[1].spines['bottom'].set_color('none')
#
axs[1].set_xlabel(r'$r$')
axs[1].xaxis.set_label_coords(0.95, 1.1)
axs[1].set_ylabel(r'$J$', rotation=0)
axs[1].yaxis.set_label_coords(0.04, 0.02)

axs[1].text(1.3, .2, r'$A<0$')
axs[0].text(1.3, 2.5, r'$A>0$')
axs[1].tick_params(axis="x")
axs[1].tick_params(axis="y")
arrowed_spines(axs[1],xiangxian=4, locations=('top right', 'left down'))
axs[1].invert_yaxis()
pos1 = axs[1].get_position() # get the original position
pos2 = [pos1.x0, pos1.y0 - 0.048,  pos1.width, pos1.height]
axs[1].set_position(pos2)


axs[0].vlines(0.8, 0.5,1.5, colors='r', linestyles='dotted',)
axs[0].vlines(1.2, 0.5,1.5, colors='r',linestyles='dotted')
axs[1].vlines(0.8, -0.5,-1.5, colors='r',linestyles='dotted')
axs[1].vlines(1.2, -0.5,-1.5, colors='r',linestyles='dotted')

fig.legend(loc='center', edgecolor='None', facecolor='None',ncol=1)
plt.savefig('sigmoid.pdf')
# plt.show()
