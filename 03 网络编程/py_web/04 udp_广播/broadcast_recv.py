from socket import *

HOST = ''
PORT = 12345

# 创建数据报式套接字
receive = socket(AF_INET, SOCK_DGRAM)

# 设置套接字可以接收广播
receive.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

# 设置端口可重用
receive.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

# 固定接收端的端口号, 没有绑定ip哦
receive.bind((HOST, PORT))

count = 1

while True:

    try:
        message, addr = receive.recvfrom(4096)
        print("form {1} get message: {0}".format(message.decode(), addr))

        receive.sendto(b"return %d, got." % count, addr)
        count += 1
    except(KeyboardInterrupt, SyntaxError):
        raise
    except Exception as e:
        print(e)

receive.close()
