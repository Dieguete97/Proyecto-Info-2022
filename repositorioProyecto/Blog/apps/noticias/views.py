from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from .models import Noticia,Comentario,Categoria
from django.db.models import Q


def listar_noticia(request):
	busqueda = request.GET.get("buscar",None)
	print(busqueda)
	if busqueda:
		noticias = Noticia.objects.filter(titulo__icontains = busqueda)
	else:
		noticias = Noticia.objects.all()
	print(noticias)
	return render(request, 'noticias/listar_noticias.html', {'notis':noticias})




#def Buscar(request):
	#creo el filtro de busqueda
#	queryset= request.GET.get("buscar")
#	categorias= Categoria.objects.all()
#	if queryset :
#		categorias= Noticia.objects.filter(
#			Q(Categoria__icontains= queryset) |
#			Q(Titulo__icontains= queryset)
#		).distinct()
#	return render(request, 'noticias/listar_noticias.html', {'Categorias': categorias})
	  

# EJEMPLO DE COMO DESARMA EL CTX EL TEMPLATE.
# ctx['nombre'] = 'nicolas'
# ctx['notas'] = [5,6,9]
# EL TEMPLATE ya separa el diccionario
# nombre = 'nicolas'
# notas = [5,6,9]

#VISTA BASADA EN FUNCIONES
@login_required
def Detalle_Noticia_Funcion(request, pk):
	ctx = {}
	noticia = Noticia.objects.get(pk = pk)
	ctx['resultado'] = noticia
	return render(request,'noticias/detalle_noticia.html',ctx)

#VISTA BASADA EN CLASES
class Detalle_Noticia_Clase(LoginRequiredMixin,DetailView):
	model = Noticia
	template_name = 'noticias/detalle_noticia.html'



#SI USO UNA VISTA BASADA EN CLASE EL CONTEXTO SE LLAMA:
# SI ES UNO SOLO object
# SI SON MUCHOS SE LLAMA obect_list

def Agregar_Comentario(request,pk):
	texto_comentario = request.POST.get('coment')
	
	#Forma 1 (es la mejor para este caso)
	noti = Noticia.objects.get(pk = pk)

	c = Comentario.objects.create(noticia = noti, texto = texto_comentario, usuario = request.user)

	return HttpResponseRedirect(reverse_lazy('noticias:detalle_noticias' , kwargs={'pk':pk}))
	
#Ejemplo de Dani
def busqueda_categorias(request):

	return render(request, "noticias/buscar_categoria.html")

def Buscar(request):

	if request.GET["prd"]:
		mensaje="Categoria buscada: %r" %request.GET["prd"] 
		return HttpResponse(mensaje)
		#noticia=request.GET["prd"]

		#categoria=categoria.objects.filter(nombre_icontains=producto)
	else:
		mensaje="No has introducido nada" 
	return HttpResponse(mensaje)
