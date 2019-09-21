from django.shortcuts import render, redirect


def homePage(request):
    return render(request, 'home/home.html')


def redirectToDashboard(request):
    return redirect('dashboard:home')


def handle404(request, *args, **kwargs):
    return render(request, 'errpages/404.html', status=404)


def handle500(request, *args, **kwargs):
    return render(request, 'errpages/500.html', status=500)
