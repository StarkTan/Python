import tushare as ts
import pymysql.cursors
import collections


def get_all_code():
    df = ts.get_stock_basics()
    Code = df.index
    deque = collections.deque(maxlen=4000)
    for code in Code:
        deque.append(code)
    return deque


def insert_code():
    """
    股票代码数据进入数据库
    :return:
    """
    df = ts.get_stock_basics()
    Code = df.index
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='root',
                                 db='stock_python',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            for code in Code:
                info = df.ix[code]
                sql = "INSERT INTO `tick_info` \
                    (`code`, `name`, `industry`, `area`, `pe`, `outstanding`, `totals`, `totalAssets`,\
                     `liquidAssets`, `fixedAssets`, `reserved`, `reservedPerShare`, `esp`, `bvps`, `pb`,\
                     `timeToMarket`, `undp`, `perundp`, `rev`, `profit`, `gpr`, `npr`, `holders`) VALUES\
                    ('%s', '%s', '%s', '%s', '%f', '%f', '%f', '%f',\
                      '%f', '%f', '%f', '%f', '%f', '%f', '%f',\
                       '%d', '%f', '%f', '%f', '%f', '%f', '%f', '%f')" % \
                      (code, info['name'], info['industry'], info['area'], info['pe'], info['outstanding'],
                       info['totals'], info['totalAssets'],
                       info['liquidAssets'], info['fixedAssets'], info['reserved'], info['reservedPerShare'],
                       info['esp'], info['bvps'], info['pb'],
                       info['timeToMarket'], info['undp'], info['perundp'], info['rev'], info['profit'], info['gpr'],
                       info['npr'], info['holders'])
                cursor.execute(sql)
            connection.commit()
    finally:
        connection.close()


# insert_code()

def create_table(table_name, connection):
    sql1 = """ drop table if exists history;"""
    sql2 = """  CREATE TABLE `history` (
              `date` int(8) NOT NULL,
              `open` double DEFAULT NULL,
              `high` double DEFAULT NULL,
              `close` double DEFAULT NULL,
              `low` double DEFAULT NULL,
              `volume` double DEFAULT NULL,
              `ma_5` double DEFAULT NULL,
              `ma_10` double DEFAULT NULL,
              `ma_20` double DEFAULT NULL,
              `ma_60` double DEFAULT NULL,
              `ma_120` double DEFAULT NULL,
              `ma_240` double DEFAULT NULL,
              `ma_480` double DEFAULT NULL,
              PRIMARY KEY (`date`),
              KEY `ix_history_date` (`date`)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
                """
    sql1 = sql1.replace('history', table_name)
    sql2 = sql2.replace('history', table_name)
    with connection.cursor() as cursor:
        cursor.execute(sql1)
        cursor.execute(sql2)
    connection.commit()


def insert_history(code, connection, index=False, start='1990-01-01', end='2019-01-01', create=False):
    if index:
        table_name = str(code) + "_index_his"
    else:
        table_name = str(code) + "_his"
    if create:
        create_table(table_name, connection)
    dh = ts.get_k_data(code, index=index, start=start, end=end)
    Indexs = dh.index
    with connection.cursor() as cursor:
        for index in Indexs:
            hist = dh.ix[index]
            sql = "REPLACE INTO `" + table_name + "` (`date`, `open`, `high`, `close`, `low`, `volume`) " \
                                                  "VALUES ('%d', '%f', '%f', '%f', '%f', '%f')" % \
                  (int(hist['date'].replace('-', '')), hist['open'], hist['high'],
                   hist['close'], hist['low'], hist['volume'])
            cursor.execute(sql)
        connection.commit()


# 数据分析
def get_index_range_day(up, down, connection):
    deque_1 = collections.deque()
    deque_2 = collections.deque()
    deque_3 = collections.deque()
    deque_4 = collections.deque()
    deque_5 = collections.deque()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM 000001_index_his ORDER BY 000001_index_his.date ASC "
            cursor.execute(sql)
            connection.commit()
            results = cursor.fetchall()
            for row in results:
                close = row['close']
                date = row['date']
                if close > 3200 and close < 3250:
                    deque_1.append(date)
                elif close > 3150 and close < 3200:
                    deque_2.append(date)
                elif close > 3100 and close < 3150:
                    deque_3.append(date)
                elif close > 3050 and close < 3100:
                    deque_4.append(date)
                elif close > 3000 and close < 3050:
                    deque_5.append(date)

    finally:
        connection.close()
    return (deque_1, deque_2, deque_3, deque_4, deque_5)


def get_stock_avg(code, deques, connection):
    arr_1 = []
    arr_2 = []
    arr_3 = []
    arr_4 = []
    arr_5 = []
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM " + code + "_his"
            cursor.execute(sql)
            connection.commit()
            results = cursor.fetchall()
            for row in results:
                close = row['close']
                date = row['date']
                if date in deques[0]:
                    arr_1.append(close)
                elif date in deques[1]:
                    arr_2.append(close)
                elif date in deques[2]:
                    arr_3.append(close)
                elif date in deques[3]:
                    arr_4.append(close)
                elif date in deques[4]:
                    arr_5.append(close)
    finally:
        connection.close()
    return (arr_1, arr_2, arr_3, arr_4, arr_5)


def get_stock_avg_other(code, deques, connection):
    arr_1 = []
    arr_2 = []
    arr_3 = []
    arr_4 = []
    arr_5 = []
    dh = ts.get_k_data(code, start='1990-01-01', end='2019-01-01', autype=None)
    indexs = dh.index
    for index in indexs:
        date = dh.ix[index]['date']
        close = dh.ix[index]['close']
        date = int(date.replace('-', ''))
        if date in deques[0]:
            arr_1.append(close)
        elif date in deques[1]:
            arr_2.append(close)
        elif date in deques[2]:
            arr_3.append(close)
        elif date in deques[3]:
            arr_4.append(close)
        elif date in deques[4]:
            arr_5.append(close)
    return (arr_1, arr_2, arr_3, arr_4, arr_5)


def get_step_range(code, conn, start=20100101,end =20100101, step=0.1):
    highest = 0
    lowest = 1000
    hanlder_time = 0
    first = True
    high_get = 0
    try:
        with conn.cursor() as cursor:
            sql = 'SELECT * FROM ' + str(code) + '_his WHERE date BETWEEN  ' + str(start) + ' and ' + str(
                end) + '  ORDER BY date ASC'
            cursor.execute(sql)
            print(sql)
            conn.commit()
            results = cursor.fetchall()
            total = 0
            day = 0
            print(results.__len__())
            for row in results:
                open = row['open']
                high = row['high']
                low = row['low']
                close = row['close']
                if high > highest:
                    highest = high
                if low < lowest:
                    lowest = low
                total = total + high - low
                day = day + 1

    finally:
        conn.close()
    return highest, lowest, total / day


def get_wive_count(code, conn, start=20100101,end=20100101, last_sell=6.0,step=0.10):
    count = 0
    try:
        with conn.cursor() as cursor:
            sql = 'SELECT * FROM ' + str(code) + '_his WHERE date BETWEEN  ' + str(start) + ' and ' + str(
                end) + '  ORDER BY date ASC'
            #sql = "SELECT * FROM " + code + "_his WHERE date>" + str(start) + " ORDER BY date ASC"
            cursor.execute(sql)
            conn.commit()
            results = cursor.fetchall()
            for row in results:
                close = row['close']
                high = row['high']
                low = row['low']
                if high - last_sell >= step:
                    sell = int((high - last_sell) / step)
                    count = count + sell
                    last_sell = last_sell + step * sell
                if last_sell - close >= step:
                    buy = int((last_sell - close) / step)
                    last_sell = last_sell - step * buy
    finally:
        conn.close()
    return count


# 列出在特定时间，处于特定价位的

def get_by_time_price(conn, code,low=1.0,up=2.0, tartime=20170525, endtime=20180525):
    sql = 'SELECT close,date FROM ' + str(code) + '_his WHERE date in (' + str(tartime) + ',' + str(endtime) + ')'
    tar_data=0.0
    end_date=0.0
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            conn.commit()
            results = cursor.fetchall()
            for row in results:
                date = row['date']
                close = row['close']
                if date==tartime :
                    tar_data = close
                if date == endtime:
                    end_date = close
        if tar_data>low and tar_data<up:
            return (tar_data,end_date)
        else:
            return (0,0)
    except:
        return (0,0)

import stock.utils
conn1 = stock.utils.get_conn()
conn2 = stock.utils.get_conn()
# deque = get_all_code()
# for code in deque:
#     res = get_by_time_price(conn,code,low=10.0,up=12.0,tartime=20170525, endtime=20180525)
#     if not res[0]==0:
#         print(code,res)
#         conn1 = stock.utils.get_conn()
#         print(get_step_range(str(code), conn1, start=20170101))
#         conn1 = stock.utils.get_conn()
#         print(get_wive_count(str(code), conn1, last_sell=12,start=20170101,step=0.1))
print(get_step_range('601939', conn1, start=20170520,end=20180520))
print(get_wive_count(code='601939',conn=conn2,start=20170520,end=20180520,last_sell=6.0,step=0.10))