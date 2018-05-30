# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django import template

def index(request):	
	return render(request,'App2_templates/index.html',{'nome':'Alex'})


	
   

def idade(request,idade):
	template_string = '''
		{% if id >= 18 %}
			Você já é maior de idade
		{% else %}
			Você é de menor
		{% endif %}
		'''
	t = template.Template(template_string)
	c = template.Context({'id':int(idade)})
	return HttpResponse(t.render(c))