import pymysql

db = pymysql.connect("localhost", "root", "123456", charset="utf8")
cursor = db.cursor()

cursor.execute("use test2;")

# 使用fetchone
cursor.execute("select * from test2.sheng;")
data1 = cursor.fetchone()
data2 = cursor.fetchone()
print(data1, data2, "\n-----------------------")

# 使用fetchmany
cursor.execute("select * from test2.sheng;")
data = cursor.fetchmany(3)
for d in data:
    print(d)
else:
    print("-----------------------")

# 使用 fetchall
cursor.execute("select * from test2.sheng;")
data = cursor.fetchall()
for d in data:
    print(d)

db.commit()
cursor.close()
db.close()
