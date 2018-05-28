# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def ola(request):
	return HttpResponse('Olá mundo do Django !!')

def nome(request):
	name = request.GET.get('nome',' ')
	return HttpResponse('O nome passado foi %s'%name)