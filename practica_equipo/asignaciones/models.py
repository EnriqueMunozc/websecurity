from django.db import models
from empleados.models import Empleado
from inventario.models import Equipo


class Asignacion(models.Model):

    ACTIVA = "Activa"
    DEVUELTA = "Devuelta"

    ESTADOS = [
        (ACTIVA, "Activa"),
        (DEVUELTA, "Devuelta"),
    ]

    empleado = models.ForeignKey(
        Empleado,
        on_delete=models.CASCADE
    )

    equipo = models.ForeignKey(
        Equipo,
        on_delete=models.CASCADE
    )

    fecha_asignacion = models.DateField()

    fecha_devolucion = models.DateField(
        null=True,
        blank=True
    )

    estado = models.CharField(
        max_length=15,
        choices=ESTADOS,
        default=ACTIVA
    )

    def __str__(self):
        return f"{self.equipo} → {self.empleado}"