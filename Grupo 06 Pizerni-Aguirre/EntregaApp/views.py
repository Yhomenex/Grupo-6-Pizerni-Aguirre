from django.shortcuts import render, HttpResponse
from EntregaApp.models import *
from EntregaApp.forms import *


#inicio
def inicio(request):
    return render(request, "EntregaApp/inicio.html")
    
#videojueogos
def videojuego(request):
    return render(request, "EntregaApp/videojuego.html")

#Formulario de Videojuegos
def videojuegoFormulario(request):
    
    if request.method == 'POST':
        formulario = VideojuegoFormulario(request.POST)
        if formulario.is_valid():
            input = formulario.cleaned_data
            videojuego = Videojuego(nombre=input['nombre'], categoria=input['categoria'])
            videojuego.save()
            return render(request, 'EntregaApp/videojuego.html') 
    else:
        formulario = VideojuegoFormulario()
   
    return render(request, 'EntregaApp/videojuegoFormulario.html', {'formulario':formulario})

#torneo
def torneo(request):
    return render(request, "EntregaApp/torneo.html")

#Formulario de Torneo            
def torneoFormulario(request):
    
    if request.method == 'POST':
        formulario = TorneoFormulario(request.POST)
        if formulario.is_valid():
            input = formulario.cleaned_data
            torneo = Torneo(nombre=input['nombre'], pais=input['pais'],premio=input['premio'],descripcion=input['descripcion'])
            torneo.save()
            return render(request, 'EntregaApp/torneo.html') 
    else:
        formulario = TorneoFormulario()
   
    return render(request, 'EntregaApp/torneoFormulario.html', {'formulario':formulario})

#equipos
def equipos(request):
    return render(request, "EntregaApp/equipos.html")
#Formulario de Equipos
def equiposFormulario(request):
    
    if request.method == 'POST':
        formulario = EquiposFormulario(request.POST)
        if formulario.is_valid():
            input = formulario.cleaned_data
            equipos = Equipo(nombre=input['nombre'], nacionalidad=input['nacionalidad'],cantidad_integrantes=input['cantidad_integrantes'])
            equipos.save()
            return render(request, 'EntregaApp/equipos.html') 
    else:
        formulario = EquiposFormulario()
   
    return render(request, 'EntregaApp/equiposFormulario.html', {'formulario':formulario})

#Busqueda y Resultado de Equipos
def equiposBusqueda(request):
    return render(request, 'EntregaApp/equiposBusqueda.html')

def equiposBusquedaResultado(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        equipos = Equipo.objects.filter(nombre__icontains=nombre)
        return render(request, 'EntregaApp/equiposBusquedaResultado.html', {"equipos":equipos, "nombre":nombre})
    else:
        output = f"ERROR: No se ingresó ningún nombre de Equipos"
    return HttpResponse(output)