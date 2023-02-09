from django.db import models
import uuid


from ..core.sucursal import Sucursal

class FondoFijo(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    version = models.BigIntegerField()
    sucursal = models.ForeignKey(Sucursal, models.DO_NOTHING)
    rembolso = models.BooleanField(default=False)
    solicitud = models.CharField(max_length=255, blank=True, null=True)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    fecha = models.DateTimeField()
    comentario = models.CharField(max_length=255, blank=True, null=True)
    fondo = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    documento = models.CharField(max_length=255, blank=True, null=True)
    importe = models.DecimalField(max_digits=19, decimal_places=2)
    create_user = models.CharField(max_length=255, blank=True, null=True)
    solicitado = models.DateField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    last_updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        managed = False
        db_table = 'fondo_fijo'
