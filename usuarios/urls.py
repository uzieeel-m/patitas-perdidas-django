# ./usuarios/urls.py
from django.urls import path
from .views import VistaPerfilUsuario, VistaListaUsuarios, VistaEditarUsuario, VistaEliminarUsuario

urlpatterns = [
    path("perfil/<int:pk>", VistaPerfilUsuario.as_view(), name="perfil"),
    path("lista-usuarios/", VistaListaUsuarios.as_view(), name="lista-usuarios"),
    path("editar-usuario/<int:pk>", VistaEditarUsuario.as_view(), name="editar-usuario"),
    path("eliminar-usuario/<int:pk>", VistaEliminarUsuario.as_view(), name="eliminar-usuario"),
]