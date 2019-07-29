from django.urls import re_path
from .import views

app_name = "district"

urlpatterns = [
    re_path(r'^$', views.ViewDistrct.as_view(), name="home"),
    re_path(r'^create/', views.CreateDistrict.as_view(), name="create")
]
