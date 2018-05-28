#-*- coding: utf-8 -*-

''' 
o método match verifica se casou desdo o inicio
o método search  verifica se há determinados caracteres 
na string passada

match é bom para verificar padrões fixos como e-mails 
search é bom para fazer pesquisa na string
'''
import re

def casamento(regex,string):
	casou = re.search(regex, string)
	#casou = re.match(regex, string)
	if casou:
		print "Foi encontrado os caracteres >> ",casou.group()
	else:
		print " Não encontrou-se caracteres" 

# o \w indica a quantidade de letras as ser cadasdas junto ao al
casamento(r'al\w\w','alex lindo')
casamento(r'al\w\w\w','só 10')

#casando numeros
# no final 
casamento(r'\d{3}$','alex lindo 123')
# no inicio
casamento(r'^\d{3}','123 alex lindo')

# Se vai usar muitas vezes
# é bom fazer um objeto fixo

math = re.compile(r'\d{2}')
math.match('O  numero 10 foi encontrado 20 vezes')
if math ==None:
	print "nao casou"