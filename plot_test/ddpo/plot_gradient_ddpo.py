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


# plt.subplots(1,2, figsize=(12,6))
# plt.subplot(1,2,1)

fig = plt.figure(figsize=(4.5,1.8))
axs = fig.subplot_mosaic([['bar1','bar2']])


x = np.arange(0, 1.3, 0.01)
y = np.ones_like(x)
# axs['bar1'].fill_between(x, y, hatch='\\\\\\',facecolor="None",  edgecolor="b", linewidth=0.0, label='PPO')
axs['bar1'].plot(x,y,'--',c='#1f77b4',zorder=2,alpha=0.6)
axs['bar1'].plot([1.3]*100,np.arange(0, 1, 0.01),'--',c='#1f77b4',zorder=2)
axs['bar1'].plot(np.arange(1.3,3.1, 0.01),[0]*180,'--',c='#1f77b4',zorder=2)
axs['bar1'].plot(np.arange(0,3.1, 0.01),[1]*310,'-.',c='black',alpha=1,zorder=1)
x = np.arange(0, end, 0.001)
g = gradient(x)
# axs['bar1'].fill_between(x, g, hatch="///", fc="None", edgecolor="orange", linewidth=0.0, label='STPG')
axs['bar1'].scatter(1,1, c='red')
axs['bar1'].plot(x,g, c='#ff7f0e')

axs['bar1'].set_ylim(0, 1.1)
axs['bar1'].set_xlim(0, 3.1)
axs['bar1'].spines['right'].set_color('none')
axs['bar1'].spines['top'].set_color('none')

annots = arrowed_spines(axs['bar1'], locations=('bottom right', 'left up'))

axs['bar1'].set_xlabel(r'$r$')
axs['bar1'].xaxis.set_label_coords(0.95, -0.02)
axs['bar1'].set_ylabel(r'$\nabla_{r}  \; J$', rotation=0)
axs['bar1'].yaxis.set_label_coords(0.14, 0.95)

axs['bar1'].tick_params(axis="x")
axs['bar1'].tick_params(axis="y")

# Todo


axs['bar2'].xaxis.tick_top()



axs['bar2'].plot(np.arange(0,3.1, 0.01),[-1]*310,'-.',c='black',zorder=1)
x = np.arange(0, end, 0.01)
g = gradient(x) * -1
# axs['bar2'].fill_between(x, g, hatch="///", fc="None", edgecolor="orange", linewidth=0.0, label='STPG')
l2 = axs['bar2'].plot(x,g, c='#ff7f0e', label='sigmoid preconditioning function')
axs['bar2'].scatter(1,-1, c='red')


x = np.arange(0.7, 3, 0.01)
y = np.ones_like(x) * -1
# axs['bar2'].fill_between(x, y, hatch='\\\\\\',facecolor="None",  edgecolor="b", linewidth=0.0, label='PPO')
l1 = axs['bar2'].plot(x,y,'--', label="PPO's min+clipping",zorder=2)
axs['bar2'].plot([0.7]*100,np.arange(-1, 0, 0.01),'--',c='#1f77b4',zorder=2)
axs['bar2'].plot(np.arange(0,0.7, 0.01),[0]*70,'--',c='#1f77b4',zorder=2)



axs['bar2'].set_ylim(0, -1.1)
axs['bar2'].set_xlim(0, 3.1)
axs['bar2'].set_xticks([0,0.7, 1])
axs['bar2'].set_xticklabels([0,r'$1-\epsilon$',r'$1$'])
axs['bar2'].set_yticks([-1])
axs['bar1'].set_xticks([0, 1, 1.3])
axs['bar1'].set_xticklabels([0,r'$1$',r'$1+\epsilon$'])
axs['bar1'].set_yticks([1])
axs['bar2'].spines['right'].set_color('none')
axs['bar2'].spines['bottom'].set_color('none')
# 0.0 -1.1 0 1.1 0.8 0.0693 -0.04428571428571429
arrowed_spines(axs['bar2'],xiangxian=4, locations=('top right', 'left down'))

axs['bar2'].set_xlabel(r'$r$')
axs['bar2'].xaxis.set_label_coords(0.95, 1.1)
axs['bar2'].set_ylabel(r'$\nabla_{r} \; J$', rotation=0)
axs['bar2'].yaxis.set_label_coords(0.17, -0.07)

axs['bar2'].text(1.3, .07, r'$A<0$')
axs['bar1'].text(1.3, 1.1, r'$A>0$')
axs['bar2'].tick_params(axis="x")
axs['bar2'].tick_params(axis="y")

# axs['bar2'].set_xlabel(r'$1-\epsilon$', fontsize=12)
# axs['bar2'].xaxis.set_label_coords(0.25, 0.98)
#
# axs['bar1'].set_xlabel(r'$1+\epsilon$', fontsize=12)
# axs['bar1'].xaxis.set_label_coords(0.4, -0.02)

axs['bar2'].invert_yaxis()
pos1 = axs['bar2'].get_position() # get the original position
pos2 = [pos1.x0, pos1.y0 - 0.048,  pos1.width, pos1.height]
axs['bar2'].set_position(pos2)
fig.legend(loc='lower center',bbox_to_anchor=(0.5,-0.14), edgecolor='None', facecolor='None',ncol=2)
# plt.savefig('gradient.pdf')
plt.show(bbox_inches='tight')
#