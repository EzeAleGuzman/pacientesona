from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pacientes/', include ('pacientes_2023.urls')),
    path('vehiculos/', include ('Vehiculos.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', RedirectView.as_view(pattern_name='index'), name='login_redirect'),
]
