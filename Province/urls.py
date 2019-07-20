from django.urls import re_path, path
from .import views

app_name = "provinces"

urlpatterns = [
    re_path(r"^$",
            views.ViewProvinces.as_view(),
            name="home"),

    re_path(r"^edit/(?P<pk>\d+)/",
            views.EditProvinces.as_view(),
            name="edit"),

    re_path(r"^create/",
            views.Create.as_view(),
            name="create"),

    re_path(r"^remove/(?P<pk>\d+)/",
            views.RemoveProvince.as_view(),
            name="remove"),
]
