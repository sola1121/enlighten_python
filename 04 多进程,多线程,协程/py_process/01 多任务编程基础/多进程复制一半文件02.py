import os 
from multiprocessing import Process 

#获取文件大小
size = os.path.getsize('file.jpg')

# 在创建进程前获取文件对象，父子进程操作同一个文件流
#　会造成操作混乱
# f = open('file.jpg','rb')

#复制前半部分
def copy1():
    f = open('file.jpg','rb')
    n = size // 2
    fw = open('copy1.jpg','wb')
    while True:
        if n < 64:
            data = f.read(n)
            fw.write(data)
            break
        data = f.read(64)
        fw.write(data)
        n -= 64
    fw.close()

#复制后半部分
def copy2():
    f = open('file.jpg','rb')
    fw = open("copy2.jpg",'wb')
    f.seek(size //2,0)
    while True:
        data = f.read(64)
        if not data:
            break
        fw.write(data)
    fw.close()

p1 = Process(target = copy1)
p2 = Process(target = copy2)

p1.start()
p2.start()

p1.join()
p2.join()
