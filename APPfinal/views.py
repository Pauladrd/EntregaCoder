from django.shortcuts import render
from django import forms
from django.template import loader
from datetime import datetime
from pipes import Template
from django.http import HttpResponse
from django.template import Template, Context






# Create your views here.

def clientes(request):
    
    
    return render(request, 'APPfinal/clientes.html')
    

def tipodeTramite(request):
    
    return render(request, 'APPfinal/tipodeTramite.html')

def fechadeInicio(request):
   
    return render(request, 'APPfinal/fechadeInicio.html')


def documentacion(request):
    documentoDeTexto = f"Ingresa el documento de Identidad: <br> (nombre)"
    
    return render(request,'APPfinal/documentacion.html')

def pago(request):

    return render(request,'APPfinal/pagos.html')

