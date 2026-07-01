from django.urls import path

from . import views

urlpatterns=[

    path(

        "",

        views.lista_asignaciones,

        name="lista_asignaciones"

    ),

    path(

        "nuevo/",

        views.crear_asignacion,

        name="crear_asignacion"

    ),

]