from django.urls import path
from . import views
from .views import agregar_version,listarData
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('cargar/', views.cargar_documento, name='cargar_documento'),
    path('agregar_version/<int:documento_id>/', agregar_version, name='agregar_version'),
    path("lista-de-registros/", listarData, name="listarData"),
    path('cargar/<str:clase>/', views.documentos_por_clase, name='documentos_por_clase'),
   
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)