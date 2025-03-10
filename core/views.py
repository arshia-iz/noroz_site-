from django.utils.timezone import now, make_aware
from datetime import datetime
from django.shortcuts import render

def home (request):
    return render(request, "core/home.html")

def about (request):
    return render (request, "core/about.html")