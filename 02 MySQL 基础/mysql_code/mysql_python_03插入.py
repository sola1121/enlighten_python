import pymysql

db_conn = pymysql.connect("localhost", "root", "123456", charset="utf8")
cursor = db_conn.cursor()

re = cursor.execute("insert into test2.sheng values('11', '111111', '日本省');")
print("执行返回: %s" %re)

cursor.execute("select * from test2.sheng;")
re = cursor.fetchall()
for info in re:
    print(info)

db_conn.commit()
cursor.close()
db_conn.close()
