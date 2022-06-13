from django.shortcuts import render
from .forms import FormularioCliente
from .forms import FormularioTipodeTramite
from .forms import FormularioFechadeInicio
from .forms import FormularioDocumentacion
from .forms import FormularioPago






# Create your views here.

def clientes(request):
    
    formulario = FormularioCliente()
    contexto = {'formulario': formulario}
    return render(request, 'APPfinal/clientes.html', contexto)

    

def tipodeTramite(request):

    formulario = FormularioTipodeTramite()
    contexto = {'formulario': formulario}
    
    return render(request, 'APPfinal/tipodeTramite.html', contexto)

def FechadeInicio(request):
   
    formulario = FormularioFechadeInicio()
    contexto = {'formulario': formulario}
    return render(request, 'APPfinal/fechadeInicio.html', contexto)


def Documentacion(request):

    formulario = FormularioDocumentacion()
    contexto = {'formulario': formulario}
    
    return render(request,'APPfinal/documentacion.html', contexto)

def Pago(request):

    formulario = FormularioPago()
    contexto = {'formulario': formulario}

    return render(request,'APPfinal/pagos.html', contexto)

