from django.db import models
import uuid

class Marca(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    version = models.BigIntegerField()
    activa = models.BooleanField(default=True)
    marca = models.CharField(unique=True, max_length=20)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'marca'