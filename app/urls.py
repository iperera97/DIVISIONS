from django.contrib import admin
from django.urls import path, include, re_path, reverse
from django.conf import settings
from django.conf.urls.static import static
from .views import homePage, redirectToDashboard


urlpatterns = [
    re_path(r'^$', homePage, name='home_page'),
    re_path(r'^adminpanel/$', redirectToDashboard),
    re_path(r'^adminpanel/auth/', include("user.urls")),
    re_path(r'^adminpanel/dashboard/', include("dashboard.urls")),
    re_path(r'^adminpanel/provinces/', include("Province.urls")),
    re_path(r'^adminpanel/district/', include("district.urls")),
    re_path(r'^adminpanel/city/', include("city.urls")),
    re_path(r'^api/', include("api.urls")),

] 


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [

        path('__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns

handler404 = 'app.views.handle404'
handler500 = 'app.views.handle500'
