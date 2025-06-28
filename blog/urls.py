from django.urls import path
from .views import lista_peliculas

urlpatterns = [
    path('', lista_peliculas, name='lista_peliculas'),
]
