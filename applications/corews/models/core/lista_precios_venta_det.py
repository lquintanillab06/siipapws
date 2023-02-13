from django.db import models
import uuid

from .proveedor import Proveedor
from .producto import Producto
from .lista_precios_venta import ListaDePreciosVenta

# === REVISADA, Sin Uso Para Descontinuar y Elimnar ===

class ListaDePreciosVentaDet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False )
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
    producto = models.ForeignKey(Producto, models.DO_NOTHING)
    precio_contado = models.DecimalField(max_digits=19, decimal_places=2)
    lista = models.ForeignKey(ListaDePreciosVenta, models.DO_NOTHING)
    partidas_idx = models.IntegerField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    last_updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'lista_de_precios_venta_det'