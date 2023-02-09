from django.db import models
import uuid

from .complemento_ine import ComplementoIne

class ComplementoIneEntidad(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    version = models.BigIntegerField()
    ambito = models.CharField(max_length=7, blank=True, null=True)
    clave = models.CharField(max_length=10)
    complemento = models.ForeignKey(ComplementoIne, models.DO_NOTHING)
    partidas_idx = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'complemento_ine_entidad'