from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


class LoginUser(View):

    def get(self, request, *args, **kwargs):

        return render(request, 'admin/base.html')


class CreateUser(View):

    def get(self, request, *args, **kwargs):

        return HttpResponse("Create page")
