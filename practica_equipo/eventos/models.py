from django.db import models


class Evento(models.Model):

    TIPO_EVENTO = [

        ("Equipo", "Equipo"),
        ("Empleado", "Empleado"),
        ("Asignación", "Asignación"),
        ("Sistema", "Sistema"),

    ]

    tipo = models.CharField(
        max_length=20,
        choices=TIPO_EVENTO
    )

    descripcion = models.TextField()

    fecha = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return f"{self.tipo} - {self.fecha.strftime('%d/%m/%Y %H:%M')}"