from django.shortcuts import render, redirect, get_object_or_404

from .models import Empleado
from .forms import EmpleadoForm


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

        return redirect("lista_empleados")

    return render(
        request,
        "empleados/eliminar_empleado.html",
        {
            "empleado":empleado
        }
    )