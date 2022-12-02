from django.db import models
import uuid

from .lista_de_precios_venta import ListaDePreciosVenta
from .proveedor import Proveedor
from .producto import Producto


class ListaDePreciosVentaDet(models.Model):
    id = models.UUIDField(primary_key=True,default= uuid.uuid4, editable= False)
    version = models.BigIntegerField()
    incremento = models.DecimalField(max_digits=19, decimal_places=2)
    factor_credito = models.DecimalField(max_digits=19, decimal_places=2)
    precio_anterior_credito = models.DecimalField(max_digits=19, decimal_places=2)
    costo_ultimo = models.DecimalField(max_digits=19, decimal_places=2)
    proveedor = models.ForeignKey(Proveedor, models.DO_NOTHING, blank=True, null=True)
    precio_anterior_contado = models.DecimalField(max_digits=19, decimal_places=2)
    costo = models.DecimalField(max_digits=19, decimal_places=2)
    factor_contado = models.DecimalField(max_digits=19, decimal_places=2)
    precio_credito = models.DecimalField(max_digits=19, decimal_places=2)
    producto = models.ForeignKey(Producto, models.DO_NOTHING, null=True)
    precio_contado = models.DecimalField(max_digits=19, decimal_places=2)
    lista = models.ForeignKey(ListaDePreciosVenta,on_delete= models.CASCADE, related_name= 'detalles')
    partidas_idx = models.IntegerField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'lista_de_precios_venta_det'