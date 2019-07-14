from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.http import HttpResponse

urlpatterns = [
    path('admin/', admin.site.urls),
]
