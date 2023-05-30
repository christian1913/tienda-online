from . import views
from django.urls import path


urlpatterns = [

    # Paginas

    path('usuario/', views.index, name='usuario'),

]