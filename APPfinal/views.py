from random import choices
from django.shortcuts import render, redirect
from django.template import loader
from .forms import FormularioCliente, FormularioTramite, FormularioFecha, FormularioDocumentacion, FormularioPago 
from .models import ModeloCliente, ModeloDocumentacion, ModeloFecha, ModeloPago, ModeloTramite
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login, logout





# Create your views here.

def clientes(request):
    miFormulario = FormularioCliente()
    misClientes = ModeloCliente.objects.all()

    if request.method == 'POST':
    
        miFormulario = FormularioCliente(request.POST)
        print(miFormulario)


        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            cliente = ModeloCliente(nombre = informacion['nombre'], apellido = informacion['apellido'], email = informacion['email'])

            cliente.save()

            return render(request, 'APPfinal/clientes.html', {'formulario':miFormulario, 'clientes':misClientes})

    else:
        
        return render(request, 'APPfinal/clientes.html', {'formulario':miFormulario, 'clientes':misClientes})


    

def Tramite(request):
    data = {
            'form': ModeloTramite
    }

    if request.method == 'POST':
       
        miFormulario = FormularioTramite(request.POST)

        print(miFormulario)

        if miFormulario.is_valid():
            miFormulario.save()
            informacion = miFormulario.cleaned_data

            tramite = ModeloTramite(tramite = informacion['tramite'])

            tramite.save()

            return render(request, 'APPfinal/Tramite.html')

    
    else:
        miFormulario = FormularioTramite()
        return render(request, 'APPfinal/Tramite.html', {'formulario':miFormulario})
    


def Fecha(request):
    if request.method == 'POST':
   
        miFormulario = FormularioFecha(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            fecha = ModeloFecha(mes = informacion['mes'], a??o = informacion['a??o'])

            fecha.save()

            return render(request, 'APPfinal/fecha.html')

    else:
        miFormulario = FormularioFecha()
        return render(request, 'APPfinal/fecha.html', {'formulario':miFormulario})
    



def Documentacion(request):
    if request.method == 'POST':

        miFormulario = FormularioDocumentacion(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            documento = ModeloDocumentacion(documento = informacion['documento'], numero = informacion['numero'])

            documento.save()

            return render(request, 'APPfinal/documentacion.html')

    else:
        miFormulario = FormularioDocumentacion()
        return render(request, 'APPfinal/documentacion.html', {'formulario':miFormulario})
    

def Pago(request):
    if request.method == 'POST':

        miFormulario = FormularioPago(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            pago = ModeloPago(mediodepago = informacion['mediodepago'], total = informacion['total'])

            pago.save()

            return render(request, 'APPfinal/pagos.html')

    else:
        miFormulario = FormularioPago()
        return render(request, 'APPfinal/pagos.html', {'formulario':miFormulario})
    


def index(self):
    index = loader.get_template('index.html')
    documento = index.render()


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('Nombre')
    else:
        form = AuthenticationForm()

    return render(request, 'APPfinal/login.html', {'form':form})


def logout_view(request):
    logout(request)
    return redirect('Nombre')

def sobremi(request):
    return render(request,'APPfinal/sobremi.html')