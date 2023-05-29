from . import views
from django.urls import path


urlpatterns = [

    # Paginas

    path('tienda/producto-<int:id>', views.index, name='producto'),

    # Funciones

    path('agregar-producto/<int:id>', views.agregar_producto, name='agregar-producto'),

]