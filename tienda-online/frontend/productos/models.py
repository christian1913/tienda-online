from django.db import models

# Create your models here.

class Categorias(models.Model):
    nombre = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='imagenes')

    def __str__(self):
        return self.nombre
    

class Imagenes(models.Model):
    imagen = models.ImageField(upload_to='imagenes')
    def __str__(self):
        return self.imagen.name 

class Productos(models.Model):
    nombre = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='imagenes')
    otras_imagenes = models.ManyToManyField(Imagenes, blank=True)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre