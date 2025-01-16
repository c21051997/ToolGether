from django.shortcuts import render
from django.views.generic import ListView, DetailView
from Web_Main.models import category, slider, Item

# Create your views here.

def Home(request):
    categorydata = category.objects.all()
    sliderdata = slider.objects.all()
    itemdata = Item.objects.all()
    if itemdata.count() > 6:
        itemdata = itemdata[:]
    context = {
        'category': categorydata,
        'slider': sliderdata,
        'items': itemdata,
    }
    return render(request, 'Web_Main/index.html', context)

def About(request):
    return render(request, 'Web_Main/about.html')

def Credits(request):
    return render(request, 'Web_Main/credits.html')

def ItemPage(request):
    return render(request, 'Web_Main/item.html')

def Search(request):
    itemdata = Item.objects.all()
    context = {

        'c': itemdata,
    }
    return render(request, 'Web_Main/search.html', context)
