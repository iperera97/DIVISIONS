from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import logout


def logoutUser(request):

    logout(request)
    return redirect('user:login')
