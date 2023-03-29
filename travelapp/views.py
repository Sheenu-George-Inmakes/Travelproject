from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, People

# Create your views here.


def demo(request):
    obj=Place.objects.all()
    obj2 = People.objects.all()
    return render(request, "index.html",{'result':obj, 'details':obj2})


def contacts(request):
    return render(request, "contact.html")


def destinations(request):
    return render(request, "destinations.html")


def news(request):
    return render(request, "news.html")


def elements(request):
    return render(request, "elements.html")