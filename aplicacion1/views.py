from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hola_mundo(request):
    return HttpResponse('Hola Marti Querido')


def saludar(request, nombre='user'):
    return HttpResponse(f"""
        <h1> Hola Queridisimo [{nombre}]                        
                        """)