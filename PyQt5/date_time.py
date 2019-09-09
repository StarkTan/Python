"""
使用 pyqt5 中的 QDate QTime QDateTime 类来操作时间
    QDtate 主要用于日期操作
    QTime 主要用于时间操作
    QDateTime 包含上面两个类的操作
"""

from PyQt5.QtCore import QDate, QTime, QDateTime, Qt


def current_date_time():
    """
    创建当前日期和时间
    :return:
    """
    now = QDate().currentDate()  # 获取当前日期
    print(now.toString(Qt.ISODate))  # 以ISO格式展示日期 xxxx-xx-xx
    print(now.toString(Qt.DefaultLocaleLongDate))  # 以电脑的默认配置展示
    datetime = QDateTime().currentDateTime()  # 获取当前日期和时间
    print(datetime.toString())  # 当前时间和日期转为字符串
    time = QTime().currentTime()  # 获取当前时间
    print(time.toString(Qt.DefaultLocaleLongDate))  # 以默认格式打印时间


def utc_time():
    """
    本地时间和UTC时间的相互转换
    """
    now = QDateTime().currentDateTime()
    print("Local datetime: ", now.toString(Qt.ISODate))
    now_utc = now.toUTC()  # 本地时间转化成UTC时间
    print("Universal datetime: ", now_utc.toString(Qt.ISODate))
    now = now_utc.toLocalTime()  # UTC时间转化成本地时间
    print("Local datetime: ", now.toString(Qt.ISODate))
    print("The offset from UTC is: {0} seconds".format(now.offsetFromUtc()))  # 与UTC时间相差秒数


def number_days():
    """
    对日期进行计算
    """
    d = QDate(1945, 5, 7)
    print("Days in week: {0}".format(d.dayOfWeek()))
    print("Days in month: {0}".format(d.daysInMonth()))
    print("Days in year: {0}".format(d.daysInYear()))


def difference_days():
    """
    比较两个日期之间的间隔
    """
    xmas1 = QDate(2018, 12, 24)
    xmas2 = QDate(2020, 12, 24)
    now = QDate().currentDate()
    days_passed = xmas1.daysTo(now)  # 比较日期距离
    print("{0} days have passed since last XMas".format(days_passed))
    nof_days = now.daysTo(xmas2)
    print("There are {0} days until next XMas".format(nof_days))


def datetime_arithmetic():
    """
    时间日期的计算
    """
    now = QDateTime().currentDateTime()

    print("Today:", now.toString(Qt.ISODate))
    print("Adding 12 days: {0}".format(now.addDays(12).toString(Qt.ISODate)))
    print("Subtracting 22 days: {0}".format(now.addDays(-22).toString(Qt.ISODate)))

    print("Adding 50 seconds: {0}".format(now.addSecs(50).toString(Qt.ISODate)))
    print("Adding 3 months: {0}".format(now.addMonths(3).toString(Qt.ISODate)))
    print("Adding 12 years: {0}".format(now.addYears(12).toString(Qt.ISODate)))


def daylight_saving():
    """
    判断是否进入夏令时
    """
    now = QDateTime().currentDateTime()

    print("Time zone: {0}".format(now.timeZoneAbbreviation()))

    if now.isDaylightTime():
        print("The current date falls into DST time")
    else:
        print("The current date does not fall into DST time")


def unix_timestamp():
    """
    日期时间与 Unix 时间戳的转换
    """
    now = QDateTime().currentDateTime()
    timestamp = now.toSecsSinceEpoch()
    print(timestamp)
    d = QDateTime().fromSecsSinceEpoch(timestamp)
    print(d.toString(Qt.ISODate))


def julian_day():
    """
    获取 儒略日
    :return:
    """
    now = QDate().currentDate()
    print("Gregorian date for today: ", now.toString(Qt.ISODate))
    print("Julian day for today: ", now.toJulianDay())


# current_date_time()
# utc_time()
# number_days()
# difference_days()
# datetime_arithmetic()
# daylight_saving()
# unix_timestamp()
julian_day()
