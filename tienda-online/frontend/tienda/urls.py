from . import views
from django.urls import path


urlpatterns = [

    # Paginas

    path('tienda/', views.index, name='tienda'),

]