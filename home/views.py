from django.shortcuts import render
from .models import LostItem, FoundItem


def index(request):
    return render(request, 'index.html')

def lost(request, *args, **kwargs):
    items = LostItem.objects.all()
    ctx = {'items': items}
    return render(request, 'lost.html', ctx)

def found(request):
    return render(request, 'found.html')

def about(request):
    return render(request, 'about.html')

def lost_item(request):
    return render(request, 'lost_item.html')