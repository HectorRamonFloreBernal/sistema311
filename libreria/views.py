from django.shortcuts import render

# se importa el modulo HttpResponse para poder mostrar una respuesta en el navegador
from django.http import HttpResponse 

# se importa el modelo Libro para poder mostrar los datos de la base de datos
from .models import Libro

# Create your views here.
#  Se crean los metodos para las diferentes vistas de la pagina

# Metodo para la pagina de inicio
def inicio(request):
    return render(request, "paginas/inicio.html")

# Metodo para la pagina de nosotros
def nosotros(request):
    return render(request, "paginas/nosotros.html")

# Metodo para la pagina de index
# Recibe los datos de la base de datos y los muestra en la pagina
def libros(request):
    
    # Se crea una variable que almacena todos los datos de la base de datos 
    libros = Libro.objects.all()
    # print(libros)
    # Se crea un diccionario que almacena los datos de la base de datos
    return render(request, "libros/index.html", {'libros': libros})

def crear(request):
    return render(request, "libros/crear.html")

def editar(request):
    return render(request, "libros/editar.html")

def borrar(request):
    return render(request, "libros/borrar.html")

#---------------------------

# Metodo para la pagina de usuario
def usuario(request):
    return render(request, "paginas/usuario.html")
