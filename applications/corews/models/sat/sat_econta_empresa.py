from django.db import models
import uuid



class SatEcontaEmpresa(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    version = models.BigIntegerField()
    sql_auxiliar_folios = models.TextField(blank=True, null=True)
    sql_auxiliar_cuentas = models.TextField(blank=True, null=True)
    clave = models.CharField(max_length=255)
    certificado_digital = models.TextField(blank=True, null=True)
    certificado = models.CharField(max_length=255)
    rfc = models.CharField(max_length=13)
    razon_social = models.CharField(max_length=255)
    data_base_url = models.CharField(max_length=255)
    llave_privada = models.TextField(blank=True, null=True)
    username = models.CharField(max_length=255)
    sql_catalogo = models.TextField(blank=True, null=True)
    password = models.CharField(max_length=255)
    sql_balanza = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    last_updated = models.DateTimeField(auto_now=True, null= True)

    class Meta:
        managed = False
        db_table = 'sat_econta_empresa'
        unique_together = (('rfc', 'clave'),)