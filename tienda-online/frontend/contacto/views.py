from django.shortcuts import render

# Paginas

def index(request):

    return render(request, 'frontend/contacto/index.html')


# Funciones