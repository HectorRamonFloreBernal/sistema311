# Description: URLS de la app libreria
from django.urls import path 
# se importa las vistas de la app libreria
from . import views 

# se importa el modulo settings para poder mostrar las imagenes
from django.conf import settings
from django.contrib.staticfiles.urls import static

 
#  se crea una lista de url
urlpatterns = [

# se crea la url para la pagina de inicio
    path('', views.inicio, name='inicio'),
    
# se crea la url para la pagina de nosotros
    path('nosotros', views.nosotros, name='nosotros'),

# se crea la url para la pagina de libros
    path('libros', views.libros, name='libros'),

# se crea la url para la pagina de crear
    path('libros/crear', views.crear, name='crear'),

# se crea la url para la pagina de editar
    path('libros/editar', views.editar, name='editar'),

# se crea la url para la pagina de borrar
    path('libros/borrar', views.borrar, name='borrar'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

