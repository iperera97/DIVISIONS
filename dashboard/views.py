from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class Dashboard(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):

        parseData = {
            "title": "DASHBOARD",
            "pageTitle": "DASHBOARD"
        }

        return render(request, "dashboard/home.html", parseData)
