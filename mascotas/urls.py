from django.urls import path
from .views import VistaDetalleMascota, VistaListaMascotas

urlpatterns = [
    path('detalle-mascota/<int:pk>', VistaDetalleMascota.as_view(), name="detalle-mascota"),
    path('lista-mascotas', VistaListaMascotas.as_view(), name="lista-mascotas"),
]