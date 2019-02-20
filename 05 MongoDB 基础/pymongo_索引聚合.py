import pymongo

# 连接数据库
db_conn = pymongo.MongoClient("localhost", 27017)
# use stu
db = db_conn.stu
# db.class3
cls3 = db.class3

# 创建索引
index_name = cls3.ensure_index("name")
print(index_name)   # 打印返回的新索引名

# 复合索引
index_name = cls3.ensure_index([("name": 1), ("age": 1)])
print(index_name)

# 创建索引模型, 可同时创建多个索引
index1 = pymongo.IndexModel([("name", 1), ("age", -1)])
index2 = pymongo.IndexModel([("name", 1)])
indexes = cls3.create_indexes([index1, index2])

# 唯一索引
index_name = cls3.ensure_index("name", unique=True)

# 稀疏索引
index_name = cls3.ensure_index("name", sparse=True)

# 查看集合中索引
index_list = cls3.list_indexes()
for in_name in index_list:
    print(in_name)

# 删除索引
cls3.drop_index(index_name)   # 通过索引名删除索引
cls3.drop_indexes()   # 删除所有索引


# 聚合管道
l = [{"$group": {"_id": "$gender", "count": {"$sum": 1}}}, {"$match": {"count": {"$gt": 1}}}]  # gender分组并计数, 输出计数大于1的
cursor = cls3.aggregate(l)
