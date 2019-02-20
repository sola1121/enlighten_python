from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def index_sport(requset):
    return HttpResponse("<h3>这是在sport中的index</h3>")