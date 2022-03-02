from django.http import JsonResponse
from django.shortcuts import render
from django.urls import include, path
from django.views import View
from django.views.generic import TemplateView
from .models import *
from django.db.models import Q

import datetime


class IndexView(TemplateView):
    template_name = 'smartapp/index.html'

    def get(self, request, *args, **kwargs):
        date = datetime.datetime.today()
        cur_btn = request.GET.get('cur_btn', date.weekday())
        lessons = Lesson.objects.filter(Q(datetime__week_day=int(cur_btn) + 2)
                                        & Q(datetime__week=date.strftime("%V")))
        context = {
            'cur_btn': cur_btn,
            'dataFront': lessons
        }
        return render(request, self.template_name, context)



# def register(request):
#     return render(request, 'smartapp/register.html')