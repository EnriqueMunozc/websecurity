from django.shortcuts import render

from inventario.models import Equipo
from empleados.models import Empleado
from asignaciones.models import Asignacion


def dashboard(request):

    context = {

        "equipos": Equipo.objects.count(),

        "empleados": Empleado.objects.count(),

        "asignaciones": Asignacion.objects.count(),

        "disponibles": Equipo.objects.filter(
            estado="Disponible"
        ).count(),

    }

    return render(
        request,
        "dashboard/dashboard.html",
        context
    )