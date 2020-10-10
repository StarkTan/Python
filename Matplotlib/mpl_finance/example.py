import pandas as pd
import numpy as np
import mpl_finance as mpf
import matplotlib.pyplot as plt


def draw_candlestick():
    index = np.arange(5)
    columns = np.array(['date', 'open', 'high', 'low', 'close'])
    datas = [
        (0, 12, 14, 12, 12.5),
        (1, 12, 14, 12, 12.5),
        (2, 12, 14, 12, 12.5),
        (3, 12, 14, 12, 12.5),
        (4, 12, 14, 12, 12.5),
    ]
    df = pd.DataFrame(datas, index=index, columns=columns)
    df = df.as_matrix()
    print(df)
    fig, ax = plt.subplots()
    # ax.xaxis_date()
    plt.xticks(rotation=45)
    mpf.candlestick_ohlc(ax, df, width=1.0, colorup='r', colordown='green', alpha=1)  ##设置利用mpf画股票K线图
    date_tickers = ['20190101', '20190102', '20190103', '20190104', '20190105']
    ax.set_xticks(range(len(date_tickers)))
    ax.set_xticklabels(date_tickers)
    ax.set_xticklabels(date_tickers)
    plt.show()
    return False

df = pd.read_json('../data.json', dtype=np.int)
print()
# draw_candlestick()
"""
import matplotlib.pyplot as plt  ## 导入画图模块
from matplotlib.pylab import date2num  ## 导入日期到数值一一对应的转换工具
from dateutil.parser import parse  ## 导入转换到指定格式日期的工具
import mpl_finance as mpf  ## 导入 mpl_finance 模块

plt.rcParams['font.family'] = 'SimHei'  ## 设置字体
fig, ax = plt.subplots()  ## 创建图片和坐标轴
fig.subplots_adjust(bottom=0.2)  ## 调整底部距离
ax.xaxis_date()  ## 设置X轴刻度为日期时间
plt.xticks(rotation=45)  ## 设置X轴刻度线并旋转45度
plt.yticks()  ## 设置Y轴刻度线
plt.title("股票代码 ** K线图")  ##设置图片标题
plt.xlabel("时间")  ##设置X轴标题
plt.ylabel("股价（元）")  ##设置Y轴标题
plt.grid(True, 'major', 'both', ls='--', lw=.5, c='k', alpha=.3)  ##设置网格线
data_list_ = [
    (date2num(parse(str(20181110))), 10, 20, 5, 15),
    (date2num(parse(str(20181111))), 10, 20, 5, 9),
    (date2num(parse(str(20181114))), 10, 20, 5, 9)]  # 其中元组的格式是（日期，开盘价，最高价，最低价，收盘价）
mpf.candlestick_ohlc(ax, data_list_, width=1.0, colorup='r', colordown='green', alpha=1)  ##设置利用mpf画股票K线图
plt.show()  ## 显示图片

"""