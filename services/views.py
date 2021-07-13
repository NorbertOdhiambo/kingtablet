from django.shortcuts import render
from .models import *


def index(request):
    services = Service.objects.all()
    context = {'services': services}
    return render(request, 'index.html', context)


def comp(request):
    return render(request, 'comp_info.html')


def internet(request):
    return render(request, 'internet_serve.html')


def screens(request):
    return render(request, 'screens.html')


def assign(request):
    return render(request, 'assign.html')
