from django.db import models
import uuid

from .cliente import Cliente

# REVISADA, Para descontinuar y Ellimnar, no tiene uso

class CuentaBancaria(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable= False)
    version = models.BigIntegerField()
    activo = models.BooleanField(default=True)
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING)
    cuenta_habiente = models.CharField(max_length=255)
    numero_de_cuenta = models.CharField(max_length=255)
    pago_referenciado = models.CharField(max_length=255, blank=True, null=True)
    sw2 = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'cuenta_bancaria'