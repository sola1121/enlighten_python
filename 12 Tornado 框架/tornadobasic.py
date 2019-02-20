from tornado.options import define, parse_config_file, options
from tornado.web import Application, RequestHandler
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

define("port_define", type=int, default=12345)
parse_config_file('../config/config_file')


class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write("<h2><a href='/python/'>jump to python</a></h2>")
        self.write("<h2><a href='/golang/'>jump to golang</a></h2>")

    def post(self, *args, **kwargs):
        pass


class PythonHandler(RequestHandler):
    def get(self, para1=None, para2=None, *args, **kwargs):   # 接收正则传参
        self.write("<h2>hello Python!</h2>")
        if para1:
            self.write("<h3>para1: %s</h3>" %para1)
            if para2:
                self.write("<h3>para2: %s</h3>" %para2)

    def post(self, *args, **kwargs):
        self.write("post method to python.")
        day = self.get_body_argument("day", None)
        subject = self.get_body_arguments("subject")
        if day:
            self.write("<h3>day: %s</h3>" %day)
        if subject:
            self.write("<h3>subject: %s</h3>" %subject)
        day_lst = self.get_body_arguments("day")
        subject_lst = self.get_body_arguments("subject")
        print("day_lst ->", day_lst, "subject_lst ->", subject_lst)
        day_lst2 = self.get_arguments("subject")
        print("day_lst2 ->", day_lst2)


class GolangHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write("<h2>hello Golang!</h2>")
        # 接收使用get的传递过来的查询参数
        day = self.get_query_argument("day")
        subject = self.get_query_argument("subject", None)
        all_para = self.get_query_arguments("day")   # 获取所有day参数的值
        if day:
            self.write("<h3>day: %s</h3>" %day)
        if subject:
            self.write("<h3>subject: %s</h3>" %subject)
        print(all_para)


app = Application(handlers=[("[/index|/]", IndexHandler),
                            ("/python", PythonHandler),
                            ("/python/(day[0-9]+)", PythonHandler),   # 通过正则分组进行传参
                            ("/python/(day[0-9]+)/([a-z0-9]+)", PythonHandler),
                            ("/golang.*", GolangHandler),   # 用于get传参数
                            ])
server = HTTPServer(app)
server.listen(options.port_define)
IOLoop.current().start()
