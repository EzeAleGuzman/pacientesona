from django.urls import path, include
from . import views

urlpatterns = [
    path('ver/', views.ver_vehiculos, name='vehiculos' ),
    path('buscar/', views.buscar_vehiculo, name='buscar_vehiculo'),
    path('vehiculo/<int:vehiculo_id>/', views.ver_ficha_vehiculo, name='ver_ficha_vehiculo'),
]
