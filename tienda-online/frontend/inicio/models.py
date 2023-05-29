from django.db import models

# Create your models here.


class Formulario(models.Model):
    nombre = models.CharField(max_length=200)
    correo = models.EmailField()
    mensaje = models.TextField(max_length=500)
    telefono = models.CharField(max_length=20)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Orden {self.nombre} - {self.fecha}'