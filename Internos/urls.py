from django.urls import path
from . import views

urlpatterns = [
    path('', views.ver_interno, name='internos' ),
    path('buscar/', views.buscar_interno, name='buscar_interno'),
    path('agregar_interno/', views.agregar_interno, name='agregar_interno'),
    path('borrar_interno/<int:interno_id>/', views.borrar_interno, name='borrar_interno'),
    path('editar_interno/<int:interno_id>/', views.editar_interno, name='editar_interno'),

]
