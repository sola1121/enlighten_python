import pymysql

# 1. 创建数据库连接
db = pymysql.connect("localhost","root","123456")

# 2. 创建游标对象
cursor = db.cursor()

# 3. 利用游标对象cursor的方法来操作数据库
content = cursor.execute("select * from test2.sheng;")
print(content)

# 4. 如有增删改, 提交到数据库
db.commit()

# 5. 关闭游标对象
cursor.close()

# 关闭数据库
db.close()
        