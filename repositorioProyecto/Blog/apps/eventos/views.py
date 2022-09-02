from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


from .models import Evento

def ver_eventos(request):
	busqueda = request.GET.get("buscar",None)
	print(busqueda)
	if busqueda:
		evento = Evento.objects.filter(categoria__nombre__icontains = busqueda)
	else:
		evento = Evento.objects.all()
	print(evento)
	return render(request, 'eventos/ver_eventos.html', {'resultado':evento})

class Detalle_Evento_Clase(DetailView):
	model = Evento
	template_name = 'eventos/detalle_eventos.html'