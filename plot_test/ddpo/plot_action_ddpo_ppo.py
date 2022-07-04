with open(r'C:\Users\chenxing\0323\result_compare\runP3OqueryPPO\p3o_log','r') as f:
    log = eval(f.read())

with open(r'C:\Users\chenxing\0323\result_compare\runP3OqueryPPO\ppo_log','r') as f:
    log2 = eval(f.read())

from matplotlib import pyplot as plt
import numpy as np
res1 = []
for item in log:
    res1.append(item[1])
b = np.array(res1).squeeze(1)

res1 = []
for item in log2:
    res1.append(item[1])
a = np.array(res1).squeeze(1)



fig, axs = plt.subplots(2,3,figsize=(18,10))

fig.suptitle('run P3O, query PPO - minus mean (20 episode)',fontsize=16)

# fig.supxlabel('Episode Length')
# fig.supylabel('Action Value')


axs[0][0].set_title('bthigh')
axs[0][0].plot(b[:,0]- b[:,0].mean(), label='P3O')
axs[0][0].plot(a[:,0] - a[:,0].mean(), label='PPO')

axs[0][1].set_title('bshin')
axs[0][1].plot(b[:,1]- b[:,1].mean())
axs[0][1].plot(a[:,1]- a[:,1].mean())

axs[0][2].set_title('bfoot')
axs[0][2].plot(b[:,2]- b[:,2].mean())
axs[0][2].plot(a[:,2]- a[:,2].mean())

axs[1][0].set_title('fthigh')
axs[1][0].plot(b[:,3]- b[:,3].mean())
axs[1][0].plot(a[:,3]- a[:,3].mean())

axs[1][1].set_title('fshin')
axs[1][1].plot(b[:,4]- b[:,4].mean())
axs[1][1].plot(a[:,4]- a[:,4].mean())

axs[1][2].set_title('ffoot')
axs[1][2].plot(b[:,5]- b[:,5].mean())
axs[1][2].plot(a[:,5]- a[:,5].mean())

# handles, labels = plt.gca().get_legend_handles_labels()
# fig.legend(handles, labels, loc='upper center')
fig.legend(loc='lower center', edgecolor='None', facecolor='None',ncol=2, fontsize=16)
plt.savefig('run P3O and query PPO-minus mean')