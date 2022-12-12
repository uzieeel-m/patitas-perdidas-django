from django.urls import path
from . import views

urlpatterns = [
    path("", views.correo.as_view(), name="correo"),
]