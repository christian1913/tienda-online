from . import views
from django.urls import path


urlpatterns = [

    # Paginas

    path('carrito/', views.index, name='carrito'),

    # Funciones

    path('eliminar-producto/<int:id>', views.eliminar_producto, name='eliminar-producto'),

]