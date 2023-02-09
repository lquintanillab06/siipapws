from django.db import models
import uuid

from cuenta_contable import CuentaContable

class CuentaDeudoraMapeo(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    deudor = models.CharField(max_length=255)
    contexto = models.CharField(max_length=255)
    cuenta = models.ForeignKey(CuentaContable, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cuenta_deudora_mapeo'
        unique_together = (('contexto', 'deudor', 'cuenta'),)