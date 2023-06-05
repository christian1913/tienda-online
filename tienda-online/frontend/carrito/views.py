from django.shortcuts import render, redirect, get_object_or_404
from frontend.productos.models import Productos, Categorias
from frontend.carrito.models import Carrito, ElementosCarrito


# Paginas

def index(request):
    productos = Productos.objects.all()
    categorias = Categorias.objects.all()

    session_key = request.session.session_key
    if not session_key:
        # Si no hay una clave de sesión, forzar la creación de una
        request.session.create()
        session_key = request.session.session_key

    if request.user.is_authenticated:
        carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
    else:
        carrito, _ = Carrito.objects.get_or_create(session_key=session_key)
        
    data = {
        'productos': productos,
        'categorias': categorias,
        'carrito': carrito,
    }
    return render(request, 'frontend/carrito/index.html', data)


# Funciones

def eliminar_producto(request, id=None):
    elemento_carrito = get_object_or_404(ElementosCarrito, producto__id=id)

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
        carrito.carrito.remove(elemento_carrito)

    return redirect('carrito')