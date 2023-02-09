from django.db import models
import uuid


from .proveedor import Proveedor


class ListaDePreciosProveedor(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4,editable= False)
    version = models.BigIntegerField()
    fecha_inicial = models.DateField()
    fecha_final = models.DateField()
    proveedor = models.ForeignKey(Proveedor, models.DO_NOTHING)
    sw2 = models.BigIntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    ejercicio = models.IntegerField()
    moneda = models.CharField(max_length=5)
    copia = models.BigIntegerField(blank=True, null=True)
    mes = models.IntegerField()
    aplicada = models.DateField(blank=True, null=True)
    create_user = models.CharField(max_length=255, blank=True, null=True)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'lista_de_precios_proveedor'