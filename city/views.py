from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import City
from .forms import CityInitForm
from django.contrib import messages


# create city with model form
class CreateCity(LoginRequiredMixin, View):

    TEMPLATE_NAME = "city/create.html"

    # init form
    def get(self, request, *args, **kwargs):

        form = CityInitForm()

        parseData = {
            'title': 'Create City',
            'form': form
        }

        return render(request, self.TEMPLATE_NAME, parseData)

    # pass form data to database and redirect
    def post(self, request, *args, **kwargs):

        form = CityInitForm(request.POST, request.FILES)

        # if form is valid
        if form.is_valid():

            # save db
            form.save()

            # flash messages
            messages.success(request, " {} City Added ".format(
                request.POST.get("englishName")))

            return redirect("city:home")

        parseData = {
            'title': 'Create City',
            'form': form
        }

        return render(request, self.TEMPLATE_NAME, parseData)


# update city data through model form
class UpdateCity(LoginRequiredMixin, View):

    TEMPLATE_NAME = "city/edit.html"

    # get relevent object details
    # bound model form
    def get(self, request, *args, **kwargs):

        city = get_object_or_404(City, pk=kwargs.get('pk'))
        form = CityInitForm(instance=city)

        parseData = {
            'title': 'Update {}'.format(city.englishName),
            'form': form
        }

        return render(request, self.TEMPLATE_NAME, parseData)

    def post(self, request, *args, **kwargs):

        city = get_object_or_404(City, pk=kwargs.get('pk'))
        form = CityInitForm(request.POST, instance=city)

        parseData = {
            'form': form,
            'title': 'Update {}'.format(city.englishName)
        }

        if form.is_valid():
            # save record
            form.save()

            messages.success(request, " {} City Added ".format(
                request.POST.get("englishName")))

            return redirect("city:home")

        else:
            return render(request, self.TEMPLATE_NAME, parseData)


class RemoveCity(LoginRequiredMixin, View):
    pass


class ListCity(LoginRequiredMixin, ListView):

    queryset = City.objects.all()
    queryset = queryset.select_related('district')
    queryset = queryset.values(
        'pk',
        'sinhalaName',
        'englishName',
        'district_id',
        'district__englishName')

    template_name = "city/list.html"

    def get_context_data(self, *args, **kwargs):
        contextData = super().get_context_data(*args, **kwargs)
        contextData['title'] = 'City'
        return contextData
