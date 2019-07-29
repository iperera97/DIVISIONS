from django.shortcuts import render, redirect
from django.views import View
from .forms import DistrictInitForm
from django.contrib import messages


# view all districts
class ViewDistrct(View):

    def get(self, request):

        parseData = {
            'title': 'District'
        }

        return render(request, "district/home.html", parseData)


# create a new district
class CreateDistrict(View):

    def get(self, request):

        parseData = {
            'title': 'Create District',
            'form': DistrictInitForm()
        }

        return render(request, "district/create.html", parseData)

    def post(self, request):

        parseData = {
            'title': 'Create District',
        }

        # requset form data and init form
        form = DistrictInitForm(request.POST)

        if form.is_valid():

            form.save()
            messages.success(request, "New District added ")

            return redirect("district:home")

        parseData['form'] = form
        return render(request, "district/create.html", parseData)
