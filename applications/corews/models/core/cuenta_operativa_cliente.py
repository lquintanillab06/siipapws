from django.db import models

from .cliente import Cliente

# REVISADA, sin cambio (Vincula a cuenta_contable CHE, JUR y CRE*)

class CuentaOperativaCliente(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    cuenta_operativa = models.CharField(max_length=255)
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cuenta_operativa_cliente'
