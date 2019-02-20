from django.conf.urls import url

from .views import index_sport

urlpatterns = [
    url(r"", index_sport),
    url(r"index/$", index_sport)
]