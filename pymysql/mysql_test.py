import pymysql.cursors


def create_table():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='root',
                                 db='pymysql',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
            sql = """CREATE TABLE EMPLOYEE (
                     FIRST_NAME  CHAR(20) NOT NULL,
                     LAST_NAME  CHAR(20),
                     AGE INT,  
                     SEX CHAR(1),
                     INCOME FLOAT )"""
            cursor.execute(sql)
            connection.commit()
    except:
        connection.rollback()
    finally:
        connection.close()


def insert_record():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='root',
                                 db='pymysql',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
                  ('Mac', 'Mohan', 20, 'M', 2000)
            cursor.execute(sql)
            connection.commit()
    except:
        connection.rollback()
    finally:
        connection.close()


def query():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='root',
                                 db='pymysql',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM EMPLOYEE \
                    WHERE INCOME > '%d'" % (1000)
            cursor.execute(sql)
            connection.commit()
            results = cursor.fetchall()
            for row in results:
                print(row['FIRST_NAME'])
    finally:
        connection.close()


def update():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='root',
                                 db='pymysql',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
            cursor.execute(sql)
            connection.commit()
    except:
        connection.rollback()
    finally:
        connection.close()

def delete():
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='root',
                                 db='pymysql',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            sql = sql = "DELETE FROM EMPLOYEE WHERE AGE > '%d'" % (20)
            cursor.execute(sql)
            connection.commit()
    except:
        connection.rollback()
    finally:
        connection.close()
delete()