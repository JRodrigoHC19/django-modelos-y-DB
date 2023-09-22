from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='principal'),
    path('entradas/<str:autor>',views.list_entradas, name='lista_entradas'),
]