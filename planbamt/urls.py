from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index,name='accueil'),
    path("detail/<id_plan>",views.detail,name='detail'),
    path('list',views.list,name='list'),
    path('propos',views.propos,name='propos'),
    path('contact',views.contact,name='contact'),
    path('recherche',views.recherche,name="recherche"),
    path('deconnexion',views.deconnexion,name="deconnexion"),
]
