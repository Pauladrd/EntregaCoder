from pyexpat import model
from django import forms
from .models import ModeloCliente
from .models import ModeloTipodeTramite
from .models import ModeloFechadeInicio
from .models import ModeloDocumentacion
from .models import ModeloPago

class FormularioCliente(forms.ModelForm):
    class Meta: 
        model = ModeloCliente
        fields = '__all__'
        widgets = { 
            'nombre': forms.TextInput(attrs={'class': 'form-control col-md-8'}),


        }

class FormularioTipodeTramite(forms.ModelForm):
    class Meta: 
        model = ModeloTipodeTramite
        fields = '__all__'
        widgets = { 
            'nombre': forms.TextInput(attrs={'class': 'form-control col-md-8'}),
        }

class FormularioFechadeInicio(forms.ModelForm):
    class Meta: 
        model = ModeloFechadeInicio
        fields = '__all__'
        widgets = { 
            'nombre': forms.TextInput(attrs={'class': 'form-control col-md-8'}),
        }

class FormularioDocumentacion(forms.ModelForm):
    class Meta: 
        model = ModeloDocumentacion
        fields = '__all__'
        widgets = { 
            'nombre': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
        }


class FormularioPago(forms.ModelForm):
    class Meta: 
        model = ModeloPago
        fields = '__all__'
        widgets = { 
            'nombre': forms.TextInput(attrs={'class': 'form-control col-md-6'}),
        }
