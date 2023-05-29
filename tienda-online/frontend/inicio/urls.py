from . import views
from django.urls import path


urlpatterns = [

    # Paginas

    path('', views.index, name='inicio'),

]