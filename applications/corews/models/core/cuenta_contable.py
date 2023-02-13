from django.db import models

# REVISADA y Sin Cambios, se bajo la columna de update_uer

class CuentaContable(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    cuenta_sat_id = models.CharField(max_length=255, blank=True, null=True)
    nivel = models.IntegerField()
    padre = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    clave = models.CharField(unique=True, max_length=100, blank=True, null=True)
    detalle = models.BooleanField(default=False)
    presentacion_financiera = models.BooleanField(default=False)
    presentacion_fiscal = models.BooleanField(default=False)
    sub_tipo = models.CharField(max_length=11)
    naturaleza = models.CharField(max_length=9)
    de_resultado = models.BooleanField(default=False)
    tipo = models.CharField(max_length=7)
    suspendida = models.BooleanField(default=False)
    presentacion_contable = models.BooleanField(default=False)
    descripcion = models.CharField(max_length=300)
    presentacion_presupuestal = models.BooleanField(default=False)
    create_user = models.CharField(max_length=255, blank=True, null=True)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cuenta_contable'