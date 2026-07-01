from django.db import models


class Evento(models.Model):

    descripcion = models.TextField()

    fecha = models.DateTimeField(
        auto_now_add=True
    )

    modulo = models.CharField(
        max_length=30
    )

    usuario = models.CharField(
        max_length=50
    )

    def __str__(self):
        return f"{self.fecha.strftime('%d/%m/%Y %H:%M')} - {self.modulo}"