from django.db import models
from django.utils import timezone

# Create your models here.
choices = [
    [1, 'Apostilla'],
    [2, 'Partidas'],
    [3, 'Residencia Uruguaya'],
    [4, 'Titulos de Estudio'],
    [5, 'DNI'],
    [6, 'Pasaporte'],
    [7, 'Turnos visados'],
    [8, 'Otro'],
 

]
class ModeloCliente(models.Model):

    nombre = models.CharField(max_length=40, null=False)
    apellido = models.CharField(max_length=40, null=False)
    email = models.EmailField(null=False)

    def __str__(self) -> str:
        return self.nombre + " " + self.apellido


class ModeloTramite(models.Model):

    tramite = models.IntegerField(choices=choices,verbose_name="")

    def __str__(self) -> str:
        return self.tramite + " - " 

    

class ModeloFecha(models.Model):

    dia = models.CharField(max_length=40, null=False)
    mes = models.CharField(max_length=40, null=False)
    año = models.CharField(max_length=40, null=False)

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