# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def ola(request):
	return HttpResponse('Olá mundo do Django !!')

# nome passado de forma /?nome="Qulquer nome"
def nomeInit(request):
	name = request.GET.get('nome',' ')
	return HttpResponse('O valor passado foi %s'%name)

# Nome passado de fomra /"Quaquer nome"
def nome(request,nome):
	return HttpResponse('O nome passado foi %s'%nome)	