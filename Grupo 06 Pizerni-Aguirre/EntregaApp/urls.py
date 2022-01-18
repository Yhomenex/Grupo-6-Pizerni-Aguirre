from django.urls import path
from EntregaApp import views

urlpatterns = [
    #Inicio
    path('', views.inicio, name="inicio"),
    
    #Seccion Videojuegos
    path('videojuego/', views.videojuego, name="videojuego"),
    path('videojuegoFormulario',views.videojuegoFormulario, name="videojuegoFormulario"),
    
    #Seccion Torneos
    path('torneo/', views.torneo, name="torneo"),
    path('torneoFormulario',views.torneoFormulario, name="torneoFormulario" ),
    
    #Seccion Equipos
    path('equipos/', views.equipos, name="equipo"),
    path('equiposFormulario',views.equiposFormulario, name="equiposFormulario"),
    path('equiposBusqueda',views.equiposBusqueda, name='equiposBusqueda'),
    path('equiposBusquedaResultado/', views.equiposBusquedaResultado, name="equipoBusquedaResultado"),
]

