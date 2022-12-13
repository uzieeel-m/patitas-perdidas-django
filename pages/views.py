from django.views.generic import TemplateView

# Create your views here.
class VistaPaginaInicio(TemplateView):
    template_name = "index.html"

class VistaQuienesSomos(TemplateView):
    template_name = "quienes-somos.html"

class VistaContacto(TemplateView):
    template_name = "contacto.html"
