from django.db import models 

class Cheque(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    entregado = models.DateField(blank=True, null=True)
    last_updated = models.DateTimeField()
    confidencial = models.TextField()  # This field type is a guess.
    update_user = models.CharField(max_length=255, blank=True, null=True)
    cobrado = models.DateField(blank=True, null=True)
    liberado = models.DateField(blank=True, null=True)
    folio = models.BigIntegerField()
    cancelado_comentario = models.CharField(max_length=255, blank=True, null=True)
    fecha = models.DateField()
    impresion = models.DateTimeField(blank=True, null=True)
    egreso = models.ForeignKey('MovimientoDeCuenta', models.DO_NOTHING, blank=True, null=True)
    cancelado = models.DateTimeField(blank=True, null=True)
    nombre = models.CharField(max_length=255)
    cuenta = models.ForeignKey('CuentaDeBanco', models.DO_NOTHING)
    importe = models.DecimalField(max_digits=19, decimal_places=2)
    create_user = models.CharField(max_length=255, blank=True, null=True)
    devolucion = models.ForeignKey('MovimientoDeCuenta', models.DO_NOTHING, blank=True, null=True)
    fecha_devolucion = models.DateTimeField(blank=True, null=True)
    cancelacion = models.DateTimeField(blank=True, null=True)
    comentario_cancelacion = models.CharField(max_length=255, blank=True, null=True)
    asignado = models.CharField(max_length=255, blank=True, null=True)
    fecha_transito = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cheque'