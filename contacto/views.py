from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from .forms import FormularioContacto

# Create your views here.

def correo(request):
    formulario = FormularioContacto()

    if request.method=='POST':
        formulario = FormularioContacto(data=request.POST)
        if formulario.is_valid():
            nombre = request.POST.get("nombre")
            apellido = request.POST.get("apellido")
            email = request.POST.get("email")
            numCelular = request.POST.get("numCelular")
            asunto = request.POST.get("asunto")
            contenido = request.POST.get("contenido")
            
            email = EmailMessage("Mensaje de prueba",
            "Mensaje enviado por {} {} por el asunto {}, {}, puedes comunicarte al {}".format(nombre, apellido, asunto, contenido,numCelular ),
            ["alu.18131273@correo.itlalaguna.edu.mx"],
            reply_to = [email]
            )
            try:
                email.send()
                return redirect('/correo/?valido')
            except:
                return redirect('/correo/?novalido')

    return render(request, "correo/correo.html", {'miFormulario':formulario})