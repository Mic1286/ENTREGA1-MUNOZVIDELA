from ast import Pass
from operator import index
from django.shortcuts import render

from Proyecto_coder.apps import CelularesConfig
from.models import celulares
from django.template import loader
from django.http import HttpResponse

# Create your views here.

def crear (request):
    celular1= celulares(marca= "Samsung" , modelo= "S22", precio= "60000')
    celular2= celulares(marca= "Iphone" , modelo= "G4", precio= "130000' )
    
    celular1.save()
    celular2.save()
    
    return HttpResponse('Creado con exito')

def mostrar(request):
    
    info= CelularesConfig.objects.all()
    
    dicc={"celulares": info}
    
    index= loader.get_template ('index.html')
    
    documento= index.render(dicc)
    
    return HttpResponse(documento)