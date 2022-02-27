from django.http import JsonResponse
from django.shortcuts import render
from django.urls import include, path
from django.views import View
from django.views.generic import TemplateView
from .models import *

import datetime


class IndexView(TemplateView):
    template_name = 'smartapp/index.html'
    # torrents = Lesson.objects.all()
    # return render(request, 'smartapp/index.html', {'title': 'Главная страница', 'content': torrents})

    # def get_context_data(self, **kwargs):
    # context = super(IndexView, self).get_context_data(**kwargs)
    # context['asd'] = '213'
    # context['dataFront'] = Lesson.objects.filter(datetime__in='2022-02-27')
    # return context

    def get(self, request, *args, **kwargs):

        cur_btn = request.GET.get('cur_btn', datetime.datetime.today().weekday())
        context = {
            'cur_btn': cur_btn,
            'dataFront': Lesson.objects.filter(datetime__week_day=int(cur_btn)+2)
        }

        # cur_btn = datetime.datetime.today().weekday()

        # if request.GET:

        return render(request, self.template_name, context)



# def register(request):
#     return render(request, 'smartapp/register.html')


# class SheduleTable(View):
#     def get(self, *args, **kwargs):
#         lessons = list(Lesson.objects.values())
#         return JsonResponse({'data': lessons}, safe=True)

