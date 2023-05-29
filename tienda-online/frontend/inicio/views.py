from django.shortcuts import render
from frontend.productos.models import Productos, Categorias

# Paginas


def index(request):
    productos = Productos.objects.all()
    categorias = Categorias.objects.all()
    data = {
        'productos': productos,
        'categorias': categorias,

    }
    return render(request, 'frontend/inicio/index.html', data)

# Funciones