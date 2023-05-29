from django.contrib import admin
from .models import Productos, Categorias, Imagenes

# Register your models here.

admin.site.register(Categorias)
admin.site.register(Productos)
admin.site.register(Imagenes)