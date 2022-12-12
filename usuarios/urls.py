# ./usuarios/urls.py
from django.urls import path
from .views import VistaPerfilUsuario, VistaListaUsuarios

urlpatterns = [
    path("perfil/<int:pk>", VistaPerfilUsuario.as_view(), name="perfil"),
    path("lista-usuarios/", VistaListaUsuarios.as_view(), name="lista-usuarios"),
]