from django.db import models
import uuid 

from .cambio_precio import CambioDePrecio

class CambioDePrecioDet(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    last_updated = models.DateTimeField()
    precio_credito_anterior = models.DecimalField(max_digits=19, decimal_places=2)
    unidad = models.CharField(max_length=10)
    update_user = models.CharField(max_length=255)
    precio_contado_anterior = models.DecimalField(max_digits=19, decimal_places=2)
    precio_credito = models.DecimalField(max_digits=19, decimal_places=2)
    cambio = models.ForeignKey(CambioDePrecio, models.DO_NOTHING)
    producto = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=255)
    precio_contado = models.DecimalField(max_digits=19, decimal_places=2)
    create_user = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'cambio_de_precio_det'