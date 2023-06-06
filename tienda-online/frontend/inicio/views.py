from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from frontend.productos.models import Productos, Categorias

def index(request):
    productos = Productos.objects.all()
    categorias = Categorias.objects.all()

    data = {
        'productos': productos,
        'categorias': categorias,
    }
    return render(request, 'frontend/inicio/index.html', data)
