import pymysql

# 1. 创建数据库连接
db = pymysql.connect("localhost", "root", "123456", "test2", charset='utf8')

# 2. 创建游标对象
cursor = db.cursor()

# 3. 利用游标对象cursor的方法来操作数据库
cursor.execute("insert into 表名 values(...);")   # 改中文为有意义字符

# 4. 如有增删改, 提交到数据库
db.commit()

# 5. 关闭游标对象
cursor.close()

# 关闭数据库
db.close()
        