from django.db import models
import uuid


class AnticipoSat(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, editable=False)
    version = models.BigIntegerField()
    total = models.DecimalField(max_digits=19, decimal_places=2)
    uuid = models.CharField(max_length=255)
    sucursal = models.CharField(max_length=255)
    cxc_documento = models.BigIntegerField()
    cfdi_folio = models.CharField(max_length=255)
    moneda = models.CharField(max_length=5)
    rfc = models.CharField(max_length=255)
    cfdi_serie = models.CharField(max_length=255)
    tipo_de_cambio = models.DecimalField(max_digits=19, decimal_places=6)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    disponible = models.DecimalField(max_digits=19, decimal_places=2)
    fecha = models.DateField()
    comentario = models.CharField(max_length=255, blank=True, null=True)
    impuesto = models.DecimalField(max_digits=19, decimal_places=2)
    nombre = models.CharField(max_length=255)
    cliente = models.CharField(max_length=255)
    cxc = models.CharField(max_length=255)
    importe = models.DecimalField(max_digits=19, decimal_places=2)
    create_user = models.CharField(max_length=255, blank=True, null=True)
    cfdi = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    last_updated = models.DateTimeField(auto_now=True,null=True)

    class Meta:
        managed = False
        db_table = 'anticipo_sat'