from django.urls import re_path
from .import views

app_name = "district"

urlpatterns = [
    re_path(r'^$',
            views.ViewDistrct.as_view(),
            name="home"),

    re_path(r'^create/',
            views.CreateDistrict.as_view(),
            name="create"),

    re_path(r'^edit/(?P<pk>\d+)/',
            views.EditDistrict.as_view(),
            name="edit"),

    re_path(r'^remove/(?P<pk>\d+)/',
            views.RemoveDistrict.as_view(),
            name="delete")
]
