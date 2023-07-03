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
    OPTIMO = 'Optimo'
    BUEN_ESTADO = 'Buen estado'
    POR_RESTAURAR = 'Por restaurar'
    SIN_ESPECIFICAR = 'Sin especificar'

    ESTADO_CHOICES = (
        (OPTIMO, 'Óptimo'),
        (BUEN_ESTADO, 'Buen estado'),
        (POR_RESTAURAR, 'Por restaurar'),
        (SIN_ESPECIFICAR, 'Sin especificar'),
    )

    nombre = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='imagenes')
    otras_imagenes = models.ManyToManyField(Imagenes, blank=True)
    descripcion = models.TextField()
    informacion = models.TextField()
    peso = models.DecimalField(max_digits=10, decimal_places=2)
    dimensiones = models.CharField(max_length=50)
    año = models.CharField(max_length=20)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    estado = models.CharField(max_length=200, choices=ESTADO_CHOICES, default=OPTIMO)

    def __str__(self):
        return self.nombre