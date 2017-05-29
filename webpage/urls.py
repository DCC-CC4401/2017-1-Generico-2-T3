# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^login$', views.login_user, name='login'),

    url(r'^logout$', views.logout_intent, name='logout'),
    url(r'^login/logtry$', views.login_intent, name='logtry'),
    url(r'^signup$', views.signup, name='signup'),
    url(r'^signup/regtry$', views.reg_intent, name='regtry'),
    url(r'^vendedor/(?P<nombre_vendedor>\w+)$', views.perfil_vendedor, name='perfil_vendedor'),
    url(r'^producto$', views.gestion_producto, name='gestion_producto'),

    url(r'^miPerfil$', views.gestion_usuario, name='miPerfil'),
    url(r'^miPerfil/cambios$', views.cambios_exitosos, name='cambios_exitosos'),


    url(r'^producto/addtry$', views.agregar_producto, name='addtry'),
    url(r'^producto/(?P<pk_producto>\w+)$', views.editar_producto, name='editarProducto'),
    url(r'^actualizarProducto/(?P<pk_producto>\w+)$', views.actualizar_producto, name='actualizarProducto'),
    url(r'^eliminarProducto/(?P<pk_producto>\w+)$', views.eliminar_producto, name='eliminarProducto'),
    url(r'^checkswitch$', views.checkswitch, name='checkswitch'),
    url(r'^favoritos/(?P<nombre_vendedor>\w+)?', views.gestion_favoritos, name='gestion_favoritos')


    

    
]
