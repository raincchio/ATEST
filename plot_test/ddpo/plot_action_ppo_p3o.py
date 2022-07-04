with open(r'C:\Users\chenxing\0323\result_compare\runPPOqueryP3O\p3o_log','r') as f:
    log = eval(f.read())

with open(r'C:\Users\chenxing\0323\result_compare\runPPOqueryP3O\ppo_log','r') as f:
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


plt.figure()
fig, axs = plt.subplots(2,3,figsize=(18,10))

fig.suptitle('run PPO and query P3O',fontsize=16)

# fig.supxlabel('Episode Length')
# fig.supylabel('Action Value')


axs[0][0].set_title('bthigh')
axs[0][0].plot(b[:,0], label='P3O')
axs[0][0].plot(a[:,0], label='PPO')

axs[0][1].set_title('bshin')
axs[0][1].plot(b[:,1])
axs[0][1].plot(a[:,1])

axs[0][2].set_title('bfoot')
axs[0][2].plot(b[:,2])
axs[0][2].plot(a[:,2])

axs[1][0].set_title('fthigh')
axs[1][0].plot(b[:,3])
axs[1][0].plot(a[:,3])

axs[1][1].set_title('fshin')
axs[1][1].plot(b[:,4])
axs[1][1].plot(a[:,4])

axs[1][2].set_title('ffoot')
axs[1][2].plot(b[:,5])
axs[1][2].plot(a[:,5])

# handles, labels = plt.gca().get_legend_handles_labels()
# fig.legend(handles, labels, loc='upper center')
fig.legend(loc='lower center', edgecolor='None', facecolor='None',ncol=2, fontsize=16)
plt.savefig('run PPO and query P3O')