from django.urls import path
from .views import VistaDetalleMascota, VistaListaMascotas, VistaMisMascotas, VistaEditarMascota, VistaEliminarMascota, VistaAgregarMascota, VistaEscribirComentario

urlpatterns = [
    path('detalle-mascota/<int:pk>', VistaDetalleMascota.as_view(), name="detalle-mascota"),
    path('lista-mascotas', VistaListaMascotas.as_view(), name="lista-mascotas"),
    path('mis-mascotas', VistaMisMascotas.as_view(), name="mis-mascotas"),
    path('editar-mascota/<int:pk>', VistaEditarMascota.as_view(), name="editar-mascota"),
    path('eliminar-mascota/<int:pk>', VistaEliminarMascota.as_view(), name="eliminar-mascota"),
    path('agregar-mascota/', VistaAgregarMascota.as_view(), name="agregar-mascota"),
    path('escribir-comentario/<int:pk>', VistaEscribirComentario.as_view(), name="escribir-comentario"),
]