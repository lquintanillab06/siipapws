from django.db import models
import uuid

class Linea(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    version = models.BigIntegerField()
    activa = models.BooleanField(default=True)
    linea = models.CharField(unique=True, max_length=50)
    descripcion = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'linea'

