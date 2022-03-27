from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('register', register_request, name='register'),
    # path('timesheet/', SheduleTable.as_view(), name='shedule-table-view')
    path('lk', lk_request, name='lk'),
]
