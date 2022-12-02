from django.db import models
import uuid


from .proveedor import Proveedor


class ListaDePreciosPorProveedor(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4,editable= False)
    version = models.BigIntegerField()
    fecha_inicial = models.DateField()
    fecha_final = models.DateField()
    descuento_financiero = models.DecimalField(max_digits=19, decimal_places=2)
    proveedor = models.ForeignKey(Proveedor, models.DO_NOTHING)
    sw2 = models.BigIntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    linea = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'lista_de_precios_por_proveedor'