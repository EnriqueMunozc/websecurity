#inventario/views.py
from django.shortcuts import render, redirect, get_object_or_404

from .models import Equipo
from .forms import EquipoForm
from eventos.models import Evento

def lista_equipos(request):

    equipos = Equipo.objects.all().order_by("codigo")

    return render(
        request,
        "inventario/lista_equipos.html",
        {
            "equipos": equipos
        }
    )


def crear_equipo(request):

    if request.method == "POST":

        formulario = EquipoForm(request.POST)

        if formulario.is_valid():

            formulario.save()

            Evento.objects.create(
                tipo = "Equipo Creado",
                descripcion = f"Se ha creado un nuevo equipo con código {formulario.cleaned_data['codigo']}."
            )
            return redirect("lista_equipos")

    else:

        formulario = EquipoForm()

    return render(
        request,
        "inventario/formulario_equipo.html",
        {
            "formulario": formulario,
            "titulo": "Nuevo Equipo"
        }
    )


def editar_equipo(request, id):

    equipo = get_object_or_404(
        Equipo,
        pk=id
    )

    if request.method == "POST":

        formulario = EquipoForm(
            request.POST,
            instance=equipo
        )

        if formulario.is_valid():

            formulario.save()
            Evento.objects.create(
                tipo = "Equipo Editado",
                descripcion = f"Se ha editado el equipo con código {formulario.cleaned_data['codigo']}."
            )

            return redirect("lista_equipos")

    else:

        formulario = EquipoForm(
            instance=equipo
        )

    return render(
        request,
        "inventario/formulario_equipo.html",
        {
            "formulario": formulario,
            "titulo": "Editar Equipo"
        }
    )


def eliminar_equipo(request, id):

    equipo = get_object_or_404(
        Equipo,
        pk=id
    )

    if request.method == "POST":

        equipo.delete()
        Evento.objects.create(
            tipo = "Equipo Eliminado",
            descripcion = f"Se ha eliminado el equipo con código {equipo.codigo}."
        )

        return redirect("lista_equipos")

    return render(
        request,
        "inventario/eliminar_equipo.html",
        {
            "equipo": equipo
        }
    )


from django.http import JsonResponse

def buscar_equipo(request):

    texto = request.GET.get("q", "")

    equipos = Equipo.objects.filter(
        modelo__icontains=texto
    ) | Equipo.objects.filter(
        marca__icontains=texto
    ) | Equipo.objects.filter(
        codigo__icontains=texto
    )

    datos = []

    for equipo in equipos:

        datos.append({
            "id": equipo.id,
            "codigo": equipo.codigo,
            "marca": equipo.marca,
            "modelo": equipo.modelo,
            "tipo": equipo.tipo,
            "estado": equipo.estado,
        })

    return JsonResponse(datos, safe=False)