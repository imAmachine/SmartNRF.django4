from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    # path('timesheet/', SheduleTable.as_view(), name='shedule-table-view')
]
