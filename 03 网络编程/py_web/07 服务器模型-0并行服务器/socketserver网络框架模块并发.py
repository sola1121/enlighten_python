from socketserver import *

# 创建服务器类
class Server(ForkingMixIn, TCPServer):    # class Server(ForkingTCPServer)
    """多进程TCP服务器"""
    pass

# 处理具体请求
class Handler(StreamRequestHandler):

    def handle(self):   # 重写父类中的方法
        addr = self.request.getpeername()
        print("Connect from", addr)
        while True:
            data = self.request.recv(1024).decode()
            if not data:
                break
            self.request.send(b"Get Your Message.")


server = Server(('127.0.0.1', 12345), Handler)
server.serve_forever()

