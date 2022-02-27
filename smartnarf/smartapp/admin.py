from django.contrib import admin
from .models import  Teacher, Group, Lesson, Discipline, SubGroup, Homework, Comment

# Register your models here.
#admin.site.register(User)
admin.site.register(Teacher)
admin.site.register(Group)
admin.site.register(Lesson)
admin.site.register(Discipline)
admin.site.register(SubGroup)
admin.site.register(Homework)
admin.site.register(Comment)
