from django import forms

class FormularioContacto(forms.Form):
    nombre = forms.CharField(label='Nombre(s)', required=True, max_lenght=20)
    apellido = forms.CharField(label='Apellido(s)', required=True, max_lenght=40)
    email = forms.CharField(label='email', required=True, max_length=50)
    numCelular = forms.CharField(label='Número de celular', required=True, max_lenght=10)
    asunto = forms.CharField(label='Asunto', required=True)
    contenido = forms.CharField(label='Contenido', max_length=254, widget=forms.Textarea)
