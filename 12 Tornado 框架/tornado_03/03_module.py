from tornado.options import options, define, parse_config_file
from tornado.web import Application, RequestHandler, UIModule
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
        self.render("blog_index.html")


class LoginModule(UIModule):

    def render(self, *args, **kwargs):
        print(self.request)
        print(self.request.uri)   # uri=路径+get参数
        print(self.request.path)   # 路径
        print(self.request.query)   # get参数
        return self.render_string("the_module/login_module.html", result=None)


class BlogModule(UIModule):
    def render(self, *args, **kwargs):
        content1 = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. "
        content2 = "Autem iusto minus nisi! At cum debitis dolorum eos, iste itaque maiores nobis provident."
        content3 = "Quae quidem quod reiciendis repudiandae sunt suscipit veritatis."
        blogs = [
            {"avator": "get_head.jpg", "author": "hinata", "title": "如何做好一只猫.", "content": content1, "tags": "game cat", "count": 2},
            {"avator": "rabit02.png", "author": "luna", "title": "如何鸽.", "content": content2, "tags": "game cat", "count": 4},
            {"avator": None, "author": "siro", "title": "如何杀害一个豆腐.", "content": content3, "tags": "game cat", "count": 0},
        ]
        return self.render_string("the_module/blog_module.html", blogs=blogs)


class RegistHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render("regist_index.html")

    def post(self, *args, **kwargs):
        pass


# parse_config_file('../config/config')
# define('duankou',type=int,default=8888)
app = Application(handlers=[('/', IndexHandler),
                            ('/login', LoginHandler),
                            ('/blog', BlogHandler),
                            (r'/regist|/regist/', RegistHandler),
                            ],
                  template_path="./the_template",   # 配置template地址
                  static_path="./the_statics",   # 配置静态资源
                  ui_modules={"login_module": LoginModule, "blog_module": BlogModule},   # 配置module文件, 匹配在模块中的login_module()
                  )
server = HTTPServer(app)
server.listen(8000)
IOLoop.current().start()