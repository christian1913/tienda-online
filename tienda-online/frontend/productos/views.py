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
    
    session_key = request.session.session_key
    if not session_key:
        # Si no hay una clave de sesión, forzar la creación de una
        request.session.create()
        session_key = request.session.session_key

    if request.user.is_authenticated:
        carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
    else:
        carrito, _ = Carrito.objects.get_or_create(session_key=session_key)

    if carrito.carrito.filter(id=elemento_carrito.id).exists():
        carrito.fecha = datetime.now()
        carrito.save(update_fields=['fecha']) 
    else:
        carrito.carrito.add(elemento_carrito)

    return redirect('producto', id=id)
