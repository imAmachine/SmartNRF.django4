from django.http import JsonResponse
from django.shortcuts import render
from django.urls import include, path
from django.views import View
from django.views.generic import TemplateView
from .models import *


class IndexView(TemplateView):
    template_name = 'smartapp/index.html'
    # torrents = Lesson.objects.all()
    # return render(request, 'smartapp/index.html', {'title': 'Главная страница', 'content': torrents})



# def register(request):
#     return render(request, 'smartapp/register.html')


class SheduleTable(View):
    def get(self, *args, **kwargs):
        lessons = list(Lesson.objects.values())
        return JsonResponse({'data': lessons}, safe=False)

