from django.urls import path
from . import views

urlpatterns = [
    path('', views.ver_interno, name='internos' ),
    path('buscar/', views.buscar_interno, name='buscar_interno'),
]
