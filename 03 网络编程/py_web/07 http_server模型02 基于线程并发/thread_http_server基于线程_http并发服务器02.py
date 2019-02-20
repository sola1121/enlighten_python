"""
完成httpserver的并发
并发使用多线程完成
用不同的后端程序处理不同的请求
可以简单的显示静态页面
"""

import os, sys
import time
from threading import Thread
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR

# 存放静态网页
static_root = "./template"
# 存放python处理模块
handler_root = "./handler"

ADDR = ('127.0.0.1', 8000)

# http服务器类
class HTTPserver:

    def __init__(self, addr):
        self.server = socket(AF_INET, SOCK_STREAM, 0)
        self.server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.server.bind(addr)
        self.server.listen(20)
        self.serverName = addr[0]
        self.serverPort = addr[1]

    # 正式启动服务器, 连接入的用户创建用户线程
    def serverForever(self):
        while True:
            self.conn, self.addr = self.server.accept()
            clientThread = Thread(target=self.handleRequset)
            clientThread.start()

    # 传门用于传入外部功能的接口
    def setApp(self, application):
        self.application = application

    # 处理线程
    def handleRequset(self):
        self.recvData = self.conn.recv(2048)
        requestHeaders = self.recvData.splitlines()
        for line in requestHeaders:
            print(line)
        else:
            print("\n========%s=======" % str(self.conn.getpeername()))
        
        # 获取到从浏览器输入的具体请求, 传输过来的是bytes
        # 浏览器的网页请求: b'GET /%E6%83%B3%E8%A6%81%E5%BE%97%E5%88%B0%E7%9A%84%E7%BD%91%E9%A1%B5 HTTP/1.1', b'Host: 127.0.0.1:8000',...
        getRequest = str(requestHeaders[0]).split(" ")[1]
        if getRequest[-3:] != ".py":
            if getRequest == "/":
                getFilename = static_root + "/index.html"
            else:
                getFilename = static_root + getRequest
            
            try:
                file = open(getFilename, 'r')
            except:
                responseHeaders = "HTTP/1.1 404 not found\r\n"
                responseHeaders += "\r\n"
                responseBody = "====Sorry, html not found===="
            else:
                requestHeaders = "HTTP/1.1 200 ok\r\n"
                responseHeaders += "\r\n"
                responseBody = file.read()
                file.close()
            finally:
                response = responseHeaders + responseBody
                self.conn.send(response.encode())
        else:
            # 需要的环境变量
            env = {}
            bodyContent = self.application(env, self.startResponse)
            response = "HTTP/1.1 {} \r\n".format(self.header_set[0])
            for hearder in self.header_set[1:]:
                response += "{0}:{1}\r\n".format(*hearder)
            response += "\r\n"
            response += bodyContent
            self.conn.send(response.encode())

        self.conn.close()
        
    def startResponse(self, status, response_handlers):
        serverHearders = [
            ("Date", time.strftime("H:M:S m-d-Y", time.localtime())),
            ("Server", "HTTPserver1.0")
        ]
        self.header_set = [status, response_handlers + serverHearders]


# 控制服务器启动
def main():
    # 启动时直接告知使用哪个模块那个函数处理请求, 如: python3 本文件名.py module app
    if len(sys.argv) < 3:
        sys.exit("请选择一个模块和应用")
    # 将handler文件夹加入python搜索路径
    sys.path.insert(0, handler_root)
    # 导入自己定义的想要导入的模块module
    mod = __import__(sys.argv[1])
    # 获取module下的app付给一个变量
    application = getattr(mod, sys.argv[2])   # mod.xxx属性, 具体操作中是 webApp.app

    hs = HTTPserver(ADDR)
    hs.setApp(application)
    print("Server HTTP on port %d" % ADDR[1])
    hs.serverForever()


if __name__ == "__main__":

    main()
