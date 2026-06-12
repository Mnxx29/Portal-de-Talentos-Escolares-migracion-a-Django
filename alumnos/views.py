from django.shortcuts import render

# Create your views here.
# Definimos una funcion para la url de index

def index(request):
    return render(request, 'alumnos/index.html')

def musica(request):
    return render(request, 'alumnos/html/Musica.html')

def deportes(request):
    return render(request, 'alumnos/html/Deportes.html')

def formulario_postulacion(request):
    return render(request, 'alumnos/html/FormularioPostulacion.html')

def localstorage(request):
    return render(request, 'alumnos/html/localstorage.html')

def pokemones(request):
    return render(request, 'alumnos/html/pokemones.html')

# Vistas para talentos individuales
def talento_antoniacastillo(request):
    return render(request, 'alumnos/html/Talentos/AntoniaCastillo.html')

def talento_benjaminvargas(request):
    return render(request, 'alumnos/html/Talentos/BenjaminVargas.html')

def talento_isabellamendez(request):
    return render(request, 'alumnos/html/Talentos/IsabellaMendez.html')

def talento_luciafernandez(request):
    return render(request, 'alumnos/html/Talentos/LuciaFernandez.html')

def talento_matiassoto(request):
    return render(request, 'alumnos/html/Talentos/MatiasSoto.html')

def talento_nicolasparedes(request):
    return render(request, 'alumnos/html/Talentos/NicolasParedes.html')

def talento_sebastianrojas(request):
    return render(request, 'alumnos/html/Talentos/SebastianRojas.html')

def talento_valentinarojas(request):
    return render(request, 'alumnos/html/Talentos/ValentinaRojas.html')

