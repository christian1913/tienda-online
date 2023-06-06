from . import views
from django.urls import path, include
urlpatterns = [

    # Apps

    path('' , include('frontend.carrito.urls')),

    path('' , include('frontend.tienda.urls')),

    path('' , include('frontend.productos.urls')),

    path('' , include('frontend.inicio.urls')),

    path('' , include('frontend.usuario.urls')),

    # Frontend

    path('login/', views.inicio_sesion, name='inicio-sesion'),

 
]