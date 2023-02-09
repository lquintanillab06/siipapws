from django.db import models 
import uuid

class AntiguedadPorCliente(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    version = models.BigIntegerField()
    de31_60 = models.FloatField()
    de61_90 = models.FloatField()
    total = models.FloatField()
    cliente_id = models.CharField(max_length=255)
    tipo_vencimiento = models.CharField(max_length=255)
    saldo = models.FloatField()
    facturas = models.IntegerField()
    plazo = models.IntegerField()
    participacion = models.FloatField()
    update_user = models.CharField(max_length=255)
    atraso_maximo = models.IntegerField()
    tipo = models.CharField(max_length=255)
    fecha = models.DateField()
    mas90 = models.FloatField()
    de1_30 = models.FloatField()
    por_vencer = models.FloatField()
    limite_de_credito = models.FloatField()
    cliente = models.CharField(max_length=255)
    vencido = models.FloatField()
    create_user = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    last_updated = models.DateTimeField(auto_now=True,null=True)

    class Meta:
        managed = False
        db_table = 'antiguedad_por_cliente'
        unique_together = (('tipo', 'fecha', 'cliente_id'),)