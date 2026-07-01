from django.db import models


class Empleado(models.Model):

    numero_empleado = models.CharField(
        max_length=10,
        unique=True
    )

    nombre = models.CharField(
        max_length=50
    )

    apellido = models.CharField(
        max_length=50
    )

    departamento = models.CharField(
        max_length=50
    )

    correo = models.EmailField(
        unique=True
    )

    telefono = models.CharField(
        max_length=15
    )

    activo = models.BooleanField(
        default=True
    )

    fecha_registro = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.nombre} {self.apellido}"