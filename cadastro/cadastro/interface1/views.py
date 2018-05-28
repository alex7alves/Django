# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def ola(request):
	response = HttpResponse
	return response('Olá mundo do Django')

def index(request):
	response = HttpResponse
	return response('Olá mundo do Django !!!')	