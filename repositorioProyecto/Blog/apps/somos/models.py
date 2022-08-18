from django.db import models

# Create your models here.
class Somos(models.Model):
	titulo = models.CharField(max_length = 120)
	creado = models.DateField(auto_now_add = True)
	cuerpo = models.TextField()
	autor = models.CharField(max_length = 50, null=True, blank = True)
	imagen = models.ImageField(upload_to = 'somos', null=True, blank = True)


	def __str__(self):
		return self.titulo