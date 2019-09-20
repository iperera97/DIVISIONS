from django.urls import re_path, path
from .import views

app_name = "api"

urlpatterns = [
    re_path(r'^province/list/$',
            views.ProvinceList.as_view(),
            name='list-province'),

    re_path(r'^province/relevet-districts/(?P<province_id>[0-9]+)/$',
            views.ReleventDistrict.as_view(),
            name='rel-districts'),

    re_path(r"province/(?P<id>[0-9]+)/$",
            views.ProvinceDetail.as_view(),
            name="detail-view"),

    re_path(r'^district/list/$',
            views.GetDistrict.as_view(),
            name='list-district'),

    re_path(r'^city/list/$',
            views.GetCity.as_view(),
            name='list-city'),



]
