# -*- coding: utf-8 -*-
from datetime import time, datetime

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
    context = dict()
    user = get_object_or_404(User, username=nombre_vendedor)
    if hasattr(user, 'vendedor'):
        medios_pago = []
        if user.vendedor.acepta_Efectivo:
            medios_pago.append("Efectivo")
        if user.vendedor.acepta_Credito:
            medios_pago.append("Tarjeta de Crédito")
        if user.vendedor.acepta_Debito:
            medios_pago.append("Tarjeta de Débito")
        if user.vendedor.acepta_Junaeb:
            medios_pago.append("Tarjeta Junaeb")
        context['medios_pago'] = medios_pago
        
        
        favoritos = user.vendedor.comprador_set.all()
        context['favoritos'] = favoritos.count()



        if hasattr(user.vendedor, 'vendedorfijo'):
            context['vendedor'] = user.vendedor.vendedorfijo
            context['fijo'] = True
            horario_inicio = time(context['vendedor'].horaInicio, context['vendedor'].minutoInicio)
            horario_fin = time(context['vendedor'].horaFin, context['vendedor'].minutoFin)
            hora_actual = time(datetime.now().hour, datetime.now().minute)
            context['activo'] = hora_actual >= horario_inicio and hora_actual <= horario_fin
            context['horario_inicio'] = horario_inicio.strftime("%H:%M")
            context['horario_fin'] = horario_fin.strftime("%H:%M")
        else:
            context['vendedor'] = user.vendedor.vendedorambulante
            context['fijo'] = False
            context['activo'] = context['vendedor'].activo
    else:
        raise Http404("No hay vendedores que tengan el nombre buscado")
    return render(request, 'webpage/vendedor-profile-page.html',context)




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
        if hasattr(user, 'vendedor'):
            vendedor = Vendedor.objects.get(user=user)
            perfil = vendedor.avatar.url
            request.session['foto_perfil'] = perfil
        else:
            cliente = Comprador.objects.get(user=user)
            perfil = "../../static/img/AvatarEstudiante" + str(cliente.avatar) + ".png"
            request.session['foto_perfil'] = perfil
        return render(request, 'webpage/index.html')

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

                                               acepta_Junaeb = valMediosPago[3], avatar = request.FILES.get('fotoPerfil', None))

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




def gestion_usuario()

    return render(request, 'webpage/gestion-usuario.html')









