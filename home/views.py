from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')

def lost(request):
    return render(request, 'lost.html')

def found(request):
    return render(request, 'found.html')