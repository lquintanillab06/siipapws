from re import A
from django.db import models
import uuid

# REVISADA, Se quito sw2, clave, comision_transferencia, cuenta_concentradora, rendimiento_tasa, plazo, inversion y tasa_isr

from .banco_sat import BancoSat
from .banco import Banco

class CuentaDeBanco(models.Model):
    
    id = models.UUIDField(primary_key=True, default= uuid.uuid4, editable= False)
    version = models.BigIntegerField()
    activo = models.BooleanField(default= False)
    banco_sat = models.ForeignKey(BancoSat, models.DO_NOTHING, blank=True, null=True)
    descripcion = models.CharField(max_length=255)
    impresion_template = models.CharField(max_length=50, blank=True, null=True)
    moneda = models.CharField(max_length=255)
    numero = models.CharField(max_length=30)
    sub_cuenta_operativa = models.CharField(max_length=4, blank=True, null=True)
    tipo = models.CharField(max_length=9)
    disponible_en_venta = models.BooleanField(default= False)
    disponible_en_pagos = models.BooleanField(default= False)
    proximo_cheque = models.BigIntegerField(blank=True, null=True)
    rfc = models.CharField(max_length=15, blank=True, null=True)
    banco = models.ForeignKey(Banco, models.DO_NOTHING, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    create_user = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cuenta_de_banco'