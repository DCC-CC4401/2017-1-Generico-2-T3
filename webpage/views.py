from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login



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


def log_intent(request):
	name = request.POST['nombre']
	passw = request.POST['password']
	user = authenticate( username=name, password=passw)
	if user is not None:
		login(request, user)
		return render(request, 'webpage/index.html')
        
	else:
		return render(request, 'webpage/login.html', {
		'error' : 'No ha ingresado un usuario y contraseña válidos'
		})


			



