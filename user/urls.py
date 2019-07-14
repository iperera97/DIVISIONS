from django.urls import re_path
from .import views

app_name = "user"

urlpatterns = [
    re_path(r'^login/$', views.LoginUser.as_view(), name="login"),
    re_path(r'^create/$', views.CreateUser.as_view(), name="create")
]
