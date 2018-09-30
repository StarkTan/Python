import tushare as ts
dh = ts.get_hist_data('601939',ktype='5')
#dh = ts.get_k_data("601939", start='2018-05-22', end='2019-01-01',ktype='60')
print(dh)
