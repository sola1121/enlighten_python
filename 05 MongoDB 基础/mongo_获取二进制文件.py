import pymongo

db_conn = pymongo.MongoClient("localhost", 27017)
# use file_store
db = db_conn.file_store
# db.img
file_img = db.img

data = file_img.find({"image_name": "02.jpg"})   # data是pymongo.cursor.Cursor对象

# for it in data:
#     content = it["content"]
it = next(data)
with open("new_name.jpg", "wb") as f:
    f.write(it["content"])
