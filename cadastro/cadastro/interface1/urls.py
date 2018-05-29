# -*- coding: utf-8 -*-


from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ola, name='ola'),
    url(r'^$', views.nomeInit, name='nomeInit'),
    url(r'^(?P<nome>\w+)/$', views.nome, name='nome'),
]