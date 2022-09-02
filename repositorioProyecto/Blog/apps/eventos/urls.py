from django.urls import path, include
from . import views
app_name = "eventos"

urlpatterns = [
    path('ver/', views.ver_eventos, name = 'ver_eventos'),


    path('detalle/<int:pk>', views.Detalle_Evento_Clase.as_view(), name = 'detalle_eventos'),

]