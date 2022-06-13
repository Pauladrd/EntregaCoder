from django.urls import path
from .views import *


urlpatterns = [
    path('', clientes, name='Nombre'),
    path('TipodeTramite/', tipodeTramite, name='Tramite'),
    path('FechadeInicio/', FechadeInicio, name='Inicio'),
    path('Documentacion/', Documentacion, name='Documento'),
    path('Pago/', Pago, name='Pago'),
]