from django.contrib import admin
from .models import Carrito, ElementosCarrito, Pedidos

# Register your models here.

admin.site.register(Carrito)
admin.site.register(ElementosCarrito)
admin.site.register(Pedidos)