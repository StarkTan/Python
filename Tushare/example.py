import tushare as ts
ts.set_token('xxxxxx')
print(ts.__version__)

pro = ts.pro_api()
df = pro.daily(ts_code='601939.SH', start_date='20190101', end_date='20190702')
print(type(df))