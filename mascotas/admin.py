from django.contrib import admin
from .models import Mascota

# Register your models here.
# class ComentarioMascota(admin.TabularInline):
#     model = Comentario

# class MascotaAdmin(admin.ModelAdmin):
#     list_display = ('nombre', 'genero', 'edad', 'tamanio', 'descripcion')
#     inlines = [ ComentarioMascota ]

admin.site.register(Mascota)