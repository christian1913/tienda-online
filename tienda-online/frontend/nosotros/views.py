from django.shortcuts import render

# Paginas

def index(request):

    return render(request, 'frontend/sobre-nosotros/index.html')


# Funciones