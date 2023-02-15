from django.db import models

# === REVISADA, Sin Uso Para Descontinuar y Elimnar ===

class SaldoCliente(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    cierre = models.DateField(blank=True, null=True)
    clave = models.CharField(max_length=255)
    saldo = models.FloatField()
    inicial = models.FloatField()
    ejercicio = models.IntegerField()
    rfc = models.CharField(max_length=255)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    abonos = models.FloatField()
    corte = models.DateField()
    cargos = models.FloatField()
    nombre = models.CharField(max_length=255)
    cliente = models.CharField(max_length=255)
    create_user = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'saldo_cliente'
        unique_together = (('ejercicio', 'cliente'),)