"""
张量 类似numpy
"""
import torch
x = torch.empty(5, 3)  # 构建5*3的未初始化矩阵
print(x)
x = torch.rand(5, 3)   # 构建5*3的随机[0-1]初始化矩阵
print(x)
x = torch.zeros(5, 3, dtype=torch.long)  # 构建5*3全为0的矩阵，数据类型为long
print(x)
x = x.new_ones(5, 3, dtype=torch.double)
print(x)
x = torch.randn_like(x, dtype=torch.float)  # 使用矩阵构建一个类似的随机矩阵
print(x)
print(x.size())  # 数据为元组

# 加法操作
y = x.new_ones(5, 3, dtype=torch.double)
print(x+y)
print(torch.add(x, y))
z = torch.empty(5, 3)
torch.add(x, y, out=z)
print(z)
y.add_(x)
print(y)

# 索引操作
print(x[:, 1])

# 矩阵形状改变
x = torch.randn(4, 4)
y = x.view(16)
z = x.view(-1, 8)  # the size -1 is inferred from other dimensions
print(x.size(), y.size(), z.size())

# 获取单个元素的值
x = torch.randn(1)
print(x)
print(x.item())
