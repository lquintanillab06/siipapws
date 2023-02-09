from django.db import models
import uuid

from logistica.inventario import Inventario
from .venta import Venta
from ..core.sucursal import Sucursal
from ..core.producto import Producto


class VentaDet(models.Model):
    id = models.UUIDField(primary_key=True,default= uuid.uuid4, editable= False)
    version = models.BigIntegerField()
    total = models.DecimalField(max_digits=19, decimal_places=2)
    cantidad = models.DecimalField(max_digits=19, decimal_places=2)
    inventario = models.ForeignKey(Inventario, models.DO_NOTHING, blank=True, null=True)
    precio = models.DecimalField(max_digits=19, decimal_places=2)
    precio_original = models.DecimalField(max_digits=19, decimal_places=2)
    kilos = models.DecimalField(max_digits=19, decimal_places=2)
    venta = models.ForeignKey(Venta, models.DO_NOTHING)
    sucursal = models.ForeignKey(Sucursal, models.DO_NOTHING)
    descuento_original = models.DecimalField(max_digits=19, decimal_places=2)
    importe_cortes = models.DecimalField(max_digits=19, decimal_places=2)
    descuento_importe = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    nacional = models.BooleanField(default=True)
    descuento = models.DecimalField(max_digits=19, decimal_places=2)
    con_vale = models.BooleanField(default=False)
    precio_lista = models.DecimalField(max_digits=19, decimal_places=2)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    producto = models.ForeignKey(Producto, models.DO_NOTHING)
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    impuesto = models.DecimalField(max_digits=19, decimal_places=2)
    subtotal = models.DecimalField(max_digits=19, decimal_places=2)
    impuesto_tasa = models.DecimalField(max_digits=19, decimal_places=2)
    importe = models.DecimalField(max_digits=19, decimal_places=2)
    partidas_idx = models.IntegerField(blank=True, null=True)
    sin_existencia = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add= True,null=True)
    last_updated = models.DateTimeField(auto_now=True, null=True)
 

    class Meta:
        managed = False
        db_table = 'venta_det'