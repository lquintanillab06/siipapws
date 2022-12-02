from django.db import models
import uuid

from .producto import Producto
from .lista_de_precios_por_proveedor import ListaDePreciosPorProveedor

class ListaDePreciosPorProveedorDet(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, editable= False)
    version = models.BigIntegerField()
    precio = models.DecimalField(max_digits=19, decimal_places=2)
    descuento1 = models.DecimalField(max_digits=19, decimal_places=2)
    moneda = models.CharField(max_length=255)
    precio_anterior = models.DecimalField(max_digits=19, decimal_places=2)
    descuento4 = models.DecimalField(max_digits=19, decimal_places=2)
    descuento_financiero = models.DecimalField(max_digits=19, decimal_places=2)
    descuento2 = models.DecimalField(max_digits=19, decimal_places=2)
    producto = models.ForeignKey(Producto, models.DO_NOTHING)
    descuento3 = models.DecimalField(max_digits=19, decimal_places=2)
    lista = models.ForeignKey(ListaDePreciosPorProveedor, models.DO_NOTHING)
    neto = models.DecimalField(max_digits=19, decimal_places=2)
    partidas_idx = models.IntegerField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'lista_de_precios_por_proveedor_det'


