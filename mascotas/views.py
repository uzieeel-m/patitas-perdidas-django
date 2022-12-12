from django.views.generic import DetailView, ListView
from .models import Mascota

# Create your views here.
class VistaDetalleMascota(DetailView):
    model= Mascota
    context_object_name = 'mascota'
    template_name = 'mascotas/detalle_mascota.html'

class VistaListaMascotas(ListView):
    model = Mascota
    context_object_name= 'lista_mascotas'
    template_name = 'mascotas/lista_mascotas.html'