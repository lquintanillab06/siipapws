from django.db import models
import uuid

from .cliente import Cliente
from .socio import Socio

# Revisada y Modificada, se quito sw2

class ClienteCredito(models.Model):
    id = models.UUIDField(primary_key= True, default= uuid.uuid4, editable= False)
    version = models.BigIntegerField()
    atraso_maximo = models.BigIntegerField()
    cliente = models.OneToOneField(Cliente, on_delete= models.CASCADE)    
    credito_activo = models.BooleanField(default= True)
    descuento_fijo = models.DecimalField(max_digits=19, decimal_places=2)
    dia_cobro = models.BigIntegerField()
    dia_revision = models.BigIntegerField()
    linea_de_credito = models.DecimalField(max_digits=19, decimal_places=2)    
    plazo = models.BigIntegerField()
    postfechado = models.BooleanField(default= False)  
    revision = models.BooleanField(default= False) 
    saldo = models.DecimalField(max_digits=19, decimal_places=2)
    socio = models.ForeignKey(Socio, models.DO_NOTHING, blank=True, null=True)    
    vence_factura = models.BooleanField(default= True) 
    date_created = models.DateTimeField(auto_now_add=True, null= True)
    last_updated = models.DateTimeField(auto_now=True, null= True)

    

    class Meta:
        managed = True
        db_table = 'cliente_credito'