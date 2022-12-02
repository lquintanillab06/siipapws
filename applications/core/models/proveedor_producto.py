from django.db import models
import uuid

from .producto import Producto
from .proveedor import Proveedor

class ProveedorProducto(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, editable= False)
    version = models.BigIntegerField()
    clave_proveedor = models.CharField(max_length=255, blank=True, null=True)
    codigo_proveedor = models.CharField(max_length=255, blank=True, null=True)
    descripcion_proveedor = models.CharField(max_length=255, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    paquete_tarima = models.IntegerField()
    pieza_paquete = models.IntegerField()
    precio = models.DecimalField(max_digits=19, decimal_places=2)
    producto = models.ForeignKey(Producto, models.DO_NOTHING)
    proveedor = models.ForeignKey(Proveedor, models.DO_NOTHING)
    precio_bruto = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    moneda = models.CharField(max_length=5, blank=True, null=True)
    desc3 = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    aplicado = models.DateTimeField(blank=True, null=True)
    desc2 = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    desc1 = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    desc4 = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    lista = models.BigIntegerField(blank=True, null=True)
    create_user = models.CharField(max_length=255, blank=True, null=True)
    suspendido = models.IntegerField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'proveedor_producto'