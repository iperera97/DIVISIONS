from django.urls import re_path
from .import views

app_name = "api"

urlpatterns = [
    re_path('^province/list/$',
            views.GetProvinces.as_view(),
            name='list-province'),

    re_path('^district/list/$',
            views.GetDistrict.as_view(),
            name='list-district'),


    re_path('^city/list/$',
            views.GetCity.as_view(),
            name='list-city')
]
