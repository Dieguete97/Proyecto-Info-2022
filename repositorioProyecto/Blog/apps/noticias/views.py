from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from .models import Noticia,Comentario,Categoria
from django.db.models import Q


def Listar(request):
	busqueda = request.GET.get("buscar",None)
	print(busqueda)
	if busqueda:
		noticias = Noticia.objects.filter(categoria__nombre__icontains = busqueda)
	else:
		noticias = Noticia.objects.all()
	print(noticias)
	return render(request, 'noticias/listar_noticias.html', {'notis':noticias})


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
	
