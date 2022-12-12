from django.views.generic import DetailView, ListView
from django.urls import reverse_lazy
from .models import Usuario

# Create your views here.
class VistaPerfilUsuario(DetailView):
    model = Usuario
    template_name = "account/perfil.html"

class VistaListaUsuarios(ListView):
    model = Usuario
    context_object_name = "lista_usuarios"
    template_name = "account/lista_usuarios.html"