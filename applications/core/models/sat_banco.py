from django.db import models
import uuid

class SatBanco(models.Model):
    id = models.BigIntegerField(primary_key=True)
    version = models.BigIntegerField()
    clave = models.CharField(unique=True, max_length=20)
    nombre_corto = models.CharField(max_length=255)
    razon_social = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'sat_banco'