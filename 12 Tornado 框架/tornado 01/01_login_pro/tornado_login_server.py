from tornado.httpserver import HTTPServer
from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop

import time

class LoginHandler(RequestHandler):
    def get(self, *args, **kwargs):
        msg = self.get_query_argument("msg", None)
        if msg:
            self.write("用户错误")
        else:
            self.render("login.html")

    def post(self, *args, **kwargs):
        the_name = self.get_body_argument("username")
        the_pass = self.get_body_argument("password")
        if the_name == "abc" and the_pass == "123":
            # 接收上传文件
            # print(self.request)
            # HTTPServerRequest对象的files属性绑定着用户通过表单上传的文件,
            # 如果用户没有上传文件, files属性是空字典
            # 如果上传了文件
            # {'input name绑定': [
            #                  {'content-type': 'image/jpg', 'body': 二进制格式表示的文件内容, 'filename': '文件本地名称'},
            #                  {另一个},
            #                   ...
            #       ]}
            if self.request.files:
                # print(self.request.files)
                count = 0
                avs = self.request.files["avatar"]
                for data in avs:
                    filename = "上传_" + str(count) + "_" + data['content_type'].replace("/", ".")
                    with open(filename, 'wb') as file:
                        file.write(data['body'])
                    count += 1
            self.redirect("/blog?username=%s" %the_name)
        else:
            self.redirect("/login?msg=fail")


class BlogHandler(RequestHandler):
    def get(self, *args, **kwargs):
        the_name = self.get_query_argument("username", None)
        self.write("<h3>%s</h3><h3>跳转成功.</h3>" %the_name)


if __name__ == "__main__":

    login_app = Application(handlers=[("/$|/login.*", LoginHandler),
                                      ("/blog", BlogHandler)
                                      ])
    server = HTTPServer(login_app)
    server.listen(12346)
    IOLoop.current().start()
