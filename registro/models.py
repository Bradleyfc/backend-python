from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class Registro(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)
    carnet = models.CharField(max_length=11)

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
    password = models.CharField(max_length=20, blank=True, null=True)


    def __str__(self):
        return f"{self.nombre} - {self.get_ocupacion_display()}"
