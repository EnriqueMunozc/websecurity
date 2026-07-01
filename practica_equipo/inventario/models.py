from django.db import models


class Equipo(models.Model):

    # ===== Tipos de equipo =====

    LAPTOP = "Laptop"
    CELULAR = "Celular"

    TIPOS = [
        (LAPTOP, "Laptop"),
        (CELULAR, "Celular"),
    ]

    # ===== Estados del equipo =====

    DISPONIBLE = "Disponible"
    ASIGNADO = "Asignado"
    MANTENIMIENTO = "Mantenimiento"

    ESTADOS = [
        (DISPONIBLE, "Disponible"),
        (ASIGNADO, "Asignado"),
        (MANTENIMIENTO, "Mantenimiento"),
    ]

    # ===== Información del equipo =====

    codigo = models.CharField(
        max_length=20,
        unique=True
    )

    tipo = models.CharField(
        max_length=20,
        choices=TIPOS
    )

    marca = models.CharField(
        max_length=50
    )

    modelo = models.CharField(
        max_length=100
    )

    numero_serie = models.CharField(
        max_length=100,
        unique=True
    )

    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default=DISPONIBLE
    )

    observaciones = models.TextField(
        blank=True
    )

    fecha_registro = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.codigo} - {self.marca} {self.modelo}"