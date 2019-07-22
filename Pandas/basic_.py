import pandas as pd

date1 = pd.to_datetime('20190718')
print(date1.dayofweek)
date2 = pd.to_datetime('2019-07-19')
print((date2 - date1).days)
