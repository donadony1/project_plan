from multiprocessing import context
from re import template
from django.shortcuts import render,get_object_or_404,redirect
import pkg_resources
from . models import Image,Categorie,Plan,Visitor_Infos
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.conf import settings
from django.contrib.auth import login,authenticate,logout
from django.urls import reverse

from.form import signupForm, ConnexionForm
# Create your views here.



#------ new --------------------------#

def index(request):
    plans= Plan.objects.all()[:6]
    context={
        'plan':plans,
    }
    # if request.user.is_authenticated():
    #     contact['username']=request.user.username
    #     return render(request,'pages/index.html',locals())
    # else: 
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
    plan=get_object_or_404(Plan, pk=id_plan)
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
    form = signupForm()
    formConnex = ConnexionForm()
    error =False

    if request.method=="POST":
         # ----------parti inscription --------------#
        form = signupForm(request.POST)
        formConnex = ConnexionForm(request.POST)
        if form.is_valid():
            user=form.save()
            # --------auto-login user----------#
            login(request, user)
            # return redirect(settings.LOGIN.REDIRECT.URL)

         # ----------parti connexion --------------#
        if formConnex.is_valid():
            username=formConnex.cleaned_data['username']
            password = formConnex.cleaned_data['password']
            user= authenticate(username=username, password=password)
            if user:  # --------------si l'object user n'est pas vide
                login(request, user) #-------------- nous connecton
                return redirect(reverse(index))  #----------------------------redirige as la page d'accueil
            else:
                 error=True
    else:      
        context={
            'form':signupForm(),
            'formConnex':ConnexionForm(),
        }
    return render(request,'pages/contact.html',locals())

def deconnexion(request):
    logout(request)
    return redirect(reverse(index))  #----------------------------redirige as la page d'accueil

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

# def inscription(request):
#     return render(request,'pages/inscription.html')

