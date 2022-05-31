from datetime import datetime
from email.mime import image
from ipaddress import ip_address
from tkinter.tix import Tree
from venv import create
from django.db import models

# Create your models here.

class Image(models.Model):
    create_at = models.DateTimeField(auto_now=True)
    nom = models.CharField(max_length=300)
    image = models.ImageField(upload_to='image_publie', blank=True, null=True)

    class Meta:
        ordering=['-create_at']
        verbose_name = 'image'
        verbose_name_plural = 'images'

    def __str__(self):
        return self .nom

class Categorie(models.Model):
    create_at = models.DateTimeField(auto_now=True)
    nom = models.CharField(max_length=20,unique=True, default='maison')
    
    class Meta:
        verbose_name = 'categorie'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self .nom

class Plan(models.Model):
    create_at = models.DateTimeField(auto_now=True)
    titre = models.CharField(max_length=500)
    description = models.TextField()
    prix = models.IntegerField()
    image = models.ManyToManyField(Image, related_name='plan', blank=True)
    Categorie = models.ForeignKey(Categorie, related_name='caterogie', on_delete=models.CASCADE)

    class Meta:
        ordering=['-create_at']
        verbose_name = 'les Plans de batiment'
        verbose_name_plural = 'les Plans de batiments'

    def __str__(self):
        return self.titre

class Visitor_Infos(models.Model):
    ip_address=models.GenericIPAddressField()
    page_visited=models.TextField()
    event_date=models.DateTimeField(default=datetime.now)


