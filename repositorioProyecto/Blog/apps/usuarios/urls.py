from django.urls import path
from . import views
app_name = "usuarios"
urlpatterns = [
   
    path('usuarios', views.Usuario, name = 'usuario_asd'),

   
]

