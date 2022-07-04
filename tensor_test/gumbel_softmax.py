import torch as th
# todo gumbel softmax with mask
#
#
# mask = th.FloatTensor([[1,1,1,1,0]])
logits = th.randn(1, 5)
# ea = th.exp(logits) * mask
ea = th.exp(logits)
soft = ea/th.sum(ea, dim=-1, keepdim=True)
print(soft)
#
# num = 10000
# sum1 = th.zeros_like(logits)
# for i in range(num):
#     # gb = th.nn.functional.gumbel_softmax(logits)
#     u = th.rand_like(logits)
#     gumbel = logits-(-u.log()).log()
#     ea = th.exp(gumbel) * mask+ 1e-10
#     y_soft = ea/th.sum(ea, dim=-1, keepdim=True)
#
#     index = y_soft.max(-1, keepdim=True)[1]
#     y_hard = th.zeros_like(logits).scatter_(-1, index, 1.0)
#     # ret = y_hard - y_soft.detach() + y_soft
#
#     sum1 += y_hard
# print(sum1/num)


num = 10000
sum1 = th.zeros_like(logits)
for i in range(num):
    # gb = th.nn.functional.gumbel_softmax(logits)
    u = th.rand_like(logits)
    gumbel = logits-(-u.log()).log()
    ea = th.exp(gumbel) * mask+ 1e-10
    y_soft = ea/th.sum(ea, dim=-1, keepdim=True)

    index = y_soft.max(-1, keepdim=True)[1]
    y_hard = th.zeros_like(logits).scatter_(-1, index, 1.0)
    # ret = y_hard - y_soft.detach() + y_soft

    sum1 += y_hard
print(sum1/num)