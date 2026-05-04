# peliculas/urls.py
from django.urls import path
from .views import (
    VistaListaPeliculas,
    VistaDetallePelicula,
    VistaCrearPelicula,
    VistaActualizarPelicula,
    VistaEliminarPelicula,
)

urlpatterns = [
    path("", VistaListaPeliculas.as_view(), name="lista_peliculas"),
    path("pelicula/<int:pk>/", VistaDetallePelicula.as_view(), name="detalle_pelicula"),
    path("pelicula/nueva/", VistaCrearPelicula.as_view(), name="nueva_pelicula"),
    path("pelicula/<int:pk>/editar/", VistaActualizarPelicula.as_view(), name="editar_pelicula"),
    path("pelicula/<int:pk>/eliminar/", VistaEliminarPelicula.as_view(), name="eliminar_pelicula"),
]