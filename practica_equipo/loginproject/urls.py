#loginproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # Dashboard
    path("", include("dashboard.urls")),

    # Módulos
    path("usuarios/", include("usuarios.urls")),
    path("inventario/", include("inventario.urls")),
    path("empleados/", include("empleados.urls")),
    path("asignaciones/", include("asignaciones.urls")),
    path("eventos/", include("eventos.urls")),
]