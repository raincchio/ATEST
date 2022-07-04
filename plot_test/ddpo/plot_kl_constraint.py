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
    'axes.titlesize':11,
    # "font.size": 16,
    # 'axes.titlesize':16,
    "legend.fontsize":8,
    # 'figure.figsize': (12, 12/3.0*0.75),
    # 'figure.figsize': (5, 5/2.0*0.75),
    "text.usetex": True,
    # 'text.latex.preview': True,
    'text.latex.preamble':
        r"""
        \usepackage{times}
        \usepackage{helvet}
        \usepackage{courier}
        """,
}
matplotlib.rcParams.update(rc_fonts)

from util import arrowed_spines
def sigmoid(x):
    return 1/(1+ np.exp(-x))

def gradient(x):
    return 4*sigmoid(2*x - 2)*(1-sigmoid(2*x -2))

def operator(x):
    return 2*sigmoid(2*x -2)



# plt.subplots(1,2, figsize=(12,6))
# plt.subplot(1,2,1)

fig = plt.figure(figsize=(4.5,1.8))
axs = fig.subplot_mosaic([['bar1','bar2']])


x = np.arange(0, 2.5, 0.01)
g = operator(x)

axs['bar1'].plot(x, g,c='#ff7f0e',label='sigmoid preconditioning function')
# axs['bar1'].plot(x, x, linestyle='--',c='#1f77b4')
axs['bar1'].plot(x, x, linestyle='--',c='black')

x = np.arange(0, 1.2, 0.01)
axs['bar1'].plot(x, x, linestyle='-.',c='#1f77b4',label="PPO's min+clipping")
x = np.arange(1.2, 2.5 ,0.01)
axs['bar1'].plot(x, [1.2]*130, linestyle='-.',c='#1f77b4')


axs['bar1'].scatter(1,1, c='red')
axs['bar1'].arrow(0.5,1 ,0.25, 0,width=0.025, length_includes_head=True, fc='black', ec='black')
axs['bar1'].arrow(1.5,1 ,-0.25, 0,width=0.025, length_includes_head=True, fc='black', ec='black')
axs['bar1'].set_ylim(0, 2.5)
axs['bar1'].set_xlim(0, 2.5)
axs['bar1'].spines['right'].set_color('none')
axs['bar1'].spines['top'].set_color('none')

axs['bar1'].set_xlabel(r'$r$')
axs['bar1'].xaxis.set_label_coords(0.95, -0.02)
axs['bar1'].set_ylabel(r'$J$', rotation=0)
axs['bar1'].yaxis.set_label_coords(0.07, 0.95)
# legend= axs['bar1'].legend(loc='upper right', edgecolor='None', facecolor='None')


axs['bar1'].tick_params(axis="x")
axs['bar1'].tick_params(axis="y")
arrowed_spines(axs['bar1'], locations=('bottom right', 'left up'))
# Todo


axs['bar2'].xaxis.tick_top()

x = np.arange(0, 2.5, 0.01)
g = operator(x) * -1
axs['bar2'].plot(x, g,c='#ff7f0e')
axs['bar2'].plot(x, -x, linestyle='-.',c='black')
axs['bar2'].scatter(1,-1, c='red')
axs['bar2'].arrow(0.5,-1 ,0.25, 0,width=0.025, length_includes_head=True, fc='black', ec='black')
axs['bar2'].arrow(1.5,-1 ,-0.25, 0,width=0.025, length_includes_head=True, fc='black', ec='black')

# x = np.arange(0, 1.2, 0.01)
# axs['bar2'].plot(x, -x, linestyle='-.',c='#1f77b4')
# x = np.arange(1.2, 2.5 ,0.01)
# axs['bar2'].plot(x, [-1.2]*130, linestyle='-.',c='#1f77b4')

x = np.arange(0, 0.8, 0.01)
axs['bar2'].plot(x, [-0.8]*80, linestyle='--',c='#1f77b4')
x = np.arange(1.2, 2.5 ,0.01)
axs['bar2'].plot(x, -x, linestyle='--',c='#1f77b4')




axs['bar2'].set_ylim(0, -2.5)
axs['bar2'].set_xlim(0, 2.5)
axs['bar2'].set_xticks([0, 1])

axs['bar2'].set_yticks([-1])
axs['bar1'].set_xticks([0, 1,])

axs['bar1'].set_yticks([1])
axs['bar2'].spines['right'].set_color('none')
axs['bar2'].spines['bottom'].set_color('none')
#
axs['bar2'].set_xlabel(r'$r$')
axs['bar2'].xaxis.set_label_coords(0.95, 1.1)
axs['bar2'].set_ylabel(r'$J$', rotation=0)
axs['bar2'].yaxis.set_label_coords(0.04, 0.02)

axs['bar2'].text(1.3, .2, r'$A<0$')
axs['bar1'].text(1.3, 2.5, r'$A>0$')
axs['bar2'].tick_params(axis="x")
axs['bar2'].tick_params(axis="y")
arrowed_spines(axs['bar2'],xiangxian=4, locations=('top right', 'left down'))
axs['bar2'].invert_yaxis()
pos1 = axs['bar2'].get_position() # get the original position
pos2 = [pos1.x0, pos1.y0 - 0.048,  pos1.width, pos1.height]
axs['bar2'].set_position(pos2)


axs['bar1'].vlines(0.8, 0.5,1.5, colors='r', linestyles='dotted',)
axs['bar1'].vlines(1.2, 0.5,1.5, colors='r',linestyles='dotted')
axs['bar2'].vlines(0.8, -0.5,-1.5, colors='r',linestyles='dotted')
axs['bar2'].vlines(1.2, -0.5,-1.5, colors='r',linestyles='dotted')

fig.legend(loc='lower center',bbox_to_anchor=(0.5,-0.14), edgecolor='None', facecolor='None',ncol=2)
plt.savefig('sigmoid.pdf',bbox_inches='tight')
# plt.show()
