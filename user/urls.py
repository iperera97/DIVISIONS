from django.urls import re_path
from .import views
from django.contrib.auth.views import LoginView

app_name = "user"

urlpatterns = [
    re_path(r'^login/$',
            LoginView.as_view(template_name="user/login.html"),
            name="login"),
    re_path(r'^create/$', views.CreateUser.as_view(), name="create")
]
