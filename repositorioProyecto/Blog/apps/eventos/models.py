from django.db import models

class Categoria(models.Model):
	nombre = models.CharField(max_length = 60)
	descripcion = models.CharField(max_length = 250, null = True, blank = True)

	def __str__(self):
		return self.nombre
		
class Evento(models.Model):
	titulo = models.CharField(max_length = 60)
	fecha = models.CharField(max_length = 60, null = True, blank = False)
	creado = models.DateField(auto_now_add = True)
	modalidad = models.CharField(max_length = 20, null = True, blank = False)
	lugar = models.CharField(max_length = 60, null = False, blank = False)
	cuerpo = models.TextField()
	categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE, null = True)
	
	def __str__(self):
		return self.titulo

