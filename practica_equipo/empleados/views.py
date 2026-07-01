from django.shortcuts import render, redirect, get_object_or_404

from .models import Empleado
from .forms import EmpleadoForm
from eventos.models import Evento


def lista_empleados(request):

    empleados = Empleado.objects.all().order_by("nombre")

    return render(
        request,
        "empleados/lista_empleados.html",
        {
            "empleados": empleados
        }
    )


def crear_empleado(request):

    if request.method == "POST":

        formulario = EmpleadoForm(request.POST)

        if formulario.is_valid():

            formulario.save()

            Evento.objects.create(
                tipo="Empleado Creado",
                descripcion=f"Se ha creado un nuevo empleado: {formulario.cleaned_data['nombre']}"
            )

            return redirect("lista_empleados")

    else:

        formulario = EmpleadoForm()

    return render(
        request,
        "empleados/formulario_empleado.html",
        {
            "formulario": formulario,
            "titulo": "Nuevo empleado"
        }
    )


def editar_empleado(request,id):

    empleado = get_object_or_404(Empleado,pk=id)

    if request.method=="POST":

        formulario = EmpleadoForm(request.POST,instance=empleado)

        if formulario.is_valid():

            formulario.save()
            Evento.objects.create(
                tipo="Empleado Editado",
                descripcion=f"Se ha editado el empleado: {formulario.cleaned_data['nombre']}"
            )

            return redirect("lista_empleados")

    else:

        formulario = EmpleadoForm(instance=empleado)

    return render(
        request,
        "empleados/formulario_empleado.html",
        {
            "formulario": formulario,
            "titulo":"Editar empleado"
        }
    )


def eliminar_empleado(request,id):

    empleado=get_object_or_404(Empleado,pk=id)

    if request.method=="POST":

        empleado.delete()
        Evento.objects.create(
            tipo="Empleado Eliminado",
            descripcion=f"Se ha eliminado el empleado: {empleado.nombre}"
        )

        return redirect("lista_empleados")

    return render(
        request,
        "empleados/eliminar_empleado.html",
        {
            "empleado":empleado
        }
    )