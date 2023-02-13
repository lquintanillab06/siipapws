from django.db import models
import uuid

# REVISADA, se quito la columna tipo

class CuentaSat(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, editable= False)
    version = models.BigIntegerField()
    codigo = models.CharField(unique=True, max_length=20)
    nivel = models.IntegerField()
    nombre = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'cuenta_sat'