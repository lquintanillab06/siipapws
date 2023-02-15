from django.db import models
import uuid

# REVISADA, se quito sw2

class PreciosPorClienteDet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    version = models.BigIntegerField()
    precio = models.DecimalField(max_digits=19, decimal_places=2)
    clave = models.CharField(max_length=255)
    moneda = models.CharField(max_length=255)
    costo = models.DecimalField(max_digits=19, decimal_places=2)
    tipo_de_cambio = models.CharField(max_length=255)
    precio_de_lista = models.DecimalField(max_digits=19, decimal_places=2)
    descuento = models.DecimalField(max_digits=19, decimal_places=2)
    precios_por_cliente_id = models.CharField(max_length=255)
    costop = models.DecimalField(max_digits=19, decimal_places=2)
    producto_id = models.CharField(max_length=255)    
    descripcion = models.CharField(max_length=255)
    precio_por_kilo = models.DecimalField(max_digits=19, decimal_places=2)
    costou = models.DecimalField(max_digits=19, decimal_places=2)
    partidas_idx = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'precios_por_cliente_det'