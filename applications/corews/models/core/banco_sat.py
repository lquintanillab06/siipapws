from django.db import models
import uuid

# Revisada y Modificada; date_created y last_updated

class BancoSat(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, editable= False)
    version = models.BigIntegerField()
    clave = models.CharField(unique=True, max_length=20)
    nombre_corto = models.CharField(max_length=255)
    razon_social = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True, null= True)
    last_updated = models.DateTimeField(auto_now=True , null=True)

    class Meta:
        managed = True
        db_table = 'banco_sat'