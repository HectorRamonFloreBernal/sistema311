from django.contrib import admin
# importas el modelo libro
from .models import Libro

# Register your models here.

# registras el modelo libro
admin.site.register(Libro)