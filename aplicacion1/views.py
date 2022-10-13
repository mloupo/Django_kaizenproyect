from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
def hola_mundo(request):
    return HttpResponse('Hola Marti Querido')


def saludar(request, nombre):
    return HttpResponse(f"""
        <h1> Hola Queridisimo [{nombre}]                        
        """)

def saludar_default(request, nombre='user'):
    return HttpResponse(f"""
        <h1> Hola Queridisimo [{nombre}]                        
        """)

def ver_publicaciones_anio(request, anio):
    return HttpResponse(f"""
        <h1> publicaciones del año {anio}</h1>
        <p>Listado de pulicaciones</p>                        
                        """)

    
def ver_publicaciones(request, anio, mes=1):
    return HttpResponse(f"""
        <h1> publicaciones de {mes}/ {anio}</h1>
        <p>Listado de pulicaciones</p>                        
                        """)
    

def cursos_detalle(request, nombre_curso):
    return HttpResponse(f"""
                        <h1>{nombre_curso}</h1>
                        """)
    

def cursos(request, nombre):
    return HttpResponse(f"""
        <h2>{nombre}</h2>
        """)


def quienes_somos(request):
    #return redirect('saludar_default')
    return redirect(reverse('saludar', kwargs={'nombre': 'Estanislao'}))
