import torch
x=torch.Tensor([[1.,2.,3.],[4.,5.,6.]])
x.requires_grad_(True)
y=x+2
z=y*3
out=z.mean()
out.backward()
print(y.grad)