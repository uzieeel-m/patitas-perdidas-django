# ./pages/urls.py
from django.urls import path
from .views import (
    VistaPaginaInicio,
    VistaQuienesSomos,
    VistaContacto,
    )

urlpatterns = [
    path('', VistaPaginaInicio.as_view(), name="inicio"),
    path('quienes-somos/', VistaQuienesSomos.as_view(), name="quienes-somos"),
    path('contacto/', VistaContacto.as_view(), name="contacto"),
]