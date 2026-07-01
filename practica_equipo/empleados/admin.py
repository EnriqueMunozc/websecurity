from django.contrib import admin
from .models import Empleado


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):

    list_display = (
        "numero_empleado",
        "nombre",
        "apellido",
        "departamento",
        "correo",
        "activo",
    )

    search_fields = (
        "nombre",
        "apellido",
        "numero_empleado",
    )

    list_filter = (
        "departamento",
        "activo",
    )

    ordering = (
        "nombre",
    )