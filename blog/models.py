from django.db import models

class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    anio = models.PositiveIntegerField()
    genero = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='peliculas/', null=True, blank=True)

    def __str__(self):
        return self.titulo
