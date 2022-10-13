from django.urls import path
from . import views

urlpatterns = [
   
    path('hola_mundo', views.hola_mundo),
    path('saludar', views.saludar, name="saludar_default"),
    path('saludar/<str:nombre>', views.saludar, name="saludar"),
       
]
