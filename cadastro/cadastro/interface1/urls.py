# -*- coding: utf-8 -*-


from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ola, name='ola'),
    url(r'^$', views.nome, name='nome'),
]