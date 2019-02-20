import pymongo
import bson   # 和pymongo绑定的插件, 将文件转换为bson
import time

db_conn = pymongo.MongoClient("localhost", 27017)
# use file_store
db = db_conn.file_store
# db.img
file_img = db.img 

# 存储
f = open("02.jpg", 'rb')
# 将读取的二进制流变为bson格式二进制的字串
content = bson.binary.Binary(f.read())

file_img.insert({"image_name": "02.jpg", "dump_date": time.ctime(), "content":content})
