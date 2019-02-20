from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index_music(request):
    return HttpResponse("<h3>这是在music中的index</h3>")