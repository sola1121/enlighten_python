from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader

# Create your views here.

# 3. 该应用的视图, 出里请求
def index_view(request):
    return HttpResponse("<h3>这是在index应用中的</h3>")


def index_template(request):
    te = loader.get_template("index.html")
    html_text = te.render()
    return HttpResponse(html_text)

def index_template2(request):
    # 这是index_template的快捷封装
    return render(request, "index.html")

def variable_tem(request):
    dic = {"name": "siro", "age": 1, "alias": ["iruka", "xiaobai", "warAI"]}
    te = loader.get_template("variable.html")
    html_text = te.render()
    return HttpResponse(html_text)

def variable_tem2(request):
    dic = {"name": "siro", "age": 1, "alias": ["iruka", "xiaobai", "warAI"]}
    return render(request, "variable.html", dic)    # 也可以使用locals生成当前局部变量的字典

def tag_tem(request):
    names = ["siro", "kizuna_ai", "luna", "hinata", "akari", "yomemi", "nojialoli"]
    return render(request, "tag.html", locals())


# 父子模板
def parent_view(request):
    return render(request, "t_parent.html")
def child_view(request):
    return render(request, "t_child.html")
