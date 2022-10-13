from django.urls import path, re_path
from . import views

urlpatterns = [
    # importa el orden en que declaro las rutas si maneja                rutas iguales
    path('hola_mundo', views.hola_mundo),
    path('saludar',views.saludar_default, name="saludar_default"),
    path('saludar/<str:nombre>', views.saludar, name="saludar"),
    re_path(r'^publicacion/(?P<anio>\d{2,4})/$',views.ver_publicaciones_anio), # expresion regular que recibe un parametro anio de tipo int y de 2 a 4 caract de long, cerra exp reg con signo $
    path('publicacion/<int:anio>/<int:mes>',views.ver_publicaciones, name="ver_publicaciones"),
    path('cursos/detalle/<slug:nombre_curso>/',views.cursos_detalle, name="curso_detalle"), #no recibe espacios en blanco o caracteres especiales
    re_path(r'^cursos/(?P<nombre>\w+)/$', views.cursos, name="cursos"), # restringe lo que recibe con una expresion regular \w+
    path('quienessomos/',views.quienes_somos, name="quienes_somos"),  # no recibe
    
    

       
]
