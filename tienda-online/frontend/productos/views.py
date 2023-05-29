from django.shortcuts import render, redirect, get_object_or_404
from frontend.productos.models import Productos, Categorias
from frontend.carrito.models import Carrito, ElementosCarrito
from datetime import datetime




# Paginas

def index(request, id=None):
    productos = Productos.objects.get(id=id)
    categorias = Categorias.objects.all()
    data = {
        'productos': productos,
        'categorias': categorias,

    }
    return render(request, 'frontend/productos/index.html', data)




# Funciones


def agregar_producto(request, id=None):
    producto = get_object_or_404(Productos, id=id) 
    elemento_carrito, creado = ElementosCarrito.objects.get_or_create(producto=producto)
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)

    if carrito.carrito.filter(id=elemento_carrito.id).exists():
        carrito.fecha = datetime.now()
        carrito.save(update_fields=['fecha']) 

    else:
        carrito.carrito.add(elemento_carrito)

    return redirect('producto', id=id)