from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import * 
from .forms import *

# Create your views here.
def login_views(request):
    if request.method == "GET":
        form = UserFrom()
        dic_para = {"form": form}        
        cookies = request.COOKIES
        if "id" in cookies and "uphone" in cookies:
            return HttpResponse("欢迎" + cookies["uphone"] + "回来")
        else:
            return render(request, "login.html", dic_para)
    if request.method == "POST":
        form = UserFrom(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            uphone = data["uphone"]
            upwd = data["upwd"]
            user = Users.objects.filter(uphone=uphone, upwd=upwd)
            if user:
                if data.get("isSaved", False):
                    resp = HttpResponse("登陆成功")
                    resp.set_cookie("uphone", data["uphone"], 60*60*24*7)
                    resp.set_cookie("user_id", user[0], 60*60*24*7)
                    return resp
            else:
                return HttpResponse("登录失败")
        else:
            return HttpResponse("登录失败")


def register_views(request):
    if request.method == "GET":
        return render(request, "register.html")
    elif request.method == "POST":
        uphone = request.POST.get("uphone")
        isExsist = Users.objects.filter(uphone=uphone)   # 使用get没有数据将会报错
        if isExsist:
            errMsg = "用户已存在"
            return render(request, "register.html", locals())
        else:
            upwd = request.POST.get("upwd")
            uemail = request.POST.get("uemail")
            uname = request.POST.get("uname")
            Users.objects.create(uphone=uphone, upwd=upwd, uemail=uemail, uname=uname)
            return HttpResponse("注册成功")

