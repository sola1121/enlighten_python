import time

# 处理特定请求的模块
def app(environ, start_response):   # 这个是协议中固定格式, 就像signal自定义函数一样
    status = '200 ok'
    response_headers =[("Content-Type", "text/plain;charset=UTF-8;Server: localhost8000")]

    start_response(status, response_headers)

    return "\napp工作 %s" % time.ctime() 
