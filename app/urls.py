from django.urls import include, re_path
from django.conf import settings
from django.conf.urls.static import static
from .views import homePage, redirectToDashboard, Dashboard


urlpatterns = [
    re_path(r'^$', homePage, name='home_page'),
    re_path(r'^adminpanel/$', redirectToDashboard),
    re_path(r'^adminpanel/auth/', include("user.urls")),
    re_path(r'^adminpanel/dashboard/', Dashboard.as_view(), name="dashboard"),
    re_path(r'^adminpanel/provinces/', include("Province.urls")),
    re_path(r'^adminpanel/district/', include("district.urls")),
    re_path(r'^adminpanel/city/', include("city.urls")),
    re_path(r'^api/', include("api.urls")),

] 


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'app.views.handle404'
handler500 = 'app.views.handle500'
