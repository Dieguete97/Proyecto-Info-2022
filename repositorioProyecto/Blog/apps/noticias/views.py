from django.shortcuts import render

from .models import Noticia

def Listar(request):
	#Creo el diccionario para pasar datos al temaplte
	ctx = {}	
	#BUSCAR LO QUE QUIERO EN LA BD
	todas = Noticia.objects.all()
	#PASARLO AL TEMPLATE
	ctx['notis'] = todas

	return render(request,'noticias/listar_noticias.html',ctx)

# EJEMPLO DE COMO DESARMA EL CTX EL TEMPLATE.
# ctx['nombre'] = 'nicolas'
# ctx['notas'] = [5,6,9]
# EL TEMPLATE ya separa el diccionario
# nombre = 'nicolas'
# notas = [5,6,9]