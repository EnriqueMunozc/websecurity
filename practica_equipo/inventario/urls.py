#inventario/urls.py
from django.urls import path
from . import views

urlpatterns = [

    path(
        "",
        views.lista_equipos,
        name="lista_equipos"
    ),

    path(
        "nuevo/",
        views.crear_equipo,
        name="crear_equipo"
    ),

    path(
        "buscar/", 
        views.buscar_equipo, 
        name="buscar_equipo"),

    path(
        "editar/<int:id>/",
        views.editar_equipo,
        name="editar_equipo"
    ),

    path(
        "eliminar/<int:id>/",
        views.eliminar_equipo,
        name="eliminar_equipo"
    ),

]