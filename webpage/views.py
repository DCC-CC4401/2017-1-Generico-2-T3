from django.shortcuts import render


def index(request):
    return render(request, 'webpage/index.html')


def login(request):
    return render(request, 'webpage/login.html')


def signup(request):
    return render(request, 'webpage/signup.html')


def perfil_vendedor(request):
    return render(request, 'webpage/vendedor-profile-page.html')


def gestion_producto(request):
    return render(request, 'webpage/gestion-productos.html')
