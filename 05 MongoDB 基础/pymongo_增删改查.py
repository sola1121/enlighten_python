# coding: utf-8

# 使用pymongo进行增删改查
import pymongo

# 创建连接对象
db_conn = pymongo.MongoClient("localhost", 27017)

# use stu
# db = db_conn["db"]
db = db_conn.stu

# db.class3 
# cls3 = db["class3"]
cls3 = db.class3

# 查看支持的操作
# dir(cls3)
# help(cls3)

# 插入, 要插入字典, 由于python中的字典是无序的, 所以在数据库中, 顺序会是乱的, 可以使用collections模块中OrderedDict类
cls3.insert({"_id": 1, "name": "siro", "age": 2, "gender": "F"})
cls3.insert([{"_id": 2, "name": "kizuna_ai", "age": 5, "gender": "F"}, {"_id": 3, "name": "luna", "age": 1, "gender": "F"}])

cls3.insert_one({"_id": 6, "name": "akari", "age": 0, "gender": "F"})
cls3.insert_many([{"_id": 4, "name": "nojia", "age": 2, "gender": "F/M"}, {"_id": 5, "name": "hinata", "age": 0, "gender": "F/M"}])

# 数据删除
cls3.remove({"name": "siro"}, multi=False)   # 只删除第一条符合条件的文档

# 数据查找
cursor = cls3.find({}, {"_id": 0})
for info in cursor:
    print(info)

vtuber = db.vtuber   # 切换一个collection
cursor.find({"gender": {"$exists": True}}, {"_id": 0})
print(next(cursor))
print(cursor.next())

vtuber.find_one()

# 修改操作
cls3.update({"name": "mitu"}, {"$set": {"age": 0, "gender": "F"}}, upsert=True)   # 匹配不到则插入数据
cls3.update({"name": "mitu"}, {"$set": {"age": 0, "gender": "F"}}, multi=True)   # 修改匹配到的多条文档
cls3.update_many({"name": None}, {"$set": {"name": "mitu"}})
cls3.update_one({"name": None}, {"$set": {"name": "mitu"}})

# 查找并删除, 查找结果会返回
print(cls3.find_one_and_delete({"name": "siro"}))

db_conn.close()

