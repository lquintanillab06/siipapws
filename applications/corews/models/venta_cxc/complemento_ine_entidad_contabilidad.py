from django.db import models
import uuid


class ComplementoIneEntidadContabilidad(models.Model):
    complemento_ine_entidad_id = models.CharField(max_length=255)
    contabilidad_integer = models.IntegerField(blank=True, null=True)
    contabilidad_idx = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'complemento_ine_entidad_contabilidad'
