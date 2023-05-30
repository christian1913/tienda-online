from django.shortcuts import render

# Paginas

def index(request):

    return render(request, 'frontend/usuario/index.html')


# Funciones