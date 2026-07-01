from django.contrib import admin
from .models import Equipo


@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):

    list_display = (
        "codigo",
        "tipo",
        "marca",
        "modelo",
        "estado",
    )

    search_fields = (
        "codigo",
        "marca",
        "modelo",
    )

    list_filter = (
        "tipo",
        "estado",
        "marca",
    )

    ordering = (
        "codigo",
    )