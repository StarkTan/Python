import baostock as bs
import pandas as pd

# 个股数据查询
lg = bs.login()
rs = bs.query_history_k_data_plus("sh.601939",
                                  "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,isST",
                                  start_date='2019-07-01', end_date='2019-07-07',
                                  frequency="d", adjustflag="3")
data_list = []
while (rs.error_code == '0') & rs.next():
    # 获取一条记录，将记录合并在一起
    data_list.append(rs.get_row_data())
result = pd.DataFrame(data_list, columns=rs.fields)
print(result)
print("-" * 10)
# 指数查询
rs = bs.query_history_k_data_plus("sh.000001",
                                  "date,code,open,high,low,close,preclose,volume,amount,pctChg",
                                  start_date='2019-07-01', end_date='2019-07-07', frequency="d")
print('query_history_k_data_plus respond error_code:' + rs.error_code)
print('query_history_k_data_plus respond  error_msg:' + rs.error_msg)
# 打印结果集
data_list = []
while (rs.error_code == '0') & rs.next():
    # 获取一条记录，将记录合并在一起
    data_list.append(rs.get_row_data())
result = pd.DataFrame(data_list, columns=rs.fields)
print(result)
