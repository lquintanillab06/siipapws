from django.db import models
import uuid

# Revisada y Modificada

class Banco(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, editable= False)
    version = models.BigIntegerField()
    nacional = models.BooleanField( default= False)
    nombre = models.CharField(unique=True, max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'banco'