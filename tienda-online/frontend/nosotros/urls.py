from . import views
from django.urls import path


urlpatterns = [

    # Paginas

    path('sobre-nosotros/', views.index, name='sobre-nosotros'),

]