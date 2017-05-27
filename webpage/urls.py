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

]
