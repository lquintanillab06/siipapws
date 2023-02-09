from django.db import models
import uuid

#from .vendedor import Vendedor
from .sucursal import Sucursal

class Cliente(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, editable= False)
    version = models.BigIntegerField(blank=True, null=True)
    activo = models.BooleanField(default= True)  
    cheque_devuelto = models.DecimalField(max_digits=19, decimal_places=2)
    clave = models.CharField(max_length=255)
    foliorfc = models.BigIntegerField()
    forma_de_pago = models.BigIntegerField()
    juridico = models.BooleanField(default= False)
    nombre = models.CharField(max_length=255)
    permite_cheque = models.BooleanField(default=False)
    rfc = models.CharField(max_length=13)
    sucursal = models.ForeignKey(Sucursal, models.DO_NOTHING, blank=True, null=True)
    sw2 = models.BigIntegerField(blank=True, null=True)
    #vendedor = models.ForeignKey(Vendedor, models.DO_NOTHING, blank=True, null=True)
    direccion_calle = models.CharField(max_length=200, blank=True, null=True)
    direccion_codigo_postal = models.CharField(max_length=255, blank=True, null=True)
    direccion_colonia = models.CharField(max_length=255, blank=True, null=True)
    direccion_estado = models.CharField(max_length=255, blank=True, null=True)
    direccion_latitud = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    direccion_longitud = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    direccion_municipio = models.CharField(max_length=255, blank=True, null=True)
    direccion_numero_exterior = models.CharField(max_length=50, blank=True, null=True)
    direccion_numero_interior = models.CharField(max_length=50, blank=True, null=True)
    direccion_pais = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    razon_social = models.CharField(max_length=255, blank=True, null=True)
    regimen_fiscal = models.CharField(max_length=255, blank=True, null=True)
    create_user = models.CharField(max_length=255, blank=True, null=True)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    last_updated = models.DateTimeField(auto_now=True,null= True)

   

    class Meta:
        managed = True
        db_table = 'cliente'

    @property
    def medios(self):
        return self.comunicaciones.all()