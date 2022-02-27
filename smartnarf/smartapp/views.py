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

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['dataFront'] = list(Lesson.objects.all)
        return context

    def get(self, request, *args, **kwargs):
        cur_btn = datetime.datetime.today().weekday()

        if request.GET:
            cur_btn = request.GET.get('cur_btn')

        return render(request, self.template_name, {'cur_btn': cur_btn})



# def register(request):
#     return render(request, 'smartapp/register.html')


# class SheduleTable(View):
#     def get(self, *args, **kwargs):
#         lessons = list(Lesson.objects.values())
#         return JsonResponse({'data': lessons}, safe=True)

