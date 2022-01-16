from django.urls import path
from EntregaApp import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('equipos/', views.equipos, name="equipo"),
    path('torneo/', views.torneo, name="torneo"),
    path('videojuego/', views.videojuego, name="videojuego"),
]
