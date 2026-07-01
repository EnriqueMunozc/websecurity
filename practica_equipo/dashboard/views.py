#dashboard/views.py
from django.shortcuts import render


from inventario.models import Equipo
from empleados.models import Empleado
from asignaciones.models import Asignacion
from eventos.models import Evento


def inicio(request):

    total_equipos = Equipo.objects.count()

    total_empleados = Empleado.objects.count()

    total_asignaciones = Asignacion.objects.count()

    total_eventos = Evento.objects.count()

    disponibles = Equipo.objects.filter(
        estado="Disponible"
    ).count()

    asignados = Equipo.objects.filter(
        estado="Asignado"
    ).count()

    eventos = Evento.objects.order_by(
        "-fecha"
    )[:5]

    return render(

        request,

        "dashboard/index.html",

        {

            "total_equipos": total_equipos,
            "total_empleados": total_empleados,
            "total_asignaciones": total_asignaciones,
            "total_eventos": total_eventos,
            "disponibles": disponibles,
            "asignados": asignados,
            "eventos": eventos,

        }

    )