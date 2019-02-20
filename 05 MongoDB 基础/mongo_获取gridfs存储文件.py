import pymongo
import gridfs   # 这是和pymongo绑定的插件

db_conn = pymongo.MongoClient("localhost", 27017)
db = db_conn.file_store

fs = gridfs.GridFS(db)

# 所有文件的游标
files = fs.find()

print("获得文件:", files.count())

# 每个文件对象file
for file in files:
    print("查找", file.filename)
    if file.filename == "02.jpg":
        with open(file.filename, 'wb') as f:
            while True:
                # file的read()函数可以获取文件内容
                data = file.read(64)
                if data is None:
                    break
                f.write(data)

db_conn.close()

