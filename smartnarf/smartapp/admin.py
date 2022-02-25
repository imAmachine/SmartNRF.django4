from django.contrib import admin
from .models import User, Teacher, Group, Torrent, Discipline

# Register your models here.
admin.site.register(User)
admin.site.register(Teacher)
admin.site.register(Group)
admin.site.register(Torrent)
admin.site.register(Discipline)
