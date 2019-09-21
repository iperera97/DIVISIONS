from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from Province.models import Province
from district.models import District
from city.models import City


class Dashboard(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):

        parseData = {
            "title": "DASHBOARD",
            "pageTitle": "DASHBOARD",
            'province_count': Province.objects.all().count(),
            'district_count': District.objects.all().count(),
            'city_count': City.objects.all().count()
        }

        return render(request, "dashboard/home.html", parseData)
