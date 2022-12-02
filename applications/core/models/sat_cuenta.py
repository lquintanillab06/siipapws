from django.db import models
import uuid


class SatCuenta(models.Model):
    id = models.BigIntegerField(primary_key=True)
    version = models.BigIntegerField()
    codigo = models.CharField(unique=True, max_length=20)
    nivel = models.IntegerField()
    nombre = models.CharField(max_length=255)
    tipo = models.CharField(max_length=100, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'sat_cuenta'