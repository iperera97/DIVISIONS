from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.http import HttpResponse
from django.conf.urls.static import static

urlpatterns = [

    path('admin/', admin.site.urls),
    re_path(r'^adminpanel/auth/', include("user.urls")),
    re_path(r'^adminpanel/dashboard/', include("dashboard.urls")),
    re_path(r'^adminpanel/provinces/', include("Province.urls")),
    re_path(r'^adminpanel/district/', include("district.urls")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [

        path('__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
