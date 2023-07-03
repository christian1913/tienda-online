from . import views
from django.urls import path


urlpatterns = [

    # Paginas

    path('usuario/', views.index, name='usuario'),
    path('reset-password/', views.reset_password, name='reset-password'),

]