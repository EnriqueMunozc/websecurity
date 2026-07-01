from django.shortcuts import render,redirect,get_object_or_404
from .models import Asignacion
from .forms import AsignacionForm
from inventario.models import Equipo
from eventos.models import Evento


def lista_asignaciones(request):

    asignaciones=Asignacion.objects.select_related(
        "empleado",
        "equipo"
    )

    return render(

        request,

        "asignaciones/lista_asignaciones.html",

        {

            "asignaciones":asignaciones

        }

    )


def crear_asignacion(request):

    if request.method=="POST":

        formulario=AsignacionForm(request.POST)

        if formulario.is_valid():

            equipo = formulario.cleaned_data["equipo"]

            if equipo.estado != "Disponible":

                formulario.add_error(
                    "equipo",
                    "Este equipo ya está asignado."
                )
            else:

                asignacion=formulario.save(commit=False)

                equipo.estado = "Asignado"

                equipo.save()

                asignacion.save()
                Evento.objects.create(
                    tipo="Asignación Creada",
                    descripcion=f"Se ha creado una nueva asignación para el empleado {asignacion.empleado.nombre} con el equipo {asignacion.equipo.codigo}."
                )

                return redirect("lista_asignaciones")

    else:

        formulario=AsignacionForm()

    return render(

        request,

        "asignaciones/formulario_asignacion.html",

        {

            "formulario":formulario,

            "titulo":"Nueva Asignación"

        }

    )