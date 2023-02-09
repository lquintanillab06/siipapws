from django.db import models
import uuid


class Antiguedad(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    version = models.BigIntegerField()
    de31_60 = models.FloatField()
    de61_90 = models.FloatField()
    date_created = models.DateTimeField()
    total = models.FloatField()
    last_updated = models.DateTimeField()
    saldo = models.FloatField()
    update_user = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    fecha = models.DateField()
    mas90 = models.FloatField()
    de1_30 = models.FloatField()
    por_vencer = models.FloatField()
    vencido = models.FloatField()
    create_user = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'antiguedad'
        unique_together = (('tipo', 'fecha'),)