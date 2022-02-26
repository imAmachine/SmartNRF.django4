from django.shortcuts import render
from django.urls import include, path
from .models import *
#from .forms import UserRegisterForm


def index(request):
    torrents = Lesson.objects.all()
    return render(request, 'smartapp/index.html', {'title': 'Главная страница', 'content': torrents})


def register(request):
    #form = UserRegisterForm()
    return render(request, 'smartapp/register.html')
