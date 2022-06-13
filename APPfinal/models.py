from django.db import models
from django.utils import timezone

# Create your models here.
class ModeloCliente(models.Model):

    nombre = models.CharField(max_length=40, null=False)
    apellido = models.CharField(max_length=40, null=False)
    email = models.EmailField(null=False)

    def __str__(self) -> str:
        return self.nombre + " " + self.apellido


class ModeloTipodeTramite(models.Model):

    tramite = models.CharField(max_length=40, null=False)
    fechainicio = models.DateField(null=False)

    def __str__(self) -> str:
        return self.tramite + " " + self.fechainicio

class ModeloFechadeInicio(models.Model):

    dia = models.CharField(max_length=40, null=False)
    mes = models.CharField(max_length=40, null=False)
    año = models.EmailField(null=False)

    def __str__(self) -> str:
        return self.dia + " " + self.mes + " " + self.año

class ModeloDocumentacion(models.Model):

    documento = models.CharField(max_length=40, null=False)
    def __str__(self) -> str:
        return self.documento + " " 


class ModeloPago(models.Model):

    metododepago = models.CharField(max_length=40, null=False)
    pagado = models.BooleanField(null=False)
    
    def __str__(self) -> str:
        return self.metododepago + " " + self.pagado