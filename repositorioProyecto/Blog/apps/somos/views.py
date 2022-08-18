from django.shortcuts import render


from .models import Somos

def Quienes(request):
	#Creo el diccionario para pasar datos al temaplte
	ctx = {}	
	#BUSCAR LO QUE QUIERO EN LA BD
	todas = Somos.objects.all()
	#PASARLO AL TEMPLATE
	ctx['notis'] = todas

	return render(request,'somos/quienes_somos.html',ctx)


# Create your views here.
