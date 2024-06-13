from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('pokemons/', views.pokemons, name='pokemons'),
    path('testing/', views.testing, name='testing'),
    path('pokemons/details/<int:id>', views.details, name='details')
]
