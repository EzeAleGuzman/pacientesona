from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path('pacientes/', include ('pacientes_2023.urls')),
    path('vehiculos/', include ('Vehiculos.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', RedirectView.as_view(pattern_name='index'), name='login_redirect'),
    path('internos/', include ('Internos.urls')),
    path('protocolos/',include ('protocolos.urls')),
]
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
