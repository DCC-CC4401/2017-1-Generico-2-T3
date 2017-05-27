from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import Http404

from webpage.models import Comprador,Vendedor,VendedorFijo ,VendedorAmbulante

def index(request):
    return render(request, 'webpage/index.html')


def login_user(request):
    return render(request, 'webpage/login.html')


def signup(request):
    return render(request, 'webpage/signup.html')


def perfil_vendedor(request, nombre_vendedor):
	fijo= False 
	try:		
		vendedor = VendedorFijo.objects.get(pk=nombre_vendedor)
		fijo=True
	except VendedorFijo.DoesNotExist:
		try:
			vendedor = VendedorAmbulante.objects.get(pk=nombre_vendedor)
		except VendedorAmbulante.DoesNotExist:
			raise Http404("No hay vendedores que tengan el nombre buscado")
	return render(request, 'webpage/vendedor-profile-page.html',{'vendedor' : vendedor , 'fijo' : fijo})


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
            mediosPago = request.POST.dict()
            valMediosPago = [False,False,False,False]
            print(mediosPago)
            if "Efectivo" in mediosPago:
                valMediosPago[0]=True
            if "Credito" in mediosPago:
                valMediosPago[1] = True
            if "Debito" in mediosPago:
                valMediosPago[2] = True
            if "Junaeb" in mediosPago:
                valMediosPago[3] = True
            vendedor = Vendedor.objects.create(user=usuario,acepta_Efectivo=valMediosPago[0],
                                               acepta_Credito = valMediosPago[1], acepta_Debito = valMediosPago[2],
                                               acepta_Junaeb = valMediosPago[3], avatar = request.FILES['perfil'])

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