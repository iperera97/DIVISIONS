from django.shortcuts import render, reverse, get_object_or_404
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Province
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .forms import ProvinceForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


class CreateProvince(LoginRequiredMixin, SuccessMessageMixin, CreateView):

    model = Province
    form_class = ProvinceForm
    success_message = "%(englishName)s Province was created successfully"
    template_name = "Province/create_province.html"

    def get_context_data(self, *args, **kwargs):

        context = super().get_context_data(*args, **kwargs)
        context["title"] = "Create Province"

        return context

    def get_success_url(self, *args, **kwargs):
        return reverse("provinces:home")


class ViewProvinces(LoginRequiredMixin, ListView):

    model = Province

    def get_context_data(self, *args, **kwargs):

        context = super().get_context_data(*args, **kwargs)
        context["title"] = "Province"

        return context

    def get_queryset(self, *args, **kwargs):

        return super().get_queryset().values("id",
                                             "sinhalaName",
                                             "englishName",
                                             "tamilName",)


class EditProvinces(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = Province
    form_class = ProvinceForm
    template_name = "Province/edit_province.html"
    success_message = "%(englishName)s Province was created successfully"

    def get_context_data(self, *args, **kwargs):

        context = super().get_context_data(*args, **kwargs)
        context["title"] = "Update {} Province".format(
            self.instance.englishName)
        context['imageURL'] = self.instance.featureImage

        return context

    def get_object(self):

        PK = self.kwargs.get("pk")
        self.instance = get_object_or_404(Province, pk=PK)
        return self.instance


class RemoveProvince(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):

        PK = kwargs.get("pk")
        province = get_object_or_404(Province, pk=PK)
        response = province.delete()

        # if delete count is 1 or more => success
        if response[0] >= 1:
            messages.add_message(
                request, messages.SUCCESS, '{} province removed'.format(province.englishName))
        else:
            messages.add_message(
                request, messages.ERROR, '{} province not removed'.format(province.englishName))

        return redirect("provinces:home")
