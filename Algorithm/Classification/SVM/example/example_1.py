"""
最简单的SVM例子（二维，直线）
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.array([[1, 1], [3, 3], [2, 3], [1, -1]])
y = np.array([0, 1, 1, 0])

# 画出测试数据的图形
n = y.shape[0]
xcord1 = []; ycord1 = []
xcord2 = []; ycord2 = []
for i in range(n):
    if int(y[i]) == 1:
        xcord1.append(x[i, 0])
        ycord1.append(x[i, 1])
    else:
        xcord2.append(x[i, 0])
        ycord2.append(x[i, 1])
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')
ax.scatter(xcord2, ycord2, s=30, c='green')
plt.show()

