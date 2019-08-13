from django.urls import re_path
from .import views


app_name = "city"

urlpatterns = [
    re_path(r'^$', views.ListCity.as_view(), name="home"),
    re_path(r'^create/$', views.CreateCity.as_view(), name="create"),
]
