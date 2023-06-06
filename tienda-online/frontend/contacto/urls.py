from . import views
from django.urls import path


urlpatterns = [

    # Paginas

    path('contacto/', views.index, name='contacto'),

]