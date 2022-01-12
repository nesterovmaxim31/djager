from django.shortcuts import render
from django.http import HttpResponse
from .models import Listproblems, List, List5
from django.views.generic import ListView, DetailView

def index(response):
    return render(response, "general.html")

def acmp(response):
    res = Listproblems.objects.all()
    print({"Listproblems": res})
    return render(response, "ht1.html", {"Listproblems" : res})

def problems(response):
    res = List.objects.all()
    return render(response, "listproblems.html", {"List" : res})

def problems2(response):
    res = List5.objects.all()
    return render(response, "listproblems2.html", {"List5" : res})

class D(DetailView):
    model = List5
    template_name = "iter_2.html"
    context_object_name = 'tesla'
