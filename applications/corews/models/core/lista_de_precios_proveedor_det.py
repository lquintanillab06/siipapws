from django.db import models
import uuid

from .proveedor_producto import ProveedorProducto
from .lista_de_precios_proveedor import ListaDePreciosProveedor

class ListaDePreciosPorProveedorDet(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, editable= False)
    version = models.BigIntegerField()
    clave = models.CharField(max_length=255)
    unidad = models.CharField(max_length=255)
    precio_bruto = models.DecimalField(max_digits=19, decimal_places=2)
    precio_neto = models.DecimalField(max_digits=19, decimal_places=2)
    desc3 = models.DecimalField(max_digits=19, decimal_places=2)
    precio_anterior = models.DecimalField(max_digits=19, decimal_places=2)
    desc2 = models.DecimalField(max_digits=19, decimal_places=2)
    desc1 = models.DecimalField(max_digits=19, decimal_places=2)
    desc4 = models.DecimalField(max_digits=19, decimal_places=2)
    producto = models.ForeignKey(ProveedorProducto, models.DO_NOTHING)
    descripcion = models.CharField(max_length=255)
    lista = models.ForeignKey(ListaDePreciosProveedor, models.DO_NOTHING)
    partidas_idx = models.IntegerField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'lista_de_precios_proveedor_det'


