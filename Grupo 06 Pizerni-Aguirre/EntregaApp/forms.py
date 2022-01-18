from django import forms

class VideojuegoFormulario(forms.Form):
    nombre=forms.CharField(max_length=40)
    categoria=forms.CharField(max_length=40)

class TorneoFormulario(forms.Form):
    nombre=forms.CharField(max_length=40)
    pais=forms.CharField(max_length=40)
    premio=forms.IntegerField()
    descripcion=forms.CharField(max_length=40)
    

class EquiposFormulario(forms.Form):
    nombre=forms.CharField(max_length=40)
    nacionalidad=forms.CharField(max_length=40)
    cantidad_integrantes=forms.IntegerField()
