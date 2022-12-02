from django.contrib import admin

from .models.producto import Producto
from .models.cliente import Cliente
from .models.unidad_sat import UnidadSat

# Register your models here.

admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(UnidadSat)