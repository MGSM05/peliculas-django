from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)                  # texto corto
    sinopsis = models.TextField()                              # texto largo
    genero = models.CharField(max_length=100)
    
    # Fecha automática
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    autor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='mis_peliculas'
    )

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('detalle_pelicula', kwargs={'pk': self.pk})