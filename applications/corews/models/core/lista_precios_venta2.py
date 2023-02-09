from django.db import models
import uuid


class ListaDePreciosVenta2(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    fecha = models.DateField()
    descripcion = models.CharField(max_length=255)
    moneda = models.CharField(max_length=255)
    inicio = models.DateTimeField(blank=True, null=True)
    aplicada = models.DateTimeField(blank=True, null=True)
    tipo_de_cambio = models.DecimalField(max_digits=19, decimal_places=6)
    create_user = models.CharField(max_length=255, blank=True, null=True)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        managed = False
        db_table = 'lista_de_precios_venta2'
