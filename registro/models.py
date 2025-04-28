from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError

# Función para validar carnet único (necesaria para las migraciones)
def validar_carnet_unico(value):
    # Implementación vacía para que las migraciones funcionen
    pass

# Create your models here.
class Registro(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)
    carnet = models.CharField(
        max_length=11, 
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^.{11}$',
                message="El carnet debe tener exactamente 11 caracteres.",
                code="carnet_invalido"
            )
        ]
    )

    SEXO = [
        ("M", "Masculino"),
        ("F", "Femenino"),
    ]

    sexo = models.CharField(max_length=1, choices=SEXO, default="M")

    direccion = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)
    movil = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)

    GRADO = [
        ("grado1", "Ninguno"),
        ("grado2", "Noveno Grado"),
        ("grado3", "Bachiller"),
        ("grado4", "Superior"),
    ]

    OCUPACION = [
        ("ocupacion1", "Desocupado"),
        ("ocupacion2", "Ama de Casa"),
        ("ocupacion3", "Trabajador Estatal"),
        ("ocupacion4", "Trabajador por Cuenta Propia"),
    ]
    grado = models.CharField(max_length=50, choices=GRADO, default="grado1")
    ocupacion = models.CharField(
        max_length=100, choices=OCUPACION, default="ocupacion1"
    )
    titulo = models.CharField(max_length=100)
    correo = models.EmailField(
        validators=[
            RegexValidator(
                regex=r"\.com$",
                message="El Correo debe ser finalizado en .com",
                code="correo_invalido",
            )
        ]
    )

    def __str__(self):
        return f"{self.nombre} - {self.get_ocupacion_display()}"
