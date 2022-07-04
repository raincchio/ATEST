import torch as th
import torch.nn as nn
from torch.nn import init


class Test(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = nn.Linear(4, 3)
        init.constant_(self.fc.weight, 1)
        init.constant_(self.fc.bias, 0)

    def forward(self,input):
            data = self.fc(input)
            return data


data = th.rand(2,4)
data = th.FloatTensor([[1,2,3,4],[5,6,7,8]])
label = th.zeros(2, 3).scatter_(-1, th.LongTensor([[0],[2]]), 1)

model_a = Test()
ahat = model_a(data)
optimize = th.optim.Adam(model_a.parameters(),lr=0.01)

loss = th.nn.MSELoss()(ahat, label)
optimize.zero_grad()
print(model_a.fc.weight.grad, model_a.fc.weight)
loss.backward()
print(model_a.fc.weight.grad, model_a.fc.weight)
optimize.step()
print(model_a.fc.weight.grad, model_a.fc.weight)
# model_b = Test()
#
# for parama, paramb in zip(model_a.parameters(),model_b.parameters()):
#     paramb.data.copy_(th.FloatTensor(parama.tolist()))
# print()