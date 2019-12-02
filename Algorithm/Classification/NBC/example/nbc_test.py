"""

"""
import pandas as pd

# 先读取训练文件
columns = []
datas = []
with open('data-training.txt', 'r', encoding='utf-8') as f:
    line = f.readline().strip()
    columns = line.split(' ')
    lines = f.readlines()
    for line in lines:
        datas.append(line.strip().split(' '))

train_data = pd.DataFrame(columns=columns, data=datas)

columns = []
datas = []
with open('data-test.txt', 'r', encoding='utf-8') as f:
    line = f.readline().strip()
    columns = line.split(' ')
    lines = f.readlines()
    for line in lines:
        datas.append(line.strip().split(' ')+[''])

test_data = pd.DataFrame(columns=columns, data=datas)
coeff = 1

#  基于贝叶斯原理方程 P(Ci|X) = P(X|Ci)*P(Ci)/P(X)
#  目的是为了计算P(Ci|X) X为已知的n维向量
#  先计算先验概率P(Ci) 可以从训练集中获得
index = ['yes', 'no']
data = pd.DataFrame(index=index)
# 计算 训练集中的P(Ci)即计算yes和no的出现概率
# 分子 = 原分子 + 平滑系数，分母 = 原分子 + 训练数据的分类总数 * 平滑系数
count = train_data[columns[-1]].value_counts()
data['PCi'] = [(count.loc[index[0]]+coeff)/count.sum()*coeff, (count.loc[index[1]]+coeff)/count.sum()*coeff]

# 计算 P(X|Ci) 使用公式 P(X|Ci) = P(X1|Ci)*P(X2|Ci)*P(X3|Ci)*。。。。P(Xk|Ci)
PXCi_data = []

for ci in index:
    # 计算指定属性和指定分类等待联合概率 P(Xk|Ci)
    # 因为是离散型变量所以使用 P(Xk|Ci) = Sik/Si Sik 指训练类别中类别为Ci第k个属性为xk的样本数
    # 加入平滑处理  P(Xk | Ci)平滑：分子 = 原分子 + 平滑系数，分母 = 原分子 + 指定属性种类数量 * 平滑系数
    PXCi = 1
    ci_temp = train_data[train_data[columns[-1]].isin([ci])]
    for pro in columns[:-1]:
        xk = test_data.loc[0:, [pro]].values[0][0]
        Si = len(ci_temp)
        Sik = len(ci_temp[ci_temp[pro].isin([xk])])
        PXCi *= (Sik+coeff)/(Sik + Si*coeff)
    PXCi_data.append(PXCi)
data['PXCi'] = PXCi_data

# 计算 P(Ci|X) = P(X|Ci)*P(Ci)/P(X)
PCiX_data_temp = data['PCi']*data['PXCi']
PX = PCiX_data_temp[0] + PCiX_data_temp[1]
data['PCiX'] = PCiX_data_temp/PX
print(data)






