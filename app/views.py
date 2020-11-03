from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from Province.models import Province
from district.models import District
from city.models import City


def homePage(request):
    return render(request, 'home/home.html')


class Dashboard(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):

        parseData = {
            "title": "DASHBOARD",
            "pageTitle": "DASHBOARD",
            'province_count': Province.objects.all().count(),
            'district_count': District.objects.all().count(),
            'city_count': City.objects.all().count()
        }

        return render(request, "admin/dashboard.html", parseData)


def redirectToDashboard(request):
    return redirect('dashboard')


def handle404(request, *args, **kwargs):
    return render(request, 'errpages/404.html', status=404)


def handle500(request, *args, **kwargs):
    return render(request, 'errpages/500.html', status=500)

