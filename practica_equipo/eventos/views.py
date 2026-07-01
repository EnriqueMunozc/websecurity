from django.shortcuts import render

from .models import Evento


def lista_eventos(request):

    eventos = Evento.objects.all().order_by("-fecha")

    return render(

        request,

        "eventos/lista_eventos.html",

        {

            "eventos": eventos

        }

    )