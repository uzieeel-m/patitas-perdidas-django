from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView, CreateView
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

class VistaMisMascotas(ListView):
    model = Mascota
    context_object_name = 'lista_mascotas'
    template_name = "mascotas/mis_mascotas.html"

class VistaEditarMascota(UpdateView):
    model = Mascota
    context_object_name = "mascota"
    success_url= reverse_lazy('mis-mascotas')
    template_name = "mascotas/editar_mascota.html"
    fields = ('nombre', 'genero', 'edad', 'tamanio', 'descripcion', 'imagen')

class VistaEliminarMascota(DeleteView):
    model = Mascota
    context_object_name = "mascota"
    success_url= reverse_lazy('mis-mascotas')
    template_name = "mascotas/eliminar_mascota.html"

class VistaAgregarMascota(CreateView):
    model = Mascota
    context_object_name = "mascota"
    success_url= reverse_lazy('mis-mascotas')
    template_name = "mascotas/agregar_mascota.html"
    fields = ('nombre', 'genero', 'edad', 'tamanio', 'descripcion', 'imagen')

    #método para decirle a django quién es el usuario que registra la mascota
    def form_valid(self, form):
        form.instance.idUsrRegistro = self.request.user
        return super().form_valid(form)

# class VistaEscribirComentario(UpdateView):
#     model = Mascota
#     idMascota = str(model.pk)
#     context_object_name = "mascota"
#     success_url = reverse_lazy('detalle-mascota/'+idMascota)
#     template_name = "mascotas/editar_mascota.html"
#     fields = ('comentarios')
