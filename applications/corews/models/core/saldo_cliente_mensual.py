from django.db import models


class SaldoClienteMensual(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    cierre = models.DateField(blank=True, null=True)
    devoluciones = models.IntegerField()
    saldo = models.FloatField()
    inicial = models.FloatField()
    saldo_ytd = models.FloatField()
    facturas = models.IntegerField()
    update_user = models.CharField(max_length=255, blank=True, null=True)
    abonos = models.FloatField()
    corte = models.DateField()
    fonificaciones_importe = models.FloatField()
    mes = models.IntegerField()
    cargos = models.FloatField()
    devolucines_importe = models.FloatField()
    facturas_importe = models.FloatField()
    create_user = models.CharField(max_length=255, blank=True, null=True)
    bonificaciones = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'saldo_cliente_mensual'