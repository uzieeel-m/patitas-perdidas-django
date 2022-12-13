from django.views.generic import DetailView, ListView, DeleteView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .models import Usuario

# Create your views here.
class VistaPerfilUsuario(DetailView):
    model = Usuario
    template_name = "usuarios/perfil.html"

class VistaListaUsuarios(ListView):
    model = Usuario
    context_object_name = "lista_usuarios"
    template_name = "usuarios/lista_usuarios.html"

class VistaEditarUsuario(UpdateView):
    model = Usuario
    success_url = reverse_lazy("inicio")
    template_name = "usuarios/editar_usuario.html"

class VistaEliminarUsuario(DeleteView):
    model = Usuario
    success_url = reverse_lazy("inicio")
    template_name = "usuarios/eliminar_usuario.html"