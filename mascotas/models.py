from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
TAMANIOS = [
    ("pequenio", "Pequeño"),
    ("mediano", "Mediano"),
    ("grande", "Grande")
]
GENEROS = [ 
    ("h", "Hembra"),
    ("m", "Macho")
]
class Mascota(models.Model):
    #id: IntegerField
    nombre = models.CharField(max_length=255)
    genero = models.CharField(choices=GENEROS, default="h", max_length=255)
    edad = models.PositiveIntegerField(null=True, blank=True)
    tamanio = models.CharField(choices=TAMANIOS, default="mediano", max_length=255)
    descripcion = models.TextField()
    idUsrRegistro = models.ForeignKey(
        get_user_model(),
        on_delete= models.CASCADE,
    )
    # idUsrAdopta = models.ForeignKey(
    #     get_user_model(),
    #     on_delete= models.CASCADE,
    #     null=True,
    #     blank=True,
    # )
    def __str__(self):
        return self.nombre

# class Comentario(models.Model):
#     mascota = models.ForeignKey(
#         Mascota,
#         on_delete=models.CASCADE,
#         related_name='comentarios',
#     )
#     cuerpo = models.CharField(max_length=255)
#     autor = models.ForeignKey(
#         get_user_model(),
#         on_delete=models.CASCADE,
    # )

    # def __str__(self):
    #     return self.cuerpo
