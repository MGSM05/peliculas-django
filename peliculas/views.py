from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Pelicula
from django.db.models import Q

# --- Lista de todas las películas con búsqueda---
class VistaListaPeliculas(ListView):
    model = Pelicula
    template_name = "peliculas/lista_peliculas.html"
    context_object_name = "peliculas"
    ordering = ["-fecha_creacion"]

    def get_queryset(self):
        queryset = super().get_queryset()
        consulta = self.request.GET.get("q")  # capturamos el parámetro de búsqueda
        if consulta:
            queryset = queryset.filter(
                Q(titulo__icontains=consulta) |   # busca en el título
                Q(sinopsis__icontains=consulta)   # o en la sinopsis
            )
        return queryset


# --- Detalle de una película ---
class VistaDetallePelicula(DetailView):
    model = Pelicula
    template_name = "peliculas/detalle_pelicula.html"
    context_object_name = "pelicula"


# --- Crear una película ---
class VistaCrearPelicula(LoginRequiredMixin, CreateView):
    model = Pelicula
    template_name = "peliculas/form_pelicula.html"
    fields = ["titulo", "sinopsis", "genero", "cartel"] 

    def form_valid(self, form):
        form.instance.autor = self.request.user
        messages.success(self.request, "Película añadida correctamente.")
        return super().form_valid(form)


# --- Editar una película ---
class VistaActualizarPelicula(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Pelicula
    template_name = "peliculas/form_pelicula.html"
    fields = ["titulo", "sinopsis", "genero", "cartel"]

    def test_func(self):
        pelicula = self.get_object()
        return self.request.user == pelicula.autor or self.request.user.is_staff

    def handle_no_permission(self):
        messages.error(self.request, "No tienes permiso para editar esta película.")
        return redirect("detalle_pelicula", pk=self.get_object().pk)

    def form_valid(self, form):
        messages.success(self.request, "Película actualizada correctamente.")
        return super().form_valid(form)


# --- Eliminar una película ---
class VistaEliminarPelicula(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Pelicula
    template_name = "peliculas/confirmar_eliminar.html"
    success_url = reverse_lazy("lista_peliculas")
    context_object_name = "pelicula"

    def test_func(self):
        pelicula = self.get_object()
        return self.request.user == pelicula.autor or self.request.user.is_staff

    def handle_no_permission(self):
        messages.error(self.request, "No tienes permiso para eliminar esta película.")
        return redirect("detalle_pelicula", pk=self.get_object().pk)

    def form_valid(self, form):
        messages.success(self.request, "Película eliminada correctamente.")
        return super().form_valid(form)