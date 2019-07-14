from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.http import HttpResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^adminpanel/auth/', include("user.urls"))
]
