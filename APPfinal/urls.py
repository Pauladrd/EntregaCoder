from django.urls import path
from .views import *


urlpatterns = [
    path('', clientes, name='Nombre'),
    path('TipodeTramite/', tipodeTramite, name='Tramite'),
    path('FechadeInicio/', fechadeInicio, name='Inicio'),
    path('Documentacion/', documentacion, name='Documento'),
    path('Pago/', pago, name='Pago'),
]