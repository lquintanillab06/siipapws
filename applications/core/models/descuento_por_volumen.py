from django.db import models
import uuid

class DescuentoPorVolumen(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, editable=False)
    version = models.BigIntegerField()
    descuento = models.DecimalField(max_digits=19, decimal_places=2)
    activo = models.BooleanField(default= False) 
    importe = models.DecimalField(max_digits=19, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'descuento_por_volumen'
