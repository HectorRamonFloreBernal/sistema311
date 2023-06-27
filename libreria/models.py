from django.db import models

# Create your models here.

#creas la clase libro 
# creas los campos de la tabla libro
# creas el campo imagen y se asignara a la carpeta imagenes
class Libro(models.Model):
    id          = models.AutoField(primary_key=True)
    titulo      = models.CharField(max_length=100, verbose_name="Titulo") 
    imagen      = models.ImageField(upload_to='imagenes/',verbose_name= "Imagen", null=True)
    descripcion = models.TextField(verbose_name= "Descripcion" ,null=True)
    
#retorna el titulo del libro en la tabla libro 
# muestra el contenido de la fila   
    def __str__(self): 
        fila = "Titulo: " + self.titulo + " -/- " + " Descripcion: " + self.descripcion
        return fila
# elimina la imagen de la carpeta imagenes      
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()