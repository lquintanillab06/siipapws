from django.db import models
import uuid


class ModuloTipo(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    version = models.BigIntegerField()
    tipo = models.CharField(max_length=255)
    modulo = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'modulo_tipo'
