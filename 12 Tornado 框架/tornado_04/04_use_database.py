from tornado.options import options, define, parse_config_file
from tornado.web import Application, RequestHandler, UIModule
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

import json
import pymysql
import hashlib

from tornado_04.util_md5 import own_md5


def connect_to_db():
    # 1. 建立与数据库的连接
    db_setting = {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'password': '123456',
        'database': 'blog_db',
        'charset': 'utf8',
    }
    db = pymysql.connect(**db_setting)
    # 2. 创建游标
    cursor = db.cursor()
    return cursor


class IndexHandler(RequestHandler):

    def get(self, *args, **kwargs):
        self.render("login_index.html")


class LoginHandler(RequestHandler):

    def get(self, *args, **kwargs):
        self.render("login_index.html")

    def post(self, *args, **kwargs):
        username = self.get_body_argument('the_name', None)
        password = self.get_body_argument('the_pass', None)
        print("用户名", username, ", 用户密码", password)
        cursor = connect_to_db()
        # 3. 利用游标进行操作
        sql_query_user = "select user_id from tb_user where user_name = %s and user_pass = %s"
        password = own_md5.md5(password)
        param = (username, password)
        cursor.execute(sql_query_user, param)   # cursor.execute(sql_query_user % (username, password)) 这样容易被sql注入
        # 4. 获取查询结果
        result = cursor.fetchone()
        if result:
            print("获取%s用户ID:"% type(result), result)
            # 跳转到blog页面
            self.redirect('/blog?username='+username)
        else:
            # 跳转回登录界面
            self.redirect('/?msg=fail')
        cursor.close()


class RegistHandler(RequestHandler):

    def get(self, *args, **kwargs):
        self.render("regist_index.html")

    def post(self, *args, **kwargs):
        filename = str()
        the_name = self.get_body_argument("username")
        the_pass = self.get_body_argument("password")
        the_city = self.get_body_argument("usercity")
        if  not (the_name and the_pass and the_city):
            self.redirect("/regist?msg=fail")
            return

        if self.request.files:
            # {"userfile": [{"content-type": ..., "body":, ..., "filename": ...}, {...}, ...]
            the_file = self.request.files["userfile"]
            file = the_file[0]   # 只取值第一个上传的文件的字典
            filename = the_name + "_" + file["content_type"].replace("/", ".")   # 格式: 用户名_类型.后缀
            with open("./upload/%s"%filename, 'wb') as f:
                f.write(file["body"])

        # 将原始的password利用摘要算法md进行格式的转换
        the_pass = own_md5.md5(the_pass)

        param = (the_name, the_pass, the_city, filename)
        print("获取的将提交数据: ", param)
        sql_insert_new_user = "insert into tb_user(user_name, user_pass, user_city, user_avatar) value (%s, %s, %s, %s)"
        cursor = connect_to_db()
        try:
            cursor.execute(sql_insert_new_user, param)
            cursor.connection.commit()   # db.commit()
        except Exception as e:
            err = str(e)
            err_code = err.split(",")[0].split("(")[1]
            if err_code == '1062':
                print("注册信息重复")
            else:
                print("未知数据库错误.")
        finally:
            cursor.close()
        self.redirect("/login")


class BlogHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render("blog_index.html")


class LoginModule(UIModule):
    """模型方法是传递给模板的, 其将在模板中运行"""

    def render(self, *args, **kwargs):
        msg = self.request.query
        if msg:
            msg = "用户名或密码错误"

        print(self.request)
        print("  └request.uri的值:", self.request.uri)   # uri=路径+get参数
        print("  └request.path的值:", self.request.path)   # 路径
        print("  └request.query的值:", self.request.query)   # get参数

        return self.render_string("the_module/login_module.html", result=msg)


class RegistModule(UIModule):

    def render(self, *args, **kwargs):
        msg = self.request.query
        if msg:
            msg = "用户名, 密码, 城市都不能为空."

        cursor = connect_to_db()
        sql_query_city = "select user_city from tb_user"
        cursor.execute(sql_query_city)
        cities = cursor.fetchall()
        cursor.close()

        return self.render_string("the_module/regist_module.html", cities=cities, msg=msg)



class BlogModule(UIModule):
    """模型方法是传递给模块的, 其将在模板中运行"""

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


# parse_config_file('../config/config')
# define('duankou',type=int,default=8888)
app = Application(handlers=[('/', IndexHandler),
                            ('/login', LoginHandler),
                            ('/blog', BlogHandler),
                            ('/regist', RegistHandler),
                            ],
                  template_path="./the_template",   # 配置template地址
                  static_path="./the_statics",   # 配置静态资源
                  ui_modules={"login_module": LoginModule, "regist_module": RegistModule, "blog_module": BlogModule},   # 配置module文件, 匹配在模块中的login_module()
                  )
server = HTTPServer(app)
server.listen(8000)
IOLoop.current().start()
