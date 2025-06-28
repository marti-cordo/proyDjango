from django.shortcuts import render
from .models import Pelicula

def peliculas_view(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'blog/lista_peliculas.html', {'peliculas': peliculas})
