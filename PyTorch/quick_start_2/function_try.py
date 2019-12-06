# coding=utf-8
"""
PyTorch的核心是两个主要特征
    一个n维张量，类似于numpy，但可以在GPU上运行
    搭建和训练神经网络时的自动微分/求导机制
"""


def numpy_use():
    """
    使用numpy 进行前向和后向传递
    """
    import numpy as np
    # N是批量大小; D_in是输入维度;
    # 49/5000 H是隐藏的维度; D_out是输出维度。
    N, D_in, H, D_out = 64, 1000, 100, 10

    # 创建随机输入和输出数据
    x = np.random.randn(N, D_in)
    y = np.random.randn(N, D_out)

    # 随机初始化权重
    w1 = np.random.randn(D_in, H)  # 第一次处理输入值的权重
    w2 = np.random.randn(H, D_out)  # 第二次处理输入值的权重

    learning_rate = 1e-6
    for t in range(500):
        # 前向传递：计算预测值y和误差
        h = x.dot(w1)  # N*H的矩阵
        h_relu = np.maximum(h, 0)  # 将小于0的值换成0
        y_pred = h_relu.dot(w2)  # N*D_out的矩阵

        # 计算和打印损失loss
        loss = np.square(y_pred - y).sum()  # 计算处理后的所有差值平方和
        print(t, loss)  # 目的是为了不断减小lose

        # 反向传播，计算w1和w2对loss的梯度
        grad_y_pred = 2.0 * (y_pred - y)  # N*D_out的矩阵，y的误差
        grad_w2 = h_relu.T.dot(grad_y_pred)  # H*N * N*D_out -->H*D_out矩阵 获取第二次的权重误差
        grad_h_relu = grad_y_pred.dot(w2.T)  # 获取 h_rule的误差
        grad_h = grad_h_relu.copy()
        grad_h[h < 0] = 0
        grad_w1 = x.T.dot(grad_h)  # 获取第一次处理的权重误差

        # 更新权重
        w1 -= learning_rate * grad_w1
        w2 -= learning_rate * grad_w2


def pytorch_use():
    """
    使用pytorch的张量进行前向和后向传递
    """
    import torch
    dtype = torch.float
    device = torch.device("cpu")  # 使用CPU进行计算
    # device = torch.device（“cuda：0”）＃使用GPU进行计算

    # N是批量大小; D_in是输入维度;
    # H是隐藏的维度; D_out是输出维度。
    N, D_in, H, D_out = 64, 1000, 100, 10

    # 创建随机输入和输出数据
    x = torch.randn(N, D_in, device=device, dtype=dtype)
    y = torch.randn(N, D_out, device=device, dtype=dtype)

    # 随机初始化权重
    w1 = torch.randn(D_in, H, device=device, dtype=dtype)
    w2 = torch.randn(H, D_out, device=device, dtype=dtype)

    learning_rate = 1e-6
    for t in range(500):
        # 前向传递：计算预测y
        h = x.mm(w1)
        h_relu = h.clamp(min=0)
        y_pred = h_relu.mm(w2)

        # 计算和打印损失
        loss = (y_pred - y).pow(2).sum().item()
        print(t, loss)

        # Backprop计算w1和w2相对于损耗的梯度
        grad_y_pred = 2.0 * (y_pred - y)
        grad_w2 = h_relu.t().mm(grad_y_pred)
        grad_h_relu = grad_y_pred.mm(w2.t())
        grad_h = grad_h_relu.clone()
        grad_h[h < 0] = 0
        grad_w1 = x.t().mm(grad_h)

        # 使用梯度下降更新权重
        w1 -= learning_rate * grad_w1
        w2 -= learning_rate * grad_w2


def autogrid_use():
    """
    使用 pytorch 的 autogrid 进行
    """
    import torch

    dtype = torch.float
    device = torch.device("cpu")

    # N是批量大小; D_in是输入维度;
    # H是隐藏的维度; D_out是输出维度。
    N, D_in, H, D_out = 64, 1000, 100, 10

    # 创建随机Tensors以保持输入和输出。
    # 设置requires_grad = False表示我们不需要计算渐变
    # 在向后传球期间对于这些Tensors。
    x = torch.randn(N, D_in, device=device, dtype=dtype)
    y = torch.randn(N, D_out, device=device, dtype=dtype)

    # 为权重创建随机Tensors。
    # 设置requires_grad = True表示我们想要计算渐变
    # 在向后传球期间尊重这些张贴。
    w1 = torch.randn(D_in, H, device=device, dtype=dtype, requires_grad=True)
    w2 = torch.randn(H, D_out, device=device, dtype=dtype, requires_grad=True)

    learning_rate = 1e-6
    for t in range(500):
        # 前向传播：使用tensors上的操作计算预测值y;
        # 由于w1和w2有requires_grad=True，涉及这些张量的操作将让PyTorch构建计算图，
        # 从而允许自动计算梯度。由于我们不再手工实现反向传播，所以不需要保留中间值的引用。
        y_pred = x.mm(w1).clamp(min=0).mm(w2)

        # 使用Tensors上的操作计算和打印丢失。
        # loss是一个形状为()的张量
        # loss.item() 得到这个张量对应的python数值
        loss = (y_pred - y).pow(2).sum()
        print(t, loss.item())

        # 使用autograd计算反向传播。这个调用将计算loss对所有requires_grad=True的tensor的梯度。
        # 这次调用后，w1.grad和w2.grad将分别是loss对w1和w2的梯度张量。
        loss.backward()

        # 使用梯度下降更新权重。对于这一步，我们只想对w1和w2的值进行原地改变；不想为更新阶段构建计算图，
        # 所以我们使用torch.no_grad()上下文管理器防止PyTorch为更新构建计算图
        with torch.no_grad():
            w1 -= learning_rate * w1.grad
            w2 -= learning_rate * w2.grad

            # 反向传播后手动将梯度设置为零
            w1.grad.zero_()
            w2.grad.zero_()
    return


def custom_autogrid_use():
    """
    创建使用自己的 自动求导工具
    """
    import torch

    class MyReLU(torch.autograd.Function):
        """
        我们可以通过建立torch.autograd的子类来实现我们自定义的autograd函数，
        并完成张量的正向和反向传播。
        """
        @staticmethod
        def forward(ctx, x):
            """
            在正向传播中，我们接收到一个上下文对象和一个包含输入的张量；
            我们必须返回一个包含输出的张量，
            并且我们可以使用上下文对象来缓存对象，以便在反向传播中使用。
            """
            ctx.save_for_backward(x)
            return x.clamp(min=0)

        @staticmethod
        def backward(ctx, grad_output):
            """
            在反向传播中，我们接收到上下文对象和一个张量，
            其包含了相对于正向传播过程中产生的输出的损失的梯度。
            我们可以从上下文对象中检索缓存的数据，
            并且必须计算并返回与正向传播的输入相关的损失的梯度。
            """
            x, = ctx.saved_tensors
            grad_x = grad_output.clone()
            grad_x[x < 0] = 0
            return grad_x

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    # N是批大小； D_in 是输入维度；
    # H 是隐藏层维度； D_out 是输出维度
    N, D_in, H, D_out = 64, 1000, 100, 10

    # 产生输入和输出的随机张量
    x = torch.randn(N, D_in, device=device)
    y = torch.randn(N, D_out, device=device)

    # 产生随机权重的张量
    w1 = torch.randn(D_in, H, device=device, requires_grad=True)
    w2 = torch.randn(H, D_out, device=device, requires_grad=True)

    learning_rate = 1e-6
    for t in range(500):
        # 正向传播：使用张量上的操作来计算输出值y；
        # 我们通过调用 MyReLU.apply 函数来使用自定义的ReLU
        y_pred = MyReLU.apply(x.mm(w1)).mm(w2)

        # 计算并输出loss
        loss = (y_pred - y).pow(2).sum()
        print(t, loss.item())

        # 使用autograd计算反向传播过程。
        loss.backward()

        with torch.no_grad():
            # 用梯度下降更新权重
            w1 -= learning_rate * w1.grad
            w2 -= learning_rate * w2.grad

            # 在反向传播之后手动清零梯度
            w1.grad.zero_()
            w2.grad.zero_()


def nn_use():
    """
    使用 nn包 来实现两层的网络
    """
    import torch

    # N是批大小；D是输入维度
    # H是隐藏层维度；D_out是输出维度
    N, D_in, H, D_out = 64, 1000, 100, 10

    # 创建输入和输出随机张量
    x = torch.randn(N, D_in)
    y = torch.randn(N, D_out)

    # 使用nn包将我们的模型定义为一系列的层。
    # nn.Sequential是包含其他模块的模块，并按顺序应用这些模块来产生其输出。
    # 每个线性模块使用线性函数从输入计算输出，并保存其内部的权重和偏差张量。
    # 在构造模型之后，我们使用.to()方法将其移动到所需的设备。
    model = torch.nn.Sequential(
        torch.nn.Linear(D_in, H),
        torch.nn.ReLU(),
        torch.nn.Linear(H, D_out),
    )

    # nn包还包含常用的损失函数的定义；
    # 在这种情况下，我们将使用平均平方误差(MSE)作为我们的损失函数。
    # 设置reduction='sum'，表示我们计算的是平方误差的“和”，而不是平均值;
    # 这是为了与前面我们手工计算损失的例子保持一致，
    # 但是在实践中，通过设置reduction='elementwise_mean'来使用均方误差作为损失更为常见。
    loss_fn = torch.nn.MSELoss(reduction='sum')

    learning_rate = 1e-4
    for t in range(500):
        # 前向传播：通过向模型传入x计算预测的y。
        # 模块对象重载了__call__运算符，所以可以像函数那样调用它们。
        # 这么做相当于向模块传入了一个张量，然后它返回了一个输出张量。
        y_pred = model(x)

        # 计算并打印损失。
        # 传递包含y的预测值和真实值的张量，损失函数返回包含损失的张量。
        loss = loss_fn(y_pred, y)
        print(t, loss.item())

        # 反向传播之前清零梯度
        model.zero_grad()

        # 反向传播：计算模型的损失对所有可学习参数的导数（梯度）。
        # 在内部，每个模块的参数存储在requires_grad=True的张量中，
        # 因此这个调用将计算模型中所有可学习参数的梯度。
        loss.backward()

        # 使用梯度下降更新权重。
        # 每个参数都是张量，所以我们可以像我们以前那样可以得到它的数值和梯度
        with torch.no_grad():
            for param in model.parameters():
                param -= learning_rate * param.grad


def optim_use():
    """
    使用 optim 中的优化器来优化权重
    """
    import torch

    # N是批大小；D是输入维度
    # H是隐藏层维度；D_out是输出维度
    N, D_in, H, D_out = 64, 1000, 100, 10

    # 产生随机输入和输出张量
    x = torch.randn(N, D_in)
    y = torch.randn(N, D_out)

    # 使用nn包定义模型和损失函数
    model = torch.nn.Sequential(
        torch.nn.Linear(D_in, H),
        torch.nn.ReLU(),
        torch.nn.Linear(H, D_out),
    )
    loss_fn = torch.nn.MSELoss(reduction='sum')

    # 使用optim包定义优化器（Optimizer）。Optimizer将会为我们更新模型的权重。
    # 这里我们使用Adam优化方法；optim包还包含了许多别的优化算法。
    # Adam构造函数的第一个参数告诉优化器应该更新哪些张量。
    learning_rate = 1e-4
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

    for t in range(500):
        # 前向传播：通过像模型输入x计算预测的y
        y_pred = model(x)

        # 计算并打印loss
        loss = loss_fn(y_pred, y)
        print(t, loss.item())

        # 在反向传播之前，使用optimizer将它要更新的所有张量的梯度清零(这些张量是模型可学习的权重)
        optimizer.zero_grad()

        # 反向传播：根据模型的参数计算loss的梯度
        loss.backward()

        # 调用Optimizer的step函数使它所有参数更新
        optimizer.step()


def custom_nn_use_1():
    """
    构建自定义 nn 模块
    """
    import torch

    class TwoLayerNet(torch.nn.Module):
        def __init__(self, D_in, H, D_out):
            """
            在构造函数中，我们实例化了两个nn.Linear模块，并将它们作为成员变量。
            """
            super(TwoLayerNet, self).__init__()
            self.linear1 = torch.nn.Linear(D_in, H)
            self.linear2 = torch.nn.Linear(H, D_out)

        def forward(self, x):
            """
            在前向传播的函数中，我们接收一个输入的张量，也必须返回一个输出张量。
            我们可以使用构造函数中定义的模块以及张量上的任意的（可微分的）操作。
            """
            h_relu = self.linear1(x).clamp(min=0)
            y_pred = self.linear2(h_relu)
            return y_pred

    # N是批大小； D_in 是输入维度；
    # H 是隐藏层维度； D_out 是输出维度
    N, D_in, H, D_out = 64, 1000, 100, 10

    # 产生输入和输出的随机张量
    x = torch.randn(N, D_in)
    y = torch.randn(N, D_out)

    # 通过实例化上面定义的类来构建我们的模型。
    model = TwoLayerNet(D_in, H, D_out)

    # 构造损失函数和优化器。
    # SGD构造函数中对model.parameters()的调用，
    # 将包含模型的一部分，即两个nn.Linear模块的可学习参数。
    loss_fn = torch.nn.MSELoss(reduction='sum')
    optimizer = torch.optim.SGD(model.parameters(), lr=1e-4)
    for t in range(500):
        # 前向传播：通过向模型传递x计算预测值y
        y_pred = model(x)

        # 计算并输出loss
        loss = loss_fn(y_pred, y)
        print(t, loss.item())

        # 清零梯度，反向传播，更新权重
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()


def custom_nn_use_2():
    import random
    import torch

    class DynamicNet(torch.nn.Module):
        def __init__(self, D_in, H, D_out):
            """
            在构造函数中，我们构造了三个nn.Linear实例，它们将在前向传播时被使用。
            """
            super(DynamicNet, self).__init__()
            self.input_linear = torch.nn.Linear(D_in, H)
            self.middle_linear = torch.nn.Linear(H, H)
            self.output_linear = torch.nn.Linear(H, D_out)

        def forward(self, x):
            """
            对于模型的前向传播，我们随机选择0、1、2、3，
            并重用了多次计算隐藏层的middle_linear模块。
            由于每个前向传播构建一个动态计算图，
            我们可以在定义模型的前向传播时使用常规Python控制流运算符，如循环或条件语句。
            在这里，我们还看到，在定义计算图形时多次重用同一个模块是完全安全的。
            这是Lua Torch的一大改进，因为Lua Torch中每个模块只能使用一次。
            """
            h_relu = self.input_linear(x).clamp(min=0)
            for _ in range(random.randint(0, 3)):
                h_relu = self.middle_linear(h_relu).clamp(min=0)
            y_pred = self.output_linear(h_relu)
            return y_pred

    # N是批大小；D是输入维度
    # H是隐藏层维度；D_out是输出维度
    N, D_in, H, D_out = 64, 1000, 100, 10

    # 产生输入和输出随机张量
    x = torch.randn(N, D_in)
    y = torch.randn(N, D_out)

    # 实例化上面定义的类来构造我们的模型
    model = DynamicNet(D_in, H, D_out)

    # 构造我们的损失函数（loss function）和优化器（Optimizer）。
    # 用平凡的随机梯度下降训练这个奇怪的模型是困难的，所以我们使用了momentum方法。
    criterion = torch.nn.MSELoss(reduction='sum')
    optimizer = torch.optim.SGD(model.parameters(), lr=1e-4, momentum=0.9)
    for t in range(500):
        # 前向传播：通过向模型传入x计算预测的y。
        y_pred = model(x)

        # 计算并打印损失
        loss = criterion(y_pred, y)
        print(t, loss.item())

        # 清零梯度，反向传播，更新权重
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()


# numpy_use()
# pytorch_use()
# autogrid_use()
# custom_autogrid_use()
# nn_use()
# optim_use()
# custom_nn_use_1()
custom_nn_use_2()

