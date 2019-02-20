# 使用浏览器进行连接
# 静态网页处理器
# 采用循环模式, 无法满足客户端长连接

import socket, time
import os

DESKTOP = os.environ["USERPROFILE"] + "\\Desktop\\"

# 处理客户端请求
def handleClient(conn):
    request = conn.recv(2048)
    requestHeadlers = request.splitlines()
    for line in requestHeadlers:
        print(line)
    
    try:
        file = open(DESKTOP + "答辩.txt", 'r', encoding='utf8')
    except IOError as e:
        print("-------获得错误:", e)
        response = "HTTP/1.1 404 not found\r\n"
        response += "\r\n"
        response += "sorry, file not found"
    else:
        print("----------成功传输---------")
        response = "HTTP/1.1 200 ok\r\n"
        response += "\r\n"
        for content in file:   # 连接成功时发送的file内容, 这得按照网页传输的标准来写
            response += content
    finally:
        conn.send(response.encode())
        conn.close()

# 流程控制
def main():
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('127.0.0.1', 12345))
    server.listen(20)
    
    while True:
        conn, addr = server.accept()
        print("CONNECTED", addr, time.asctime(time.localtime()))
        handleClient(conn)


if __name__ == "__main__":

    main()
