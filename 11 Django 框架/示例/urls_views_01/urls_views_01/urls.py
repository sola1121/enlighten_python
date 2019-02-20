"""urls_views_01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

# 导入视图, 用于处理请求
from .views import run, run_args, run_kwargs

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^run/$", run),
    url(r"^run/(\d{2})/$", run_args),   # 使用子组位置传参
    url(r"^run_kwargs/", run_kwargs, kwargs={"name": "siro", "age": "1"}),   # 使用字典传参
]
