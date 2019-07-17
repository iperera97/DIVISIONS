from django.shortcuts import render, reverse
from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Province
from django.views.generic import CreateView
from .forms import ProvinceForm
from django.contrib.messages.views import SuccessMessageMixin


class Home(LoginRequiredMixin, View):

    def get(self, request):

        parseData = {
            "title": "Provinces",
        }

        return render(request, "Province/home.html", parseData)


class Create(LoginRequiredMixin, SuccessMessageMixin, CreateView):

    model = Province
    form_class = ProvinceForm
    success_message = "%(englishName)s Province was created successfully"

    def get_context_data(self, *args, **kwargs):

        context = super().get_context_data(*args, **kwargs)
        context["title"] = "Create Province"

        return context

    def get_success_url(self, *args, **kwargs):
        return reverse("provinces:home")
