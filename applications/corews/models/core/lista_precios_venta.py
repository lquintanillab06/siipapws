from django.db import models
import uuid



class ListaDePreciosVenta(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, editable=False)
    version = models.BigIntegerField()
    folio = models.BigIntegerField(unique=True)
    tipo_de_cambio_dolar = models.DecimalField(max_digits=19, decimal_places=6)
    sw2 = models.BigIntegerField(blank=True, null=True)
    autorizacion = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.CharField(max_length=255)
    inicio = models.DateTimeField()
    aplicada = models.DateTimeField(blank=True, null=True)
    linea = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True,null=True)
    last_updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'lista_de_precios_venta'