from django.shortcuts import render
from django.urls import include, path
from .models import *


def index(request):
    torrents = Torrent.objects.all()
    return render(request, 'smartapp/index.html', {'title': 'Главная страница', 'content': torrents})
