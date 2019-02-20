from tornado.options import options, define, parse_config_file
from tornado.web import Application, RequestHandler
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

import json

class IndexHandler(RequestHandler):

    def get(self, *args, **kwargs):
        self.render("login_index.html", result=None)


class LoginHandler(RequestHandler):

    def get(self, *args, **kwargs):
        msg = self.get_query_argument("msg", None)
        if msg:
            msg = "用户名或密码错误"
        self.render("login_index.html", result=msg)

    def post(self, *args, **kwargs):
        username = self.get_body_argument('the_name', None)
        password = self.get_body_argument('the_pass', None)
        print(username, password)
        if username=='abc' and password=='123':
            #跳转到blog页面
            self.redirect('/blog?username='+username)
        else:
            #跳转回登录界面
            self.redirect('/?msg=fail')


class BlogHandler(RequestHandler):
    def get(self, *args, **kwargs):
        content1 = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. "
        content2 = "Autem iusto minus nisi! At cum debitis dolorum eos, iste itaque maiores nobis provident."
        content3 = "Quae quidem quod reiciendis repudiandae sunt suscipit veritatis."
        blogs = [
            {"avator": "get_head.jpg", "author": "hinata", "title": "如何做好一只猫.", "content": content1, "tags": "game cat", "count": 2},
            {"avator": "rabit02.png", "author": "luna", "title": "如何鸽.", "content": content2, "tags": "game cat", "count": 4},
            {"avator": None, "author": "siro", "title": "如何杀害一个豆腐.", "content": content3, "tags": "game cat", "count": 0},
        ]
        self.render("blog_index.html", var_a=3, var_b=6, the_func=self.the_func, blogs=blogs)

    def the_func(self, a, b):
        # 自定义方法, 将赋给模板中的the_func方法
        return a*b


# 钩子方法示例
class BlogHandler1(RequestHandler):
    # 钩子方法, 是一个空方法定义在父类中
    def set_default_headers(self):
        # 让继承者自定义响应头
        print("1. set_default_handers方法被调用")

    def initialize(self):
        # 让继承者在执行get/post方法之前传入参数或者执行一些初始化操作
        # 如: 连接数据库...
        print("2. initialize方法被调用")

    def on_finish(self):
        # 执行get/post方法执行完成后做一些清理工作
        print("最后. on_finish方法被调用")

    def get(self, *args, **kwargs):
        # 以Json字符串作为响应内容
        # Json字符串格式 {"key1": "value1", "key2": "value2"}
        resp = {
            "key1": "value1",
            "key2": "value2",
        }
        self.write(resp)   # 传递给浏览器时, 会被自动转换为json

        # self.set_header("Content-Type", "application/json; charset=UTF-8")   # 设置响应
        # json_str = json.dumps(resp)   # 转换为纯json字符串
        # self.write(json_str)

    def post(self, *args, **kwargs):
        pass


# define('duankou',type=int,default=8888)
# parse_config_file('../config/config')
app = Application(handlers=[('/',IndexHandler),
                            ('/login',LoginHandler),
                            ('/blog',BlogHandler),
                            ],
                  template_path="./the_template",   # 配置template地址
                  static_path="./the_statics",   # 配置静态资源
                  )
server = HTTPServer(app)
server.listen(8000)
IOLoop.current().start()