from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import City
from .forms import CityInitForm
from django.contrib import messages


class CreateCity(LoginRequiredMixin, View):

    TEMPLATE_NAME = "city/create.html"

    def get(self, request, *args, **kwargs):

        form = CityInitForm()

        parseData = {
            'title': 'Create City',
            'form': form
        }

        return render(request, self.TEMPLATE_NAME, parseData)

    def post(self, request, *args, **kwargs):

        form = CityInitForm(request.POST)

        # if form is valid
        if form.is_valid():

            form.save()

            messages.success(request, " {} City Added ".format(
                request.POST.get("englishName")))

            return redirect("city:home")

        parseData = {
            'title': 'Create City',
            'form': form
        }

        return render(request, self.TEMPLATE_NAME, parseData)


class UpdateCity(LoginRequiredMixin, View):

    TEMPLATE_NAME = "city/edit.html"

    def get(self, request, *args, **kwargs):

        return render(request, self.TEMPLATE_NAME)

    def post(self, request, *args, **kwargs):
        pass


class RemoveCity(LoginRequiredMixin, View):
    pass


class ListCity(LoginRequiredMixin, ListView):

    queryset = City.objects.all()
    template_name = "city/list.html"

    def get_context_data(self, *args, **kwargs):
        contextData = super().get_context_data(*args, **kwargs)
        contextData['title'] = 'City'
        return contextData
