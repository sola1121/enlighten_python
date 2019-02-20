import time
from socket import *

# 发送广播的地址
# 也可以直接写 <broadcast>, 代替IP
dest = ('176.209.103.255', 12345)   # 176.209.103.255

# 设置数据报套接字
sen = socket(AF_INET, SOCK_DGRAM)

# 设置允许广播
sen.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

count = 1

while True:
    time.sleep(1)
    sen.sendto(b'SEND TO ALL RECV %d' % count, dest)
    print("=============SEND %d===========" % count)
    data, addr = sen.recvfrom(4096)
    print("GET MSSAGE: %s, FROM: %s"% (data.decode(), addr))
    count += 1

sen.close()