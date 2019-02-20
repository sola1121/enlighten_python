# 在主目录中的自建视图, 完成处理了请求request, 并返回响应response

from django.http import HttpResponse

# 编写视图处理函数, 一个函数相当于一个视图
def run(request):
    # request主要封装的是请求信息, 这里的request可自定义的变量名
    return HttpResponse("<h2>探究urls和views的关系</h2>")

def run_args(request, num):
    return HttpResponse("<h3>传入的数据是: %s</h3>" % num)

def run_kwargs(request, name, age):
    return HttpResponse("<h3>传入字典 name: %s age: %s</h3>" % (name, age))