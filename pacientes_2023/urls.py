from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index' ),
    path('borrar/<int:paciente_id>/', views.borrar_paciente, name='borrar_paciente'),
    path('editar/<int:paciente_id>/', views.editar_paciente, name='editar_paciente'),
    path('agregar/', views.agregar_paciente, name='agregar_paciente'),
    path("salir/", views.salir, name="salir"),
    path('pacientes/<str:servicio>/', views.pacientes_por_servicio, name='pacientes_por_servicio'),
    path('pacientes_no_internados/', views.pacientes_no_internados, name='pacientes_no_internados'),

]
