from django.db import models

from .proveedor import Proveedor
from .producto import Producto
from .lista_precios_venta2 import ListaDePreciosVenta2

class ListaDePreciosVentaDet2(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    clave = models.CharField(max_length=255)
    incremento = models.DecimalField(max_digits=19, decimal_places=2)
    factor_credito = models.DecimalField(max_digits=19, decimal_places=2)
    precio_anterior_credito = models.DecimalField(max_digits=19, decimal_places=2)
    costo_ultimo = models.DecimalField(max_digits=19, decimal_places=2)
    proveedor = models.ForeignKey(Proveedor, models.DO_NOTHING, blank=True, null=True)
    precio_anterior_contado = models.DecimalField(max_digits=19, decimal_places=2)
    costo = models.DecimalField(max_digits=19, decimal_places=2)
    marca = models.CharField(max_length=255, blank=True, null=True)
    factor_contado = models.DecimalField(max_digits=19, decimal_places=2)
    clase = models.CharField(max_length=255, blank=True, null=True)
    precio_credito = models.DecimalField(max_digits=19, decimal_places=2)
    producto = models.ForeignKey(Producto, models.DO_NOTHING)
    descripcion = models.CharField(max_length=255)
    precio_contado = models.DecimalField(max_digits=19, decimal_places=2)
    lista = models.ForeignKey(ListaDePreciosVenta2, models.DO_NOTHING)
    linea = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'lista_de_precios_venta_det2'