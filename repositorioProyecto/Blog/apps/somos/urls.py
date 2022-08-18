from django.urls import path
from . import views
app_name = "somos"
urlpatterns = [
   
    path('quienes', views.Quienes, name = 'quienes_somos'),
    #     listar          Listar           listar_noticias


    ]