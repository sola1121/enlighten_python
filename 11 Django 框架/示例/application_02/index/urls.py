from django.conf.urls import url
from .views import index_view, index_template2, variable_tem2, tag_tem, parent_view, child_view

urlpatterns = [
    url(r"^$", index_view),   # 2. 从主目录中的urls路由获得分发到的请求, 将其传递给本应用的视图处理
    url(r"index_template/$", index_template2),
    url(r"variable_template/$", variable_tem2),
    url(r"tag_template/$", tag_tem),

    url(r"parent/$", parent_view),
    url(r"child/$", child_view),

]
