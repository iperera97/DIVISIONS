from django.urls import re_path
from .import views

app_name = "provinces"

urlpatterns = [
    re_path(r"^$", views.Home.as_view(), name="home"),
    re_path(r"^create/", views.Create.as_view(), name="create")
]
