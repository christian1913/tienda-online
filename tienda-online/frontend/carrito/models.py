from django.db import models
from django.contrib.auth.models import User
from frontend.productos.models import Productos

# Create your models here.
class ElementosCarrito(models.Model):
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.producto.nombre}'   


class Carrito(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    carrito = models.ManyToManyField(ElementosCarrito, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Carrito de {self.usuario.username}'


 
class Pedidos(models.Model):
    id = models.AutoField(primary_key=True)
    comprador = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    compra = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    def __str__(self):
        return f'Orden {self.id} - {self.fecha}'