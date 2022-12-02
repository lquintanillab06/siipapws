from django.db import models
import uuid

from .clase import Clase
from .linea import Linea
from .marca import Marca
from .proveedor import Proveedor
from .producto_sat import ProductoSat
from .unidad_sat import UnidadSat

class Producto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    version = models.BigIntegerField()
    acabado = models.CharField(max_length=20, blank=True, null=True)
    activo = models.BooleanField(default=True)  
    ajuste = models.BigIntegerField()
    ancho = models.DecimalField(db_column='ANCHO', max_digits=19, decimal_places=3)  # Field name made lowercase.
    calibre = models.DecimalField(max_digits=19, decimal_places=2)
    caras = models.IntegerField()
    clase = models.ForeignKey(Clase, models.DO_NOTHING, blank=True, null=True)
    clave = models.CharField(max_length=255)
    codigo = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=15, blank=True, null=True)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    de_linea = models.BooleanField(default=True)
    descripcion = models.CharField(max_length=600, blank=True, null=True)
    fecha_lista = models.DateTimeField(blank=True, null=True)
    gramos = models.DecimalField(max_digits=19, decimal_places=2)
    inventariable = models.BooleanField(default=True)
    kilos = models.DecimalField(max_digits=19, decimal_places=3)
    largo = models.DecimalField(max_digits=19, decimal_places=3)
    linea = models.ForeignKey(Linea, models.DO_NOTHING, blank=True, null=True)
    m2xmillar = models.DecimalField(max_digits=19, decimal_places=3)
    marca = models.ForeignKey(Marca, models.DO_NOTHING, blank=True, null=True)
    modo_venta = models.CharField(max_length=1)
    nacional = models.BooleanField(default=True)
    precio_contado = models.DecimalField(max_digits=19, decimal_places=2)
    precio_credito = models.DecimalField(max_digits=19, decimal_places=2)
    presentacion = models.CharField(max_length=9)
    proveedor_favorito = models.ForeignKey(Proveedor, models.DO_NOTHING, blank=True, null=True)
    sw2 = models.BigIntegerField(blank=True, null=True)
    unidad = models.CharField(max_length=10)
    ''' clase_0 = models.CharField(db_column='clase', max_length=255, blank=True, null=True)  # Field renamed because of name conflict.
    linea_0 = models.CharField(db_column='linea', max_length=255, blank=True, null=True)  # Field renamed because of name conflict.
    marca_0 = models.CharField(db_column='marca', max_length=255, blank=True, null=True)  # Field renamed because of name conflict. '''
    producto_sat = models.ForeignKey(ProductoSat, models.DO_NOTHING, blank=True, null=True)
    unidad_sat = models.ForeignKey(UnidadSat, models.DO_NOTHING, blank=True, null=True)
    grupo_id = models.CharField(max_length=255, blank=True, null=True)
    tags = models.CharField(max_length=255, blank=True, null=True)
    hojas_paquete = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    paquete = models.IntegerField(blank=True, null=True)
    tipo_ecommerce = models.CharField(max_length=255, blank=True, null=True)
    clasificacion = models.CharField(max_length=255, blank=True, null=True)
    stock = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    activo_ecommerce = models.IntegerField(blank=True, null=True)
    clasificacion_ecommerce_id = models.BigIntegerField(blank=True, null=True)
    uso_ecommerce_id = models.BigIntegerField(blank=True, null=True)
    precio_tarjeta = models.DecimalField(max_digits=19, decimal_places=2, default= 0.00)  

    class Meta:
        managed = True
        db_table = 'producto'

 