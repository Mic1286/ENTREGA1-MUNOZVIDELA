from django.urls import path
from . import views

urlpatterns = [
    path('Hola/', views.crear ),
    path('Mostrar/', views.mostrar)
]
