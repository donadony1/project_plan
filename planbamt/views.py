from multiprocessing import context
from re import template
from django.shortcuts import render
from . models import Image,Categorie,Plan
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

# Create your views here.

def index(request):
    plans= Plan.objects.all()[:6]
    context={
        'plan':plans,
    }
    return render(request,'pages/index.html',context)

def list(request):
    plans=Plan.objects.all()
    paginator=Paginator(plans,6)
    num_page=request.GET.get('page')

    try:
        plans=paginator.page(num_page)

    except PageNotAnInteger:

        plans=paginator.page('1')

    except EmptyPage:
        plans=paginator.page(paginator.num_pages)

    context={
        'plan':plans,
        'paginator':True,
    }
    return render(request,'pages/list.html',context)

def detail(request, id_plan):
    plan=Plan.objects.get(pk=id_plan)
    context={
        'description':plan.description,
        'titre':plan.titre,
        'prix':plan.prix,
        'image':plan.image
    }
    return render(request,'pages/detail.html',context)

def propos(request):
    return render(request,'pages/propos.html')

def contact(request):
    return render(request,'pages/contact.html')

def recherche(request):
    query=request.GET.get('query')
    if not query:
        plans=Plan.objects.all()
    else:
        plans=Plan.objects.filter(titre__icontains=query)
        if not plans.exists():
            plans=Plan.objects.filter(Categorie__nom__icontains=query)

    titre="les resultats de le recherche '%s' sont: "%query 
    context={
        'plan':plans,
        'list_titre':titre
    }
    return render(request,'pages/recherche.html',context)