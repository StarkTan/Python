# -*- coding: utf-8 -*-
"""
Neural Networks 神经网络
网络神经步骤：
1.定义一个包含可训练参数的神经网络
2.迭代整个输入
3.通过神经网络处理输入
4.计算损失(loss)
5.反向传播梯度到神经网络的参数
6.更新网络的参数，典型的用一个简单的更新方法：weight = weight - learning_rate *gradient
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

# 定义神经网络
class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        # 1 input image channel, 6 output channels, 5x5 square convolution
        # kernel
        self.conv1 = nn.Conv2d(1, 6, 5)
        self.conv2 = nn.Conv2d(6, 16, 5)
        # an affine operation: y = Wx + b
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        # Max pooling over a (2, 2) window
        x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))
        # If the size is a square you can only specify a single number
        x = F.max_pool2d(F.relu(self.conv2(x)), 2)
        x = x.view(-1, self.num_flat_features(x))
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

    def num_flat_features(self, x):
        size = x.size()[1:]  # all dimensions except the batch dimension
        num_features = 1
        for s in size:
            num_features *= s
        return num_features


net = Net()
print(net)
# 一个模型可训练的参数可以通过调用 net.parameters() 返回
params = list(net.parameters())
print(len(params))
print(params[0].size())  # conv1's .weight
# 尝试随机生成一个 32x32 的输入
input = torch.randn(1, 1, 32, 32)
out = net(input)
print(out)
# 把所有参数梯度缓存器置零，用随机的梯度来反向传播
net.zero_grad()
out.backward(torch.randn(1, 10))

# 计算损失值
output = net(input)
target = torch.randn(10)  # a dummy target, for example
target = target.view(1, -1)  # make it the same shape as output
criterion = nn.MSELoss()
loss = criterion(output, target)
print(loss)

print(loss.grad_fn)  # MSELoss
print(loss.grad_fn.next_functions[0][0])  # Linear
print(loss.grad_fn.next_functions[0][0].next_functions[0][0])  # ReLU
net.zero_grad()     # zeroes the gradient buffers of all parameters
print('conv1.bias.grad before backward')
print(net.conv1.bias.grad)
loss.backward()
print('conv1.bias.grad after backward')
print(net.conv1.bias.grad)


# 更新神经网络参数
optimizer = optim.SGD(net.parameters(), lr=0.01)

optimizer.zero_grad()   # zero the gradient buffers
output = net(input)
loss = criterion(output, target)
loss.backward()
optimizer.step()    # Does the update
