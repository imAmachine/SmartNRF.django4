from django.http import JsonResponse
from django.shortcuts import render
from django.urls import include, path
from django.views import View
from django.views.generic import TemplateView
from .models import *
from django.db.models import Q

from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

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


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			#login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="smartapp/register.html", context={"register_form":form})