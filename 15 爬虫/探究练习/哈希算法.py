# 将数据内容通过一定的算法获得其数据指纹, 具体的是通过压缩内容二进制内容, 获得定长的内容

import hashlib

# sha256
print(hashlib.sha256(bytes("hello_world", encoding="utf-8")).hexdigest())

# md5
md5_obj = hashlib.md5()   # 创建指纹算法的对象
md5_obj.update("hello_world".encode("utf-8"))   # 以指定编码将内容传入
print(md5_obj.hexdigest())   # 获取十六进制的内容

# 获取文件的指定哈希值, 可以用来判断以个文件是否是一样, 即是否发生了前后的修改
def hash_file(file_addre):
    chunk_size = 4096
    sha256_obj = hashlib.sha256()
    with open(file_addre, 'rb') as file:
        while True:
            chunk = file.read(chunk_size)
            if chunk is None:
                break
            sha256_obj.update(chunk)
    print(sha256_obj.hexdigest())

hash_file("./Python网络爬虫讲义201807.doc")