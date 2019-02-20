from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import *
from .forms import *

# Create your views here.

def request_view(request):
    # return HttpResponse(str(dir(request)))
    request_type = type(request)
    scheme = request.scheme
    print(type(request.scheme))
    body = request.body
    print(type(request.body))
    host = request.get_host()
    print(type(request.get_host()))
    path = request.path 
    print(type(request.path))
    method = request.method 
    print(type(request.method))
    get = request.GET 
    print(type(request.GET))
    post = request.POST 
    print(type(request.POST))
    cookies = request.COOKIES 
    print(type(request.COOKIES))
    return render(request, "01_request.html", locals())

def login_view(request):
    if request.method == "GET":
        return render(request, "02_login.html")
    elif request.method == "POST":
        uname = request.POST["uname"]
        upwd = request.POST["upwd"]
        return HttpResponse(str(uname) + "<br>" + str(upwd))

def get_view(request):
    # if "uname" in request.GET:
    #     uname = request.GET["uname"]
    # if "upwd" in request.GET:
    #     upwd = request.GET["upwd"]

    uname = request.GET.get("uname")
    upwd = request.GET.get("upwd")

    if uname and upwd:
        return HttpResponse(str(uname) + "<br>" + str(upwd))
    else:
        return render(request, "03_login_get.html")
    
def query_view(request):
    id = request.GET.get("id", "")
    name = request.GET.get("name", "")

    return HttpResponse(str(id) + "<br>" + str(name))


def form_view(request):
    if request.method == "GET":
        form = RemarkForm()
        return render(request, "04_form.html", locals())
    elif request.method == "POST":
        # 1. 将request.POST中的数据交给RemarkForm
        form = RemarkForm(request.POST)
        # 2. 验证数据是否都符合规范
        if form.is_valid():
            # 3. 通过验证后, 在通过cleaned_data取值
            cd = form.cleaned_data
            return HttpResponse(cd["subject"] + "<br>" +cd["email"])


def register_form_view(request):
    if request.method == "GET":
        form_object = RegisterForm()
        return render(request, "05_register.html", locals())
    elif request.method == "POST":
        form_object = RegisterForm(request.POST)
        if form_object.is_valid():
            data = form_object.cleaned_data
            try:
                Users.objects.create(uname=data["uname"], upwd=data["upwd"], uemail=data["uemail"], uage=data["uage"])
                # users = Users(**data)
                # users.save()
                return HttpResponse("注册成功")
            except Exception as e:
                return HttpResponse(str(e))


def model_form_view(request):
    if request.method == "GET":
        form_object = LoginForm()
        return render(request, "06_form_login.html", locals())
    elif request.method == "POST":
        pass

def add_cookie_view(request):
    # 不使用模板
    # resp = HttpResponse("添加cookie成功")
    # resp.set_cookie("uname", "hinata", 60*60*24)
    # return resp

    # 使用模板
    resp = render(request, "07_set_cookies.html", locals())
    resp.set_cookie("uname2", "nekomiya", 60*60*24)
    return resp


def get_cookie_view(request):
    cookies = request.COOKIES
    print(cookies)
    return HttpResponse("get cookies ok.")


def set_session_view(request):
    uname = "hinata"
    uemail = "hinata@youtu.com"
    # 将以上两个数据保存进session
    request.session["uname"] = uname
    request.session["uemail"] = uemail
    return HttpResponse("session set seccess.")

def get_session_view(request):
    uname = request.session.get("uname")
    uemail = request.session["uemail"]
    return HttpResponse("session" + "   " + str(uname) + "   " + str(uemail))