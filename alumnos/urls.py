from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('musica/', views.musica, name='musica'),
    path('deportes/', views.deportes, name='deportes'),
    path('postulacion/', views.formulario_postulacion, name='formulario_postulacion'),
    path('localstorage/', views.localstorage, name='localstorage'),
    path('pokemones/', views.pokemones, name='pokemones'),
    
    # Rutas para talentos individuales
    path('talento/antoniacastillo/', views.talento_antoniacastillo, name='talento_antoniacastillo'),
    path('talento/benjaminvargas/', views.talento_benjaminvargas, name='talento_benjaminvargas'),
    path('talento/isabellamendez/', views.talento_isabellamendez, name='talento_isabellamendez'),
    path('talento/luciafernandez/', views.talento_luciafernandez, name='talento_luciafernandez'),
    path('talento/matiassoto/', views.talento_matiassoto, name='talento_matiassoto'),
    path('talento/nicolasparedes/', views.talento_nicolasparedes, name='talento_nicolasparedes'),
    path('talento/sebastianrojas/', views.talento_sebastianrojas, name='talento_sebastianrojas'),
    path('talento/valentinarojas/', views.talento_valentinarojas, name='talento_valentinarojas'),
]