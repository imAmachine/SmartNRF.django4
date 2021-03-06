from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('api/', include('authentication.urls', namespace='authentication')),
    path('', include('smartapp.urls')),
]