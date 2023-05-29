from django.shortcuts import render, redirect, get_object_or_404
from frontend.productos.models import Productos, Categorias
from frontend.carrito.models import Carrito, ElementosCarrito


# Paginas

def index(request):
    productos = Productos.objects.all()
    categorias = Categorias.objects.all()
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
    data = {
        'productos': productos,
        'categorias': categorias,
        'carrito': carrito,
    }
    return render(request, 'frontend/carrito/index.html', data)


# Funciones

def eliminar_producto(request, id=None):
    elemento_carrito = get_object_or_404(ElementosCarrito, producto__id=id)
    carrito, _ = Carrito.objects.get_or_create(usuario=request.user)

    if carrito.carrito.filter(id=elemento_carrito.id).exists():
        carrito.carrito.remove(elemento_carrito)

    return redirect('carrito')