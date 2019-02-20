# coding: utf-8

try:
    from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
except ImportError:
    from http.server import BaseHTTPRequestHandler, HTTPServer
    
# 请求处理类
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("GET method Run.")
        html_file = open(r"E:\达内学习文件\03 网络编程\py_web\07 服务器模型-0并行服务器\test.html", "rb")
        content = html_file.read()
        # 组织响应行, 这里200是响应码
        self.send_response(200)
        # 组织响应头, 这里字符串是响应头具体内容
        self.send_header('content-type', 'text/plain; charset=utf-8')
        # 响应头结束
        self.end_headers()
        # 发送响应体
        self.wfile.write(content)
        return

    def do_POST(self):
        pass
    
# 指定地址
address = ("0.0.0.0", 8000)

# 生产服务器对象
server = HTTPServer(address, RequestHandler)

# 运行
server.serve_forever()
