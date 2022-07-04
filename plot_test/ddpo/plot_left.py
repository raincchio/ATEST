import numpy as np
# import matplotlib
# matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
import matplotlib
from util import arrowed_spines

rc_fonts = {
    'xtick.direction': 'in',
    'ytick.direction': 'in',
    'xtick.labelsize':10,
    'ytick.labelsize':10,
    "lines.linewidth":2,
    "font.family": "times",
    'axes.titlesize':10,
    "legend.fontsize":10,
    'figure.figsize': (7.5, 2.5),
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

fig, ax = plt.subplots(1,4)
# color

# black CPI
# #1f77b4 CLIP
# PRE


# fig index 0
index = 0

x = np.arange(0, 2, 0.01)
y = np.arange(0, 2, 0.01)
ax[index].plot(x,y,c='black',alpha=1,zorder=1)

#clip #1f77b4
x = np.arange(0, 1.2, 0.01)
y = np.arange(0, 1.2, 0.01)
ax[index].plot(x,y,'--',c='#1f77b4',)

x = np.arange(1.2, 2, 0.01)
y = np.ones_like(x)*1.2
ax[index].plot(x,y,c='#1f77b4')

#pre #ff7f0e


# point equal
ax[index].scatter(1,1, c='red')


ax[index].set_ylim(0, 2)
ax[index].set_xlim(0, 2)
ax[index].spines['right'].set_color('none')
ax[index].spines['top'].set_color('none')

ax[index].set_xlabel(r'$r$')
ax[index].xaxis.set_label_coords(0.95, -0.02)
ax[index].set_ylabel(r'$J$', rotation=0)
ax[index].yaxis.set_label_coords(0.14, 0.95)

ax[index].tick_params(axis="x")
ax[index].tick_params(axis="y")

ax[index].set_xticks([0, 1, 1.3])
ax[index].set_xticklabels([0,r'$1$',r'$1+\epsilon$'])
ax[index].set_yticks([1])

ax[index].text(1.3, 1.1, r'$A>0$')

# fig index 2
index = 2
x = np.arange(0, 1.3, 0.01)
y = np.ones_like(x)

ax[index].plot(x,y,'--',c='#1f77b4',zorder=2,alpha=0.6)
ax[index].plot([1.3]*100,np.arange(0, 1, 0.01),'--',c='#1f77b4',zorder=2)
ax[index].plot(np.arange(1.3,3.1, 0.01),[0]*180,'--',c='#1f77b4',zorder=2)
ax[index].plot(np.arange(0,3.1, 0.01),[1]*310,'-.',c='black',alpha=1,zorder=1)
x = np.arange(0, end, 0.001)
g = gradient(x)

ax[index].scatter(1,1, c='red')
ax[index].plot(x,g, c='#ff7f0e')

ax[index].set_ylim(0, 1.1)
ax[index].set_xlim(0, 3.1)
ax[index].spines['right'].set_color('none')
ax[index].spines['top'].set_color('none')

ax[index].set_xlabel(r'$r$')
ax[index].xaxis.set_label_coords(0.95, -0.02)
ax[index].set_ylabel(r'$\nabla_{r}  \; J$', rotation=0)
ax[index].yaxis.set_label_coords(0.14, 0.95)

ax[index].tick_params(axis="x")
ax[index].tick_params(axis="y")

ax[index].set_xticks([0, 1, 1.3])
ax[index].set_xticklabels([0,r'$1$',r'$1+\epsilon$'])
ax[index].set_yticks([1])

ax[index].text(1.3, 1.1, r'$A>0$')

# fig index 2
index = 2
x = np.arange(0, 1.3, 0.01)
y = np.ones_like(x)

ax[index].plot(x,y,'--',c='#1f77b4',zorder=2,alpha=0.6)
ax[index].plot([1.3]*100,np.arange(0, 1, 0.01),'--',c='#1f77b4',zorder=2)
ax[index].plot(np.arange(1.3,3.1, 0.01),[0]*180,'--',c='#1f77b4',zorder=2)
ax[index].plot(np.arange(0,3.1, 0.01),[1]*310,'-.',c='black',alpha=1,zorder=1)
x = np.arange(0, end, 0.001)
g = gradient(x)

ax[index].scatter(1,1, c='red')
ax[index].plot(x,g, c='#ff7f0e')

ax[index].set_ylim(0, 1.1)
ax[index].set_xlim(0, 3.1)
ax[index].spines['right'].set_color('none')
ax[index].spines['top'].set_color('none')

ax[index].set_xlabel(r'$r$')
ax[index].xaxis.set_label_coords(0.95, -0.02)
ax[index].set_ylabel(r'$\nabla_{r}  \; J$', rotation=0)
ax[index].yaxis.set_label_coords(0.14, 0.95)

ax[index].tick_params(axis="x")
ax[index].tick_params(axis="y")

ax[index].set_xticks([0, 1, 1.3])
ax[index].set_xticklabels([0,r'$1$',r'$1+\epsilon$'])
ax[index].set_yticks([1])

ax[index].text(1.3, 1.1, r'$A>0$')


# fig index 2
index = 2
x = np.arange(0, 1.3, 0.01)
y = np.ones_like(x)

ax[index].plot(x,y,'--',c='#1f77b4',zorder=2,alpha=0.6)
ax[index].plot([1.3]*100,np.arange(0, 1, 0.01),'--',c='#1f77b4',zorder=2)
ax[index].plot(np.arange(1.3,3.1, 0.01),[0]*180,'--',c='#1f77b4',zorder=2)
ax[index].plot(np.arange(0,3.1, 0.01),[1]*310,'-.',c='black',alpha=1,zorder=1)
x = np.arange(0, end, 0.001)
g = gradient(x)

ax[index].scatter(1,1, c='red')
ax[index].plot(x,g, c='#ff7f0e')

ax[index].set_ylim(0, 1.1)
ax[index].set_xlim(0, 3.1)
ax[index].spines['right'].set_color('none')
ax[index].spines['top'].set_color('none')

ax[index].set_xlabel(r'$r$')
ax[index].xaxis.set_label_coords(0.95, -0.02)
ax[index].set_ylabel(r'$\nabla_{r}  \; J$', rotation=0)
ax[index].yaxis.set_label_coords(0.14, 0.95)

ax[index].tick_params(axis="x")
ax[index].tick_params(axis="y")

ax[index].set_xticks([0, 1, 1.3])
ax[index].set_xticklabels([0,r'$1$',r'$1+\epsilon$'])
ax[index].set_yticks([1])

ax[index].text(1.3, 1.1, r'$A>0$')

# fig.legend(loc='lower center',bbox_to_anchor=(0.5,-0.14), edgecolor='None', facecolor='None',ncol=2)
# fig.legend()
# plt.savefig('gradient.pdf')
plt.show(bbox_inches='tight')
#