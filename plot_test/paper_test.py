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




def sigmoid(x):
    return 1/(1+ np.exp(-x))

def gradient(x):
    return 4*sigmoid(2*x - 2)*(1-sigmoid(2*x -2))

def operator(x):
    return 2*sigmoid(2*x -2)

begin=0
end = 3


fig, axs = plt.subplots(1,2)
fig.subplots_adjust(wspace=0.7, left=0.15, right=0.85)


axs[1].plot(np.arange(0,3.1, 0.01),[1]*310,'-.',c='black',alpha=1,zorder=1,label='CPI')

x = np.arange(0, 1.3, 0.01)
y = np.ones_like(x)

axs[1].plot(x,y,'--',c='#1f77b4',zorder=2,alpha=0.6)
axs[1].plot([1.3]*100,np.arange(0, 1, 0.01),'--',c='#1f77b4',zorder=2)
axs[1].plot(np.arange(1.3,3.1, 0.01),[0]*180,'--',c='#1f77b4',zorder=2,label='PPO objective')

x = np.arange(0, end, 0.001)
g = gradient(x)
axs[1].plot(x,g, c='#ff7f0e',label='Scopic')

axs[1].scatter(1,1, c='red')

axs[1].set_ylim(0, 1.1)
axs[1].set_xlim(0, 3.1)
axs[1].spines['right'].set_color('none')
axs[1].spines['top'].set_color('none')

annots = arrowed_spines(axs[1], locations=('bottom right', 'left up'))

axs[1].set_xlabel(r'$r$')
axs[1].xaxis.set_label_coords(0.95, -0.02)
axs[1].set_ylabel(r'$\nabla_{r}  \; L$', rotation=0)
axs[1].yaxis.set_label_coords(0.14, 0.95)

axs[1].tick_params(axis="x")
axs[1].tick_params(axis="y")


axs[1].set_xticks([1, 1.3])
axs[1].set_xticklabels([r'$1$',r'$1+\epsilon$'])
axs[1].set_yticks([1])
axs[1].set_yticklabels([r'$\hat{A}$'])
# axs[0].text(1.3, 1.1, r'$A>0$')

# Todo

x = np.arange(0, 2.2, 0.001)
axs[0].plot(x, x, linestyle='-.',c='black')

x = np.arange(0, 1.3, 0.01)
axs[0].plot(x, x, linestyle='--',c='#1f77b4')
x = np.arange(1.3, 2.2 ,0.01)
axs[0].plot(x, [1.3]*91, linestyle='--',c='#1f77b4')

x = np.arange(0, 2.2, 0.01)
g = operator(x)
axs[0].plot(x, g,c='#ff7f0e')



axs[0].scatter(1,1, c='red')

# axs[0].arrow(0.5, 1, 0.25, 0,width=0.01, length_includes_head=True, fc='black', ec='black')
# axs[0].arrow(1.5, 1, -0.25, 0,width=0.01, length_includes_head=True, fc='black', ec='black')

axs[0].set_ylim(0, 2.3)
axs[0].set_xlim(0, 2.3)
axs[0].spines['right'].set_color('none')
axs[0].spines['top'].set_color('none')

axs[0].set_xlabel(r'$r$')
axs[0].xaxis.set_label_coords(0.95, -0.025)
axs[0].set_ylabel(r'$L$', rotation=0)
axs[0].yaxis.set_label_coords(0.07, 0.95)

axs[0].set_yticks([1])
axs[0].set_yticklabels([r'$\hat{A}$'])
axs[0].set_xticks([1, 1.3])
axs[0].set_xticklabels([r'$1$',r'$1+\epsilon$'])

# axs[1].tick_params(axis="x")
# axs[1].tick_params(axis="y")
arrowed_spines(axs[0], locations=('bottom right', 'left up'))


fig.legend(loc='center', edgecolor='None', facecolor='None',ncol=1)
plt.savefig('gradient.pdf')
# plt.show()