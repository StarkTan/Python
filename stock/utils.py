import pymysql.cursors

def get_conn():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='root',
                                 db='stock_python',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    connection.begin()
    return connection
