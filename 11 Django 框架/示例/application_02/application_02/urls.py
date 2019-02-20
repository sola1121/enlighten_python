"""application_02 URL Configuration

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
from django.conf.urls import url, include   # 导入include, 用于路由分发
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r"^", include("index.urls")),   # 啥也不写转到index应用
    url(r"^index/", include("index.urls")),   # 1. 将请求交给index应用中的urls路由处理(这是一个分路由)
    url(r"^music/", include("music.urls")),
    url(r"^sport/", include("sport.urls")),
]
