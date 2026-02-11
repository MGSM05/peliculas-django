from django.contrib import admin
from .models import Pelicula

class PeliculaAdmin(admin.ModelAdmin):
    list_display = (
        'titulo',
        'genero', 
        'autor', 
        'fecha_creacion'
    )

admin.site.register(Pelicula, PeliculaAdmin)

