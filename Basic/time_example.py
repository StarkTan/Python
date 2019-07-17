import time

# 获取时间戳
time1 = time.time()
print(time1)

# 获取本地时间
localTime = time.localtime(time.time())
print(localTime)

# 格式化本地时间
localTimeStrs = time.strftime("%Y-%m-%d %H:%M:%S", localTime)
print(localTimeStrs)

# 计算时间差
import datetime

day1 = datetime.datetime(2018, 5, 16)
day2 = datetime.datetime(2018, 4, 16)

# 计算指定时间的间隔
print((day1 - day2).days)

# 获取当前时间
nowTime = datetime.datetime.now()
print("nowTime: ", nowTime)

# 当前指定时间
# 获取当前年份
print(nowTime.year)
print(nowTime.day)
print(nowTime.month)
print(nowTime.hour)
print(nowTime.minute)
print(nowTime.second)

# 当前时间往前推29天计算日期,也就是近30天的其实范围
beforeTime = nowTime - datetime.timedelta(days=29)

# 往后推就使用 + 号，当然还可以使用 hours（小时） 、minutes(分钟)、seconds(秒）等单位运算。
print("beforeTime: ", beforeTime)
