from django.shortcuts import render, reverse
from django.views import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Province
from django.views.generic import CreateView, ListView, UpdateView
from .forms import ProvinceForm
from django.contrib.messages.views import SuccessMessageMixin


class Create(LoginRequiredMixin, SuccessMessageMixin, CreateView):

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

        pk = self.kwargs.get("pk")
        self.instance = Province.objects.get(pk=pk)
        return self.instance
