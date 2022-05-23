from multiprocessing import context
from re import template
from django.shortcuts import render
from . models import Image,Categorie,Plan

# Create your views here.

def index(request):
    plans= Plan.objects.all()[:8]
    context={
        'plans':plans,
    }
    return render(request,'index.html',context)