# 模拟银行转账

'''
create table CCB(
    name varchar(20),
    money float8
);

create table ICBC(
    name varchar(20),
    money float8
);
'''

import pymysql

db_conn = pymysql.connect("localhost", "root", "123456", chrset="utf8")
cursor = db_conn.cursor()

try:
    cursor.execute("update CCB set money=5000 where name='zhuanzhang';")
    cursor.execute("update ICBC set money ... 会出错")
    db_conn.commit()
    print("OJBK")
except:
    db_conn.rollback()
    print("Something Is Wrong. Rollback")

cursor.close()
db_conn.close()

