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


def separar(regex,string):
	casou = re.search(regex, string)
	return casou

def casamentos(regex,string):
	strings = re.findall(regex,string)
	return strings






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

'''
 + -> 1 ou mais vezes
* 0 ou mais
? 0 ou 1
'''
casamento(r'\d+\w?', 'Foram 2047235s gastos')

# Pegar o email da frase
email =separar(r'([\w . \- _]+)@([\w . \- _]+)', 'o e-mail é joven_25@gmail.com')
print " o e-mail é ",email.group()
print "o login é ",email.group(1)
print "o domínio é ",email.group(2)


# Pegando e-mails de um arquivo
arquivo = open('Exemplo_emails.txt','r')
strings = casamentos(r'[\w . \- _]+@[\w . \- _]+',arquivo.read())
print 'Os e-mails do arquivo são :'
for em in strings:
	print em 