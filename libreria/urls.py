# Description: URLS de la app libreria
from django.urls import path 
# se importa las vistas de la app libreria
from . import views 
#  se crea una lista de url
urlpatterns = [

    # se crea la url para la pagina de inicio
    path('', views.inicio, name='inicio'),
    
    # se crea la url para la pagina de nosotros
    path('nosotros', views.nosotros, name='nosotros'),
]

