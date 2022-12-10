from django.views.generic import TemplateView
from mascotas.models import Mascota

# Create your views here.
class VistaPaginaInicio(TemplateView):
    template_name = "index.html"
    lista_mascotas = Mascota.objects

class VistaQuienesSomos(TemplateView):
    template_name = "quienes-somos.html"

class VistaContacto(TemplateView):
    template_name = "contacto.html"
