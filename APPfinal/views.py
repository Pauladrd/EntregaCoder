from django.shortcuts import render
from .forms import FormularioCliente
from .forms import FormularioTramite
from .forms import FormularioFecha
from .forms import FormularioDocumentacion
from .forms import FormularioPago
from django.template import loader






# Create your views here.

def clientes(request):
    if request.method == 'POST':
    
    miFormulario = FormularioCliente(request.POST)
    print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            cliente = ModeloCliente(nombre = informacion['nombre'], apellido = informacion['apellido'])

            cliente.save()

            return render(request, APPfinal/clientes.html)

        else:
            miFormulario = FormularioCliente()
        return render(request, 'APPfinal/clientes.html', {miFormulario':miFormulario})


    

def Tramite(request):

   miFormulario = FormularioTramite(request.POST)
    print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            tramite = ModeloTramite(nombre = informacion['nombre'], documento = informacion['documento'])

            tramite.save()

            return render(request, APPfinal/Tramite.html)

        else:
            miFormulario = FormularioTramite()
        return render(request, 'APPfinal/Tramite.html', {miFormulario':miFormulario})
        


def Fecha(request):
   
    miFormulario = FormularioFecha(request.POST)
    print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            fecha = ModeloFecha(mes = informacion['mes'], año = informacion['año'])

            fecha.save()

            return render(request, APPfinal/fecha.html)

        else:
            miFormulario = FormularioFecha()
        return render(request, 'APPfinal/fecha.html', {miFormulario':miFormulario})
        



def Documentacion(request):

    miFormulario = FormularioDocumentacion(request.POST)
    print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            documento = ModeloDocumento(documento = informacion['documento'], numero = informacion['numero'])

            documento.save()

            return render(request, APPfinal/documentacion.html)

        else:
            miFormulario = FormularioDocumentacion()
        return render(request, 'APPfinal/documentacion.html', {miFormulario':miFormulario})
        

def Pago(request):

    miFormulario = FormularioPago(request.POST)
    print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            pago = ModeloCliente(mediodepago = informacion['mediodepago'], total = informacion['total'])

            pago.save()

            return render(request, APPfinal/pagos.html)

        else:
            miFormulario = FormularioPago()
        return render(request, 'APPfinal/pagos.html', {miFormulario':miFormulario})
        


def index(self):
    index = loader.get_template('index.html')
    documento = index.render()



