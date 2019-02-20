from django.conf.urls import url
from .views import index_music

urlpatterns = [
    url(r"", index_music),    
    url(r"index/$", index_music),
]