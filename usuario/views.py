from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Producto, Usuario, Precio,Categoría,Supermercado
# Create your views here.
def Pagina1(request):
    usuario = Usuario.objects.all()

    data = {
        'usuarios': usuario
    }

    return render(request, 'usuario/Pagina1.html',  data)

def Pagina2(request):

    return render(request, 'usuario/Pagina2.html')

def Pagina3(request):

    return render(request, 'usuario/Pagina3.html')

def Pagina4(request):

    return render(request, 'usuario/Pagina4.html')

def Pagina5(request):

    return render(request, 'usuario/Pagina5.html')

def Pagina6(request):

    return render(request, 'usuario/Pagina6.html')

def registrar(request):
    Nombre_User = request.POST['nombre']
    Correo = request.POST['email']
    contraseña = request.POST['contraseña']

    usuarios = Usuario.objects.create(Nombre_User = Nombre_User, contraseña=contraseña, Correo = Correo)
    return redirect('/')