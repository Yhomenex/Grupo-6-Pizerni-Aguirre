from django.shortcuts import render, HttpResponse

# Create your views here.


def inicio(request):
    return render(request, "EntregaApp/inicio.html")
    
def equipos(request):
    return render(request, "EntregaApp/equipos.html")

def torneo(request):
    return render(request, "EntregaApp/torneo.html")

def videojuego(request):
    return render(request, "EntregaApp/videojuego.html")