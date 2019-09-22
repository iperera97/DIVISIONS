from django.urls import include, re_path
from .views import Dashboard

app_name = "dashboard"

urlpatterns = [
    re_path(r"^$", Dashboard.as_view(), name="home")
]
