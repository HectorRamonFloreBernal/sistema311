from django.shortcuts import render

# se importa el modulo HttpResponse para poder mostrar una respuesta en el navegador
from django.http import HttpResponse 
# Create your views here.

# Metodo para la pagina de inicio
def inicio(request):
    return HttpResponse("<h1>Hola Mundo Soy Tetor</h1>")

# Metodo para la pagina de nosotros
def nosotros(request):
    return render(request, "paginas/nosotros.html")