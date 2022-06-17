from django.urls import path
from .views import *




urlpatterns = [
    path('', clientes, name='Nombre'),
    path('Tramite/', Tramite, name='Tramite'),
    path('Fecha/', Fecha, name='Inicio'),
    path('Documentacion/', Documentacion, name='Documento'),
    path('Pago/', Pago, name='Pago'),
    path('index/', index, name='index'),

]