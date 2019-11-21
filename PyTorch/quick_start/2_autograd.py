"""
自动微分
"""
import torch

x = torch.ones(2, 2, requires_grad=True)  # 创建一个张量，配置跟踪与它相关的计算
print(x)
y = x + 2  # 针对张量做一个操作
print(y)
print(y.grad_fn)  # 被记录的操作

z = y * y * 3  # 针对y做更多的操作
out = z.mean()
print(z, out)

out.backward()  # 向后传播，用于寻找梯度
print(x.grad)   # 获取从x到out的梯度，即最快到达到达向量

#  修改 requires_grad_
a = torch.randn(2, 2)
a = ((a * 3) / (a - 1))
print(a.requires_grad)
a.requires_grad_(True)  # 使用requires_grad_修改记录配置
print(a.requires_grad)
b = (a * a).sum()
print(b.grad_fn)

# 示例：雅可比向量积
x = torch.randn(3, requires_grad=True)
y = x * 2
while y.data.norm() < 1000:
    y = y * 2
print(y)
v = torch.tensor([0.1, 1.0, 0.0001], dtype=torch.float)
y.backward(v)
print(x.grad)

print(x.requires_grad)
print((x ** 2).requires_grad)

with torch.no_grad():
    print((x ** 2).requires_grad)