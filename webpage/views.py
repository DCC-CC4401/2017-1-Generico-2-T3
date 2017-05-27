from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from webpage.models import Comprador,Vendedor,VendedorFijo ,VendedorAmbulante

def index(request):
    return render(request, 'webpage/index.html')


def login_user(request):
    return render(request, 'webpage/login.html')


def signup(request):
    return render(request, 'webpage/signup.html')


def perfil_vendedor(request):
    return render(request, 'webpage/vendedor-profile-page.html')


def gestion_producto(request):
    return render(request, 'webpage/gestion-productos.html')


def logout_intent(request):
    logout(request)
    return redirect('index')


def login_intent(request):
    name = request.POST['nombre']
    passw = request.POST['password']
    user = authenticate(username=name, password=passw)
    if user is not None:
        login(request, user)
        return redirect('index')

    else:
        return render(request, 'webpage/login.html', {
            'error': 'No ha ingresado un usuario y contraseña válidos'
        })


def reg_intent(request):
    name = request.POST['nombre']
    passw = request.POST['password']
    mail = request.POST['email']
    usuario, created = User.objects.get_or_create(username=name,email = mail)
    if(created):
        usuario.set_password(passw)
        usuario.save()
        tipo = request.POST['tipo']
        if(tipo=='Cliente'):
            vavatar = request.POST['group1']
            comprador = Comprador.objects.create(user=usuario,avatar = vavatar)
            comprador.save()
        else:
            vacepta_Efectivo = request.POST['Efectivo']=='on'
            vacepta_Credito = request.POST['Credito']=='on'
            vacepta_Debito = request.POST['Debito']=='on'
            vacepta_Junaeb = request.POST['Junaeb']=='on'
            vendedor = Vendedor.objects.create(user=usuario,acepta_Efectivo=vacepta_Efectivo,
                                               acepta_Credito = vacepta_Credito, acepta_Debito = vacepta_Debito,
                                               acepta_Junaeb = vacepta_Junaeb, avatar = request.FILES['perfil'])

            if(tipo=='VendedorFijo'):
                vhoraInicio,vminutoInicio = str(request.POST['horaInicio']).split(":")
                vhoraFin,vminutoFin = str(request.POST['horaFin']).split(":")
                vendedorFijo = VendedorFijo.objects.create(user=vendedor, horaInicio=vhoraInicio,minutoInicio=vminutoInicio,
                                                       horaFin=vhoraFin,minutoFin=vminutoFin)
                vendedorFijo.save()
            else:
                vendedorAmbulante = VendedorAmbulante.objects.create(user=vendedor)
                vendedorAmbulante.save()
        return render(request,'webpage/index.html')

    else:
         return render(request, 'webpage/signup.html', {
             'error': 'Nombre de usuario no disponible'
         })