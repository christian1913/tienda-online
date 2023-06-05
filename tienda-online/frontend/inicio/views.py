from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from frontend.productos.models import Productos, Categorias

def index(request):
    productos = Productos.objects.all()
    categorias = Categorias.objects.all()

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('inicio')  # redirige al usuario a la página de inicio
    else:
        form = AuthenticationForm()

    data = {
        'productos': productos,
        'categorias': categorias,
        'form': form,
    }
    return render(request, 'frontend/inicio/index.html', data)
