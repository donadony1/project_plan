from django.urls import path
from .views import index,detail,list,propos,contact,recherche

urlpatterns = [
    path('', index,name='accueil'),
    path("detail/<id_plan>",detail,name='detail'),
    path('list',list,name='list'),
    path('propos',propos,name='propos'),
    path('contact',contact,name='contact'),
    path('recherche',recherche,name="recherche"),
]
