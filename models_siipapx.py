# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AbonoCxp(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    total = models.DecimalField(max_digits=19, decimal_places=4)
    last_updated = models.DateTimeField()
    moneda = models.CharField(max_length=255)
    proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING)
    tipo_de_cambio = models.DecimalField(max_digits=19, decimal_places=6)
    fecha = models.DateField()
    comentario = models.CharField(max_length=255, blank=True, null=True)
    sw2 = models.BigIntegerField(blank=True, null=True)
    documento = models.CharField(max_length=255)
    class_field = models.CharField(db_column='class', max_length=255)  # Field renamed because it was a Python reserved word.
    requisicion = models.ForeignKey('Requisicion', models.DO_NOTHING, blank=True, null=True)
    egreso = models.ForeignKey('MovimientoDeCuenta', models.DO_NOTHING, blank=True, null=True)
    comprobante = models.OneToOneField('ComprobanteFiscal', models.DO_NOTHING, blank=True, null=True)
    impuesto = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    concepto = models.CharField(max_length=255, blank=True, null=True)
    importe = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'abono_cxp'


class ActividadAlmacen(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.IntegerField()
    last_updated = models.DateTimeField()
    actividad = models.CharField(max_length=9)
    fin = models.DateTimeField()
    comentario = models.CharField(max_length=255)
    date_created = models.DateTimeField()
    inicio = models.DateTimeField()
    asigno = models.ForeignKey('User', models.DO_NOTHING)
    evaluacion = models.IntegerField()
    empleado = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'actividad_almacen'


class Acuse(models.Model):
    id = models.BigIntegerField(primary_key=True)
    version = models.BigIntegerField()
    comprobante_fiscal = models.ForeignKey('ComprobanteFiscal', models.DO_NOTHING)
    date_created = models.DateTimeField()
    codigo_estatus = models.CharField(max_length=100)
    uuid = models.CharField(unique=True, max_length=255)
    last_updated = models.DateTimeField()
    url = models.CharField(max_length=255)
    estado = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'acuse'


class Alcance(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    nacional = models.TextField()  # This field type is a guess.
    pedidos_pendiente = models.DecimalField(max_digits=19, decimal_places=2)
    existencia = models.DecimalField(max_digits=19, decimal_places=2)
    fin = models.DateTimeField()
    kilos = models.DecimalField(max_digits=19, decimal_places=2)
    producto = models.ForeignKey('Producto', models.DO_NOTHING)
    venta = models.DecimalField(max_digits=19, decimal_places=2)
    devolucion_venta = models.DecimalField(max_digits=19, decimal_places=2)
    sucursal = models.ForeignKey('Sucursal', models.DO_NOTHING)
    inicio = models.DateTimeField()
    existencia_en_toneladas = models.DecimalField(max_digits=19, decimal_places=4)
    fecha_inicial = models.DateField()
    date_created = models.DateTimeField()
    clave = models.CharField(max_length=255)
    unidad = models.CharField(max_length=255)
    prom_vta_en_toneladas = models.DecimalField(max_digits=19, decimal_places=4)
    last_updated = models.DateTimeField()
    sucursal_0 = models.CharField(db_column='sucursal', max_length=255)  # Field renamed because of name conflict.
    alcance = models.DecimalField(max_digits=19, decimal_places=4)
    fecha_final = models.DateField()
    proveedor = models.CharField(max_length=255, blank=True, null=True)
    marca = models.CharField(max_length=255, blank=True, null=True)
    compras_pendientes = models.DecimalField(max_digits=19, decimal_places=4)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    clase = models.CharField(max_length=255, blank=True, null=True)
    prom_vta = models.DecimalField(max_digits=19, decimal_places=4)
    fecha = models.DateField()
    comentario = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.CharField(max_length=255)
    prom_vta_en_tonelada = models.DecimalField(max_digits=19, decimal_places=4)
    meses = models.IntegerField()
    meses_periodo = models.DecimalField(max_digits=19, decimal_places=4)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    linea = models.CharField(max_length=255, blank=True, null=True)
    create_user = models.CharField(max_length=255, blank=True, null=True)
    de_linea = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'alcance'
        unique_together = (('fecha', 'sucursal_0', 'clave'),)


class AnalisisDeFactura(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    factura = models.ForeignKey('CuentaPorPagar', models.DO_NOTHING)
    date_created = models.DateTimeField()
    fecha = models.DateField()
    comentario = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField()
    sw2 = models.BigIntegerField(blank=True, null=True)
    importe = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'analisis_de_factura'


class AnalisisDeFacturaDet(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    cantidad = models.DecimalField(max_digits=19, decimal_places=2)
    last_updated = models.DateTimeField()
    entrada = models.ForeignKey('RecepcionDeCompraDet', models.DO_NOTHING)
    desc3 = models.DecimalField(max_digits=19, decimal_places=4)
    desc2 = models.DecimalField(max_digits=19, decimal_places=4)
    desc1 = models.DecimalField(max_digits=19, decimal_places=4)
    precio_de_lista = models.DecimalField(max_digits=19, decimal_places=2)
    desc4 = models.DecimalField(max_digits=19, decimal_places=4)
    analisis = models.ForeignKey(AnalisisDeFactura, models.DO_NOTHING)
    costo_unitario = models.DecimalField(max_digits=19, decimal_places=6)
    sw2 = models.BigIntegerField(blank=True, null=True)
    importe = models.DecimalField(max_digits=19, decimal_places=2)
    partidas_idx = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'analisis_de_factura_det'


class AnalisisDevolucionCompra(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'analisis_devolucion_compra'


class AplicacionCxp(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    cxp = models.ForeignKey('CuentaPorPagar', models.DO_NOTHING)
    date_created = models.DateTimeField()
    fecha = models.DateField()
    comentario = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField()
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    abono = models.ForeignKey(AbonoCxp, models.DO_NOTHING)
    importe = models.DecimalField(max_digits=19, decimal_places=2)
    class_field = models.CharField(db_column='class', max_length=255)  # Field renamed because it was a Python reserved word.
    aplicaciones_idx = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aplicacion_cxp'


class AplicacionDeCobro(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    cobro = models.ForeignKey('Cobro', models.DO_NOTHING, blank=True, null=True)
    last_updated = models.DateTimeField()
    update_user = models.CharField(max_length=255, blank=True, null=True)
    fecha = models.DateField()
    cuenta_por_cobrar = models.ForeignKey('CuentaPorCobrar', models.DO_NOTHING)
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    nota_de_credito = models.ForeignKey('NotaDeCredito', models.DO_NOTHING, blank=True, null=True)
    importe = models.DecimalField(max_digits=19, decimal_places=2)
    create_user = models.CharField(max_length=255, blank=True, null=True)
    aplicaciones_idx = models.IntegerField(blank=True, null=True)
    forma_de_pago = models.CharField(max_length=255, blank=True, null=True)
    recibo = models.CharField(max_length=255, blank=True, null=True)
    moneda = models.CharField(max_length=3, blank=True, null=True)
    tipo_de_cambio = models.DecimalField(max_digits=19, decimal_places=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aplicacion_de_cobro'


class AppConfig(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    cfdi_location = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField()
    last_updated = models.DateTimeField()
    sucursal = models.ForeignKey('Sucursal', models.DO_NOTHING)
    envio_de_correos_activo = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'app_config'


class AsignacionActividad(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    actividad = models.CharField(max_length=15)
    fin = models.DateTimeField(blank=True, null=True)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    inicio = models.DateTimeField(blank=True, null=True)
    asigno = models.ForeignKey('User', models.DO_NOTHING)
    evaluacion = models.IntegerField()
    empleado = models.ForeignKey('User', models.DO_NOTHING)
    termino = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asignacion_actividad'


class Audit(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    persisted_object_id = models.CharField(max_length=255, blank=True, null=True)
    date_replicated = models.DateTimeField(blank=True, null=True)
    target = models.CharField(max_length=255, blank=True, null=True)
    message = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField()
    last_updated = models.DateTimeField()
    name = models.CharField(max_length=255, blank=True, null=True)
    event_name = models.CharField(max_length=255, blank=True, null=True)
    table_name = models.CharField(max_length=255, blank=True, null=True)
    source = models.CharField(max_length=255, blank=True, null=True)
    registros = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'audit'


class AuditLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    persisted_object_id = models.CharField(max_length=255, blank=True, null=True)
    date_replicated = models.DateTimeField(blank=True, null=True)
    target = models.CharField(max_length=255, blank=True, null=True)
    message = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    event_name = models.CharField(max_length=255, blank=True, null=True)
    table_name = models.CharField(max_length=255, blank=True, null=True)
    source = models.CharField(max_length=255, blank=True, null=True)
    replicated_cloud = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'audit_log'


class Autorizacion(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    solicito = models.CharField(max_length=255)
    autorizo = models.CharField(max_length=255)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    fecha_de_autorizacion = models.DateField()
    fecha = models.DateField()
    last_updated = models.DateTimeField()
    class_field = models.CharField(db_column='class', max_length=255)  # Field renamed because it was a Python reserved word.

    class Meta:
        managed = False
        db_table = 'autorizacion'


class AutorizacionDeVenta(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    tipo = models.CharField(max_length=18)
    fecha = models.DateField()
    solicito = models.CharField(max_length=255)
    autorizo = models.CharField(max_length=255)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField()
    venta = models.ForeignKey('Venta', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'autorizacion_de_venta'


class AuxiliarCorte(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    corte = models.ForeignKey('Corte', models.DO_NOTHING)
    date_created = models.DateTimeField()
    tipo = models.CharField(max_length=9)
    auxiliar_corte = models.ForeignKey('User', models.DO_NOTHING)
    auxiliares_idx = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auxiliar_corte'


class AuxiliarSurtido(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    surtido = models.ForeignKey('Surtido', models.DO_NOTHING)
    nombre = models.CharField(max_length=255)
    auxiliares_idx = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auxiliar_surtido'


class Banco(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    nacional = models.TextField(blank=True, null=True)  # This field type is a guess.
    banco_sat = models.ForeignKey('BancoSat', models.DO_NOTHING, blank=True, null=True)
    sw2 = models.BigIntegerField(blank=True, null=True)
    nombre = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'banco'


class BancoSat(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    clave = models.CharField(unique=True, max_length=20)
    nombre_corto = models.CharField(max_length=255)
    razon_social = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'banco_sat'


class Bonificacionmc(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    suspendido_comentario = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField()
    autorizado = models.DateField(blank=True, null=True)
    ultima_venta = models.DateField()
    last_updated = models.DateTimeField()
    ajuste = models.DecimalField(max_digits=19, decimal_places=2)
    bono = models.DecimalField(max_digits=19, decimal_places=2)
    ejercicio = models.IntegerField()
    aplicado = models.DecimalField(max_digits=19, decimal_places=2)
    ultima_aplicacion = models.DateField(blank=True, null=True)
    facturas = models.DecimalField(max_digits=19, decimal_places=2)
    fecha = models.DateField()
    mes = models.IntegerField()
    vencimiento = models.DateField(blank=True, null=True)
    vigencia_dias = models.IntegerField()
    suspendido = models.DateField(blank=True, null=True)
    posicion = models.IntegerField()
    ventas_kilos = models.DecimalField(max_digits=19, decimal_places=2)
    ventas = models.DecimalField(max_digits=19, decimal_places=2)
    nombre = models.CharField(max_length=255)
    cliente = models.ForeignKey('Cliente', models.DO_NOTHING)
    importe = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'bonificacionmc'


class Bonificacionmcaplicacion(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    cobro = models.CharField(max_length=255)
    uuid = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField()
    sucursal = models.CharField(max_length=255)
    nota_fecha = models.DateField(blank=True, null=True)
    nota_serie = models.CharField(max_length=255, blank=True, null=True)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    fecha = models.DateField()
    bonificacion = models.ForeignKey(Bonificacionmc, models.DO_NOTHING)
    nota_folio = models.CharField(max_length=255, blank=True, null=True)
    importe = models.DecimalField(max_digits=19, decimal_places=2)
    create_user = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bonificacionmcaplicacion'


class CancelacionCfdi(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    motivo = models.CharField(max_length=255)
    date_created = models.DateTimeField()
    last_updated = models.DateTimeField()
    acuse = models.CharField(max_length=255, blank=True, null=True)
    create_user = models.CharField(max_length=100, blank=True, null=True)
    cfdi = models.ForeignKey('Cfdi', models.DO_NOTHING)
    update_user = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cancelacion_cfdi'


class Cfdi(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    total = models.DecimalField(max_digits=19, decimal_places=2)
    uuid = models.CharField(unique=True, max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField()
    emisor = models.CharField(max_length=255)
    tipo_de_comprobante = models.CharField(max_length=1)
    serie = models.CharField(max_length=30, blank=True, null=True)
    file_name = models.CharField(max_length=150)
    origen = models.CharField(max_length=12)
    version_cfdi = models.CharField(max_length=3)
    folio = models.CharField(max_length=30, blank=True, null=True)
    fecha = models.DateTimeField()
    receptor = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    receptor_rfc = models.CharField(max_length=13)
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    emisor_rfc = models.CharField(max_length=13)
    status = models.CharField(max_length=255, blank=True, null=True)
    cancelado = models.TextField(blank=True, null=True)  # This field type is a guess.
    enviado = models.DateTimeField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    xml_url = models.CharField(max_length=255, blank=True, null=True)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    pdf_url = models.CharField(max_length=255, blank=True, null=True)
    create_user = models.CharField(max_length=255, blank=True, null=True)
    uuid_relacionado = models.CharField(max_length=255, blank=True, null=True)
    tipo_de_relacion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cfdi'


class CfdiCancelado(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    folio = models.CharField(max_length=30)
    message = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField()
    uuid = models.CharField(unique=True, max_length=255)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField()
    serie = models.CharField(max_length=30)
    aka = models.TextField()
    create_user = models.CharField(max_length=255, blank=True, null=True)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    status_sat = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'cfdi_cancelado'


class Cheque(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    folio = models.IntegerField()
    date_created = models.DateTimeField()
    devolucion = models.ForeignKey('MovimientoDeCuenta', models.DO_NOTHING, blank=True, null=True)
    impresion = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField()
    egreso = models.ForeignKey('MovimientoDeCuenta', models.DO_NOTHING)
    fecha_devolucion = models.DateTimeField(blank=True, null=True)
    cancelacion = models.DateTimeField(blank=True, null=True)
    comentario_cancelacion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cheque'


class ChequeDevuelto(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    cheque = models.ForeignKey('CobroCheque', models.DO_NOTHING)
    total = models.DecimalField(max_digits=19, decimal_places=2)
    tipo_documento = models.CharField(max_length=255, blank=True, null=True)
    forma_de_pago = models.CharField(max_length=255)
    last_updated = models.DateTimeField()
    sucursal = models.ForeignKey('Sucursal', models.DO_NOTHING)
    moneda = models.CharField(max_length=255)
    tipo_de_cambio = models.DecimalField(max_digits=19, decimal_places=6)
    update_user = models.CharField(max_length=255)
    fecha = models.DateTimeField()
    cuenta_por_cobrar = models.ForeignKey('CuentaPorCobrar', models.DO_NOTHING, blank=True, null=True)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    impuesto = models.DecimalField(max_digits=19, decimal_places=2)
    documento = models.BigIntegerField()
    cliente = models.ForeignKey('Cliente', models.DO_NOTHING)
    importe = models.DecimalField(max_digits=19, decimal_places=2)
    create_user = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'cheque_devuelto'


class Chofer(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    celular = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    last_updated_by = models.CharField(max_length=255, blank=True, null=True)
    mail = models.CharField(max_length=255, blank=True, null=True)
    nombre = models.CharField(max_length=255)
    rfc = models.CharField(max_length=255, blank=True, null=True)
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    activo = models.IntegerField(blank=True, null=True)
    comision = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    precio_tonelada = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    facturista_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chofer'


class ChoferUbicacion(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    chofer = models.ForeignKey(Chofer, models.DO_NOTHING)
    embarque = models.ForeignKey('Embarque', models.DO_NOTHING, blank=True, null=True)
    fecha = models.DateTimeField()
    incidencia = models.CharField(max_length=255, blank=True, null=True)
    latitud = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    longitud = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    sucursal = models.ForeignKey('Sucursal', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'chofer_ubicacion'


class Clase(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    activa = models.TextField()  # This field type is a guess.
    clase = models.CharField(unique=True, max_length=50)
    date_created = models.DateTimeField()
    last_updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'clase'


class Cliente(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    activo = models.TextField()  # This field type is a guess.
    cheque_devuelto = models.DecimalField(max_digits=19, decimal_places=2)
    clave = models.CharField(max_length=255)
    date_created = models.DateTimeField(blank=True, null=True)
    foliorfc = models.BigIntegerField()
    forma_de_pago = models.BigIntegerField()
    juridico = models.TextField()  # This field type is a guess.
    last_updated = models.DateTimeField(blank=True, null=True)
    nombre = models.CharField(max_length=255)
    permite_cheque = models.TextField()  # This field type is a guess.
    rfc = models.CharField(max_length=13)
    sucursal = models.ForeignKey('Sucursal', models.DO_NOTHING, blank=True, null=True)
    sw2 = models.BigIntegerField(blank=True, null=True)
    vendedor = models.ForeignKey('Vendedor', models.DO_NOTHING, blank=True, null=True)
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
    create_user = models.CharField(max_length=255, blank=True, null=True)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    razon_social = models.CharField(max_length=255, blank=True, null=True)
    regimen_fiscal = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'


class ClienteContactos(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    activo = models.TextField()  # This field type is a guess.
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING)
    email = models.CharField(max_length=255, blank=True, null=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    puesto = models.CharField(max_length=255, blank=True, null=True)
    sw2 = models.BigIntegerField(blank=True, null=True)
    telefono = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente_contactos'


class ClienteCredito(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    atraso_maximo = models.BigIntegerField()
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING)
    cobrador = models.ForeignKey('Cobrador', models.DO_NOTHING, blank=True, null=True)
    credito_activo = models.TextField()  # This field type is a guess.
    descuento_fijo = models.DecimalField(max_digits=19, decimal_places=2)
    dia_cobro = models.BigIntegerField()
    dia_revision = models.BigIntegerField()
    linea_de_credito = models.DecimalField(max_digits=19, decimal_places=2)
    operador = models.BigIntegerField()
    plazo = models.BigIntegerField()
    postfechado = models.TextField()  # This field type is a guess.
    revision = models.TextField()  # This field type is a guess.
    saldo = models.DecimalField(max_digits=19, decimal_places=2)
    socio = models.ForeignKey('Socio', models.DO_NOTHING, blank=True, null=True)
    sw2 = models.BigIntegerField(blank=True, null=True)
    vence_factura = models.TextField()  # This field type is a guess.
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    create_user = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente_credito'


class Cobrador(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    activo = models.TextField()  # This field type is a guess.
    apellido_materno = models.CharField(max_length=255, blank=True, null=True)
    apellido_paterno = models.CharField(max_length=255, blank=True, null=True)
    clave = models.CharField(max_length=255, blank=True, null=True)
    comision = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    curp = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    nombres = models.CharField(max_length=255, blank=True, null=True)
    rfc = models.CharField(max_length=255, blank=True, null=True)
    sw2 = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cobrador'


class Cobro(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    diferencia_fecha = models.DateField(blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    anticipo = models.TextField()  # This field type is a guess.
    forma_de_pago = models.CharField(max_length=255)
    last_updated = models.DateTimeField(blank=True, null=True)
    sucursal = models.ForeignKey('Sucursal', models.DO_NOTHING)
    referencia = models.CharField(max_length=255, blank=True, null=True)
    moneda = models.CharField(max_length=255)
    tipo_de_cambio = models.DecimalField(max_digits=19, decimal_places=2)
    primera_aplicacion = models.DateTimeField(blank=True, null=True)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    diferencia = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    tipo = models.CharField(max_length=3)
    fecha = models.DateField()
    enviado = models.TextField()  # This field type is a guess.
    sw2 = models.CharField(unique=True, max_length=255, blank=True, null=True)
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING)
    importe = models.DecimalField(max_digits=19, decimal_places=2)
    create_user = models.CharField(max_length=255, blank=True, null=True)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    cfdi = models.ForeignKey(Cfdi, models.DO_NOTHING, blank=True, null=True)
    cancelacion_de_cfdi_id = models.BigIntegerField(blank=True, null=True)
    cancelacion_motivo = models.CharField(max_length=255, blank=True, null=True)
    recibo_anterior = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cobro'


class CobroCheque(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    ficha = models.ForeignKey('Ficha', models.DO_NOTHING, blank=True, null=True)
    date_created = models.DateTimeField()
    cobro = models.ForeignKey(Cobro, models.DO_NOTHING)
    cambio_por_efectivo = models.TextField()  # This field type is a guess.
    last_updated = models.DateTimeField()
    emisor = models.CharField(max_length=255, blank=True, null=True)
    numero_de_cuenta = models.CharField(max_length=255)
    numero = models.BigIntegerField(blank=True, null=True)
    banco_origen = models.ForeignKey(Banco, models.DO_NOTHING)
    vencimiento = models.DateField(blank=True, null=True)
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    post_fechado = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'cobro_cheque'


class CobroDeposito(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    cobro = models.ForeignKey(Cobro, models.DO_NOTHING)
    last_updated = models.DateTimeField()
    total_efectivo = models.DecimalField(max_digits=19, decimal_places=2)
    cuenta_destino = models.ForeignKey('CuentaDeBanco', models.DO_NOTHING)
    folio = models.BigIntegerField()
    banco_origen = models.ForeignKey(Banco, models.DO_NOTHING)
    total_cheque = models.DecimalField(max_digits=19, decimal_places=2)
    ingreso = models.ForeignKey('MovimientoDeCuenta', models.DO_NOTHING, blank=True, null=True)
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    fecha_deposito = models.DateField()
    total_tarjeta = models.DecimalField(max_digits=19, decimal_places=2)
    conciliado = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'cobro_deposito'


class CobroTarjeta(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    corte_de_tarjeta = models.ForeignKey('CorteDeTarjeta', models.DO_NOTHING, blank=True, null=True)
    comision = models.DecimalField(max_digits=19, decimal_places=2)
    debito_credito = models.TextField()  # This field type is a guess.
    date_created = models.DateTimeField()
    cobro = models.ForeignKey(Cobro, models.DO_NOTHING)
    visa_master = models.TextField()  # This field type is a guess.
    last_updated = models.DateTimeField()
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    validacion = models.IntegerField()
    corte = models.CharField(max_length=255, blank=True, null=True)
    partidas_idx = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cobro_tarjeta'


class CobroTransferencia(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    cobro = models.ForeignKey(Cobro, models.DO_NOTHING)
    last_updated = models.DateTimeField()
    cuenta_destino = models.ForeignKey('CuentaDeBanco', models.DO_NOTHING)
    folio = models.BigIntegerField()
    banco_origen = models.ForeignKey(Banco, models.DO_NOTHING)
    ingreso = models.ForeignKey('MovimientoDeCuenta', models.DO_NOTHING, blank=True, null=True)
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    fecha_deposito = models.DateField()
    conciliado = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'cobro_transferencia'


class CodigosPostalesMx(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    estado = models.CharField(max_length=255, blank=True, null=True)
    asentamiento = models.CharField(max_length=255, blank=True, null=True)
    codigo = models.CharField(max_length=255, blank=True, null=True)
    colonia = models.CharField(max_length=255, blank=True, null=True)
    municipio = models.CharField(max_length=255, blank=True, null=True)
    ciudad = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'codigos_postales_mx'


class ComisionBancaria(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    comision = models.DecimalField(max_digits=19, decimal_places=2)
    cxp = models.ForeignKey('CuentaPorPagar', models.DO_NOTHING, blank=True, null=True)
    fecha = models.DateField()
    comentario = models.CharField(max_length=200, blank=True, null=True)
    impuesto = models.DecimalField(max_digits=19, decimal_places=2)
    impuesto_tasa = models.DecimalField(max_digits=19, decimal_places=2)
    cuenta = models.ForeignKey('CuentaDeBanco', models.DO_NOTHING)
    referencia_bancaria = models.CharField(max_length=100, blank=True, null=True)
    date_created = models.DateTimeField()
    last_updated = models.DateTimeField()
    cxp_0 = models.CharField(db_column='cxp', max_length=255, blank=True, null=True)  # Field renamed because of name conflict.

    class Meta:
        managed = False
        db_table = 'comision_bancaria'


class ComisionBancariaMovimientoDeCuenta(models.Model):
    comision_bancaria_movimientos = models.ForeignKey(ComisionBancaria, models.DO_NOTHING)
    movimiento_de_cuenta = models.ForeignKey('MovimientoDeCuenta', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comision_bancaria_movimiento_de_cuenta'


class ComplementoIne(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    contabilidad = models.BigIntegerField(blank=True, null=True)
    venta = models.ForeignKey('Venta', models.DO_NOTHING)
    tipo_de_comite = models.CharField(max_length=18, blank=True, null=True)
    tipo_de_proceso = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'complemento_ine'


class ComplementoIneEntidad(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    ambito = models.CharField(max_length=7, blank=True, null=True)
    clave = models.CharField(max_length=10)
    complemento = models.ForeignKey(ComplementoIne, models.DO_NOTHING)
    partidas_idx = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'complemento_ine_entidad'


class ComplementoIneEntidadContabilidad(models.Model):
    complemento_ine_entidad_id = models.CharField(max_length=255)
    contabilidad_integer = models.IntegerField(blank=True, null=True)
    contabilidad_idx = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'complemento_ine_entidad_contabilidad'


class Compra(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    importe_neto = models.DecimalField(max_digits=19, decimal_places=2)
    last_updated_by = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField()
    total = models.DecimalField(max_digits=19, decimal_places=2)
    entrega = models.DateField(blank=True, null=True)
    last_updated = models.DateTimeField()
    sucursal = models.ForeignKey('Sucursal', models.DO_NOTHING)
    importe_descuento = models.DecimalField(max_digits=19, decimal_places=2)
    moneda = models.CharField(max_length=255)
    proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING)
    tipo_de_cambio = models.DecimalField(max_digits=19, decimal_places=2)
    nacional = models.TextField()  # This field type is a guess.
    folio = models.BigIntegerField()
    fecha = models.DateField()
    ultima_depuracion = models.DateTimeField(blank=True, null=True)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    especial = models.IntegerField(blank=True, null=True)
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    impuestos = models.DecimalField(max_digits=19, decimal_places=2)
    created_by = models.CharField(max_length=255, blank=True, null=True)
    importe_bruto = models.DecimalField(max_digits=19, decimal_places=2)
    centralizada = models.TextField()  # This field type is a guess.
    pendiente = models.IntegerField(blank=True, null=True)
    consolidada = models.IntegerField(blank=True, null=True)
    cerrada = models.DateField(blank=True, null=True)
    rfc = models.CharField(max_length=14, blank=True, null=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    serie = models.CharField(max_length=255, blank=True, null=True)
    clave = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'compra'
        unique_together = (('sucursal', 'folio'),)


class CompraDet(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    importe_neto = models.DecimalField(max_digits=19, decimal_places=2)
    depurado = models.DecimalField(max_digits=19, decimal_places=2)
    solicitado = models.DecimalField(max_digits=19, decimal_places=2)
    date_created = models.DateTimeField()
    precio = models.DecimalField(max_digits=19, decimal_places=2)
    descuento1 = models.DecimalField(max_digits=19, decimal_places=2)
    last_updated = models.DateTimeField()
    sucursal = models.ForeignKey('Sucursal', models.DO_NOTHING)
    importe_descuento = models.DecimalField(max_digits=19, decimal_places=2)
    compra = models.ForeignKey(Compra, models.DO_NOTHING)
    descuento4 = models.DecimalField(max_digits=19, decimal_places=2)
    descuento_financiero = models.DecimalField(max_digits=19, decimal_places=2)
    costo = models.DecimalField(max_digits=19, decimal_places=2)
    descuento2 = models.DecimalField(max_digits=19, decimal_places=2)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    depuracion = models.DateTimeField(blank=True, null=True)
    producto = models.ForeignKey('Producto', models.DO_NOTHING)
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    descuento3 = models.DecimalField(max_digits=19, decimal_places=2)
    importe_bruto = models.DecimalField(max_digits=19, decimal_places=2)
    partidas_idx = models.IntegerField(blank=True, null=True)
    clave = models.CharField(max_length=20, blank=True, null=True)
    unidad = models.CharField(max_length=10, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'compra_det'


class ComprobanteFiscal(models.Model):
    id = models.BigIntegerField(primary_key=True)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    total = models.DecimalField(max_digits=19, decimal_places=2)
    forma_de_pago = models.CharField(max_length=50)
    uuid = models.CharField(unique=True, max_length=255)
    last_updated = models.DateTimeField()
    emisor = models.CharField(max_length=255)
    tipo_de_comprobante = models.CharField(max_length=8)
    serie = models.CharField(max_length=30, blank=True, null=True)
    rfc = models.CharField(max_length=255, blank=True, null=True)
    file_name = models.CharField(max_length=150)
    original_name = models.CharField(max_length=150)
    folio = models.CharField(max_length=30, blank=True, null=True)
    fecha = models.DateTimeField()
    url = models.CharField(max_length=255)
    receptor_rfc = models.CharField(max_length=13)
    metodo_de_pago = models.CharField(max_length=30)
    emisor_rfc = models.CharField(max_length=13)

    class Meta:
        managed = False
        db_table = 'comprobante_fiscal'


class ComunicacionEmpresa(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    activo = models.TextField()  # This field type is a guess.
    tipo = models.CharField(max_length=4)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    sw2 = models.BigIntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING)
    cfdi = models.TextField()  # This field type is a guess.
    validado = models.TextField(blank=True, null=True)  # This field type is a guess.
    sucursal_updated = models.CharField(max_length=255, blank=True, null=True)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    sucursal_created = models.CharField(max_length=255, blank=True, null=True)
    create_user = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comunicacion_empresa'


class ConceptoDeGasto(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    cantidad = models.DecimalField(max_digits=19, decimal_places=2)
    producto_servicio = models.ForeignKey('ProductoServicio', models.DO_NOTHING, blank=True, null=True)
    last_updated = models.DateTimeField()
    sucursal = models.ForeignKey('Sucursal', models.DO_NOTHING, blank=True, null=True)
    gasto = models.ForeignKey('Gasto', models.DO_NOTHING)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    sw2 = models.BigIntegerField(blank=True, null=True)
    concepto = models.CharField(max_length=255, blank=True, null=True)
    cuenta_contable = models.CharField(max_length=255, blank=True, null=True)
    importe = models.DecimalField(max_digits=19, decimal_places=2)
    partidas_idx = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'concepto_de_gasto'


class CondicionDeEnvio(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    fecha_de_entrega = models.DateTimeField()
    asegurado = models.TextField()  # This field type is a guess.
    grupo = models.CharField(max_length=10, blank=True, null=True)
    zona = models.CharField(max_length=20, blank=True, null=True)
    longitud = models.DecimalField(max_digits=19, decimal_places=2)
    venta = models.ForeignKey('Venta', models.DO_NOTHING)
    recoleccion = models.TextField()  # This field type is a guess.
    latitud = models.DecimalField(max_digits=19, decimal_places=2)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    condiciones = models.CharField(max_length=255, blank=True, null=True)
    asignado = models.DateTimeField(blank=True, null=True)
    ocurre = models.TextField()  # This field type is a guess.
    parcial = models.TextField()  # This field type is a guess.
    municipio = models.CharField(max_length=100, blank=True, null=True)
    direccion_numero_exterior = models.CharField(max_length=50, blank=True, null=True)
    direccion_numero_interior = models.CharField(max_length=50, blank=True, null=True)
    direccion_latitud = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    direccion_longitud = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    direccion_estado = models.CharField(max_length=255, blank=True, null=True)
    direccion_pais = models.CharField(max_length=100, blank=True, null=True)
    direccion_calle = models.CharField(max_length=200, blank=True, null=True)
    direccion_colonia = models.CharField(max_length=255, blank=True, null=True)
    direccion_codigo_postal = models.CharField(max_length=255, blank=True, null=True)
    direccion_municipio = models.CharField(max_length=255, blank=True, null=True)
    transporte = models.CharField(max_length=255, blank=True, null=True)
    cerrado = models.DateTimeField(blank=True, null=True)
    comentario_cierre = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'condicion_de_envio'


class Conteo(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    contador1 = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField()
    capturista = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField()
    sucursal = models.ForeignKey('Sucursal', models.DO_NOTHING)
    sector = models.ForeignKey('Sector', models.DO_NOTHING)
    contador2 = models.CharField(max_length=255, blank=True, null=True)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    auditor2 = models.CharField(max_length=255, blank=True, null=True)
    fecha = models.DateField()
    comentario = models.CharField(max_length=255, blank=True, null=True)
    documento = models.BigIntegerField()
    auditor1 = models.CharField(max_length=255, blank=True, null=True)
    create_user = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conteo'


class ConteoDet(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    cantidad = models.DecimalField(max_digits=19, decimal_places=2) 
    producto = models.ForeignKey('Producto', models.DO_NOTHING)
    documento = models.BigIntegerField()
    indice = models.BigIntegerField()
    conteo = models.ForeignKey(Conteo, models.DO_NOTHING)
    partidas_idx = models.IntegerField(blank=True, null=True)




    class Meta:
        managed = False
        db_table = 'conteo_det'


class ContraRecibo(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    folio = models.BigIntegerField()
    date_created = models.DateTimeField()
    fecha = models.DateField()
    total = models.DecimalField(max_digits=19, decimal_places=2)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField()
    sw2 = models.BigIntegerField(blank=True, null=True)
    moneda = models.CharField(max_length=255)
    proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'contra_recibo'


class ContraReciboCuentaPorPagar(models.Model):
    contra_recibo_cuentas_por_pagar_id = models.CharField(max_length=255)
    cuenta_por_pagar = models.ForeignKey('CuentaPorPagar', models.DO_NOTHING, blank=True, null=True)
    cuentas_por_pagar_idx = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contra_recibo_cuenta_por_pagar'


class Corte(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    asignacion = models.DateTimeField(blank=True, null=True)
    instruccion_corte = models.ForeignKey('InstruccionCorte', models.DO_NOTHING, blank=True, null=True)
    surtido = models.ForeignKey('Surtido', models.DO_NOTHING)
    empacado_fin = models.DateTimeField(blank=True, null=True)
    inicio = models.DateTimeField(blank=True, null=True)
    cancelado_usuario = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    empacado_inicio = models.DateTimeField(blank=True, null=True)
    fin = models.DateTimeField(blank=True, null=True)
    empacador = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    producto = models.ForeignKey('Producto', models.DO_NOTHING)
    cancelado = models.DateTimeField(blank=True, null=True)
    asignado = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    cortes_idx = models.IntegerField(blank=True, null=True)
    date_created = models.DateTimeField()
    cantidad = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    clave = models.CharField(max_length=255)
    instruccion = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField()
    estado = models.CharField(max_length=255)
    venta = models.BigIntegerField(blank=True, null=True)
    parcializado = models.TextField()  # This field type is a guess.
    origen = models.CharField(max_length=255, blank=True, null=True)
    cortador = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    factura = models.BigIntegerField(blank=True, null=True)
    cancelo = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    descripcion = models.CharField(max_length=255)
    asignado_0 = models.DateTimeField(db_column='asignado', blank=True, null=True)  # Field renamed because of name conflict.
    parcial = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'corte'


class CorteCobranza(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    deposito = models.DecimalField(max_digits=19, decimal_places=2)
    date_created = models.DateTimeField()
    forma_de_pago = models.CharField(max_length=255)
    cierre = models.TextField()  # This field type is a guess.
    last_updated = models.DateTimeField()
    cortes_acumulado = models.DecimalField(max_digits=19, decimal_places=2)
    sucursal = models.ForeignKey('Sucursal', models.DO_NOTHING)
    pagos_registrados = models.DecimalField(max_digits=19, decimal_places=2)
    tipo_de_venta = models.CharField(max_length=3)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    corte = models.DateTimeField()
    fecha = models.DateField()
    comentario = models.CharField(max_length=255, blank=True, null=True)
    fecha_deposito = models.DateField(blank=True, null=True)
    anticipo_corte = models.TextField()  # This field type is a guess.
    cambio_cheque = models.TextField()  # This field type is a guess.
    cambios_de_cheques = models.DecimalField(max_digits=19, decimal_places=2)
    create_user = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'corte_cobranza'


class CorteDeTarjeta(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    total = models.DecimalField(max_digits=19, decimal_places=2)
    cuenta_de_banco = models.ForeignKey('CuentaDeBanco', models.DO_NOTHING)
    last_updated = models.DateTimeField()
    sucursal = models.ForeignKey('Sucursal', models.DO_NOTHING)
    corte = models.DateField(blank=True, null=True)
    folio = models.BigIntegerField()
    visa_master = models.TextField()  # This field type is a guess.
    comentario = models.CharField(max_length=255, blank=True, null=True)
    sw2 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'corte_de_tarjeta'


class CorteDeTarjetaAplicacion(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    corte = models.ForeignKey(CorteDeTarjeta, models.DO_NOTHING)
    orden = models.IntegerField()
    debito_credito = models.TextField()  # This field type is a guess.
    tipo = models.CharField(max_length=255)
    visa_master = models.TextField()  # This field type is a guess.
    comentario = models.CharField(max_length=255, blank=True, null=True)
    ingreso = models.ForeignKey('MovimientoDeCuenta', models.DO_NOTHING)
    sw2 = models.CharField(max_length=255)
    importe = models.DecimalField(max_digits=19, decimal_places=2)
    aplicaciones_idx = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'corte_de_tarjeta_aplicacion'


class CorteDeTarjetaDet(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    corte = models.ForeignKey(CorteDeTarjeta, models.DO_NOTHING)
    date_created = models.DateTimeField()
    cobro = models.ForeignKey(Cobro, models.DO_NOTHING)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField()
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    partidas_idx = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'corte_de_tarjeta_det'


class CuentaBancaria(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    activo = models.TextField()  # This field type is a guess.
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING)
    cuenta_habiente = models.CharField(max_length=255)
    numero_de_cuenta = models.CharField(max_length=255)
    pago_referenciado = models.CharField(max_length=255, blank=True, null=True)
    sw2 = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'cuenta_bancaria'


class CuentaContable(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    clave = models.CharField(unique=True, max_length=100, blank=True, null=True)
    cuenta_sat = models.ForeignKey('SatCuenta', models.DO_NOTHING, blank=True, null=True)
    date_created = models.DateTimeField()
    de_resultado = models.TextField()  # This field type is a guess.
    descripcion = models.CharField(max_length=300)
    detalle = models.TextField()  # This field type is a guess.
    last_updated = models.DateTimeField()
    naturaleza = models.CharField(max_length=9)
    padre = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    presentacion_contable = models.TextField()  # This field type is a guess.
    presentacion_financiera = models.TextField()  # This field type is a guess.
    presentacion_fiscal = models.TextField()  # This field type is a guess.
    presentacion_presupuestal = models.TextField()  # This field type is a guess.
    suspendida = models.TextField()  # This field type is a guess.
    tipo = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'cuenta_contable'


class CuentaDeBanco(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    activo = models.TextField()  # This field type is a guess.
    banco_sat = models.ForeignKey(BancoSat, models.DO_NOTHING, blank=True, null=True)
    clave = models.CharField(unique=True, max_length=30)
    date_created = models.DateTimeField()
    descripcion = models.CharField(max_length=255)
    impresion_template = models.CharField(max_length=50, blank=True, null=True)
    last_updated = models.DateTimeField()
    moneda = models.CharField(max_length=255)
    numero = models.CharField(max_length=30)
    sub_cuenta_operativa = models.CharField(max_length=4, blank=True, null=True)
    sw2 = models.BigIntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=9)
    disponible_en_venta = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'cuenta_de_banco'


class CuentaPorCobrar(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    total = models.DecimalField(max_digits=19, decimal_places=2)
    tipo_documento = models.CharField(max_length=18)
    forma_de_pago = models.CharField(max_length=255)
    uuid = models.CharField(unique=True, max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField()
    sucursal = models.ForeignKey('Sucursal', models.DO_NOTHING)
    moneda = models.CharField(max_length=255)
    tipo_de_cambio = models.DecimalField(max_digits=19, decimal_places=6)
    cargo = models.DecimalField(max_digits=19, decimal_places=2)
    update_user = models.CharField(max_length=255)
    tipo = models.CharField(max_length=3, blank=True, null=True)
    fecha = models.DateField()
    comentario = models.CharField(max_length=255, blank=True, null=True)
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    impuesto = models.DecimalField(max_digits=19, decimal_places=2)
    documento = models.BigIntegerField()
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING)
    importe = models.DecimalField(max_digits=19, decimal_places=2)
    create_user = models.CharField(max_length=255)
    cfdi = models.ForeignKey(Cfdi, models.DO_NOTHING, blank=True, null=True)
    cheque_post_fechado = models.TextField(blank=True, null=True)  # This field type is a guess.
    cancelacion_motivo = models.CharField(max_length=255, blank=True, null=True)
    descuento_importe = models.DecimalField(max_digits=19, decimal_places=2)
    cancelada = models.DateField(blank=True, null=True)
    subtotal = models.DecimalField(max_digits=19, decimal_places=2)
    cancelacion_usuario = models.CharField(max_length=255, blank=True, null=True)
    credito = models.ForeignKey('VentaCredito', models.DO_NOTHING, blank=True, null=True)
    vencimiento = models.DateField(blank=True, null=True)
    juridico = models.DateField(blank=True, null=True)
    saldo_actualizado = models.FloatField(blank=True, null=True)
    anticipo = models.CharField(max_length=50, blank=True, null=True)
    anticipo_tipo = models.CharField(max_length=7, blank=True, null=True)
    relacionados = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuenta_por_cobrar'


class CuentaPorPagar(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    retencion_iva = models.DecimalField(max_digits=19, decimal_places=2)
    comprobante = models.OneToOneField(ComprobanteFiscal, models.DO_NOTHING, blank=True, null=True)
    date_created = models.DateTimeField()
    total = models.DecimalField(max_digits=19, decimal_places=4)
    retencion_isr_tasa = models.DecimalField(max_digits=19, decimal_places=2)
    last_updated = models.DateTimeField()
    moneda = models.CharField(max_length=255)
    requisitado = models.DecimalField(max_digits=19, decimal_places=2)
    proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING)
    tipo_de_cambio = models.DecimalField(max_digits=19, decimal_places=6)
    retencion_iva_tasa = models.DecimalField(max_digits=19, decimal_places=2)
    descuentof = models.DecimalField(max_digits=19, decimal_places=2)
    tipo = models.CharField(max_length=7)
    fecha = models.DateField()
    comentario = models.CharField(max_length=255, blank=True, null=True)
    descuentof_vto = models.DateField(blank=True, null=True)
    vencimiento = models.DateField()
    sw2 = models.BigIntegerField(blank=True, null=True)
    impuesto = models.DecimalField(max_digits=19, decimal_places=4)
    retencion_isr = models.DecimalField(max_digits=19, decimal_places=4)
    documento = models.CharField(max_length=255)
    impuesto_tasa = models.DecimalField(max_digits=19, decimal_places=2)
    importe = models.DecimalField(max_digits=19, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'cuenta_por_pagar'


class CuentaSat(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    codigo = models.CharField(unique=True, max_length=20)
    nivel = models.IntegerField()
    nombre = models.CharField(max_length=255)
    tipo = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cuenta_sat'


class DataSourceReplica(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    central = models.TextField()  # This field type is a guess.
    username = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    server = models.CharField(max_length=255, blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    data_base = models.CharField(max_length=255)
    activa = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'data_source_replica'


class DescuentoPorVolumen(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    descuento = models.DecimalField(max_digits=19, decimal_places=2)
    date_created = models.DateTimeField()
    activo = models.TextField()  # This field type is a guess.
    importe = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'descuento_por_volumen'


class DevolucionCliente(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    total = models.DecimalField(max_digits=19, decimal_places=2)
    forma_de_pago = models.CharField(max_length=255)
    last_updated = models.DateTimeField()
    tipo_de_documento = models.CharField(max_length=255, blank=True, null=True)
    sucursal = models.ForeignKey('Sucursal', models.DO_NOTHING)
    moneda = models.CharField(max_length=255)
    tipo_de_cambio = models.DecimalField(max_digits=19, decimal_places=6)
    update_user = models.CharField(max_length=255)
    fecha = models.DateTimeField()
    cuenta_por_cobrar = models.ForeignKey(CuentaPorCobrar, models.DO_NOTHING, blank=True, null=True)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    impuesto = models.DecimalField(max_digits=19, decimal_places=2)
    documento = models.BigIntegerField()
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING)
    importe = models.DecimalField(max_digits=19, decimal_places=2)
    create_user = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'devolucion_cliente'


class DevolucionDeCompra(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    fecha_referencia = models.DateTimeField(blank=True, null=True)
    sucursal = models.ForeignKey('Sucursal', models.DO_NOTHING)
    referencia = models.CharField(max_length=255, blank=True, null=True)
    proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    nota_cxp = models.ForeignKey(AbonoCxp, models.DO_NOTHING, blank=True, null=True)
    fecha = models.DateField()
    fecha_inventario = models.DateTimeField(blank=True, null=True)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    recepcion_de_compra = models.ForeignKey('RecepcionDeCompra', models.DO_NOTHING, blank=True, null=True)
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    documento = models.BigIntegerField()
    create_user = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'devolucion_de_compra'


class DevolucionDeCompraDet(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    cantidad = models.DecimalField(max_digits=19, decimal_places=2)
    inventario = models.ForeignKey('Inventario', models.DO_NOTHING, blank=True, null=True)
    devolucion_de_compra = models.ForeignKey(DevolucionDeCompra, models.DO_NOTHING)
    importe_costo = models.DecimalField(max_digits=19, decimal_places=2)
    last_updated = models.DateTimeField()
    analisis_devolucion = models.ForeignKey(AnalisisDevolucionCompra, models.DO_NOTHING, blank=True, null=True)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    producto = models.ForeignKey('Producto', models.DO_NOTHING)
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    costo_dec = models.DecimalField(max_digits=19, decimal_places=2)
    recepcion_de_compra_det = models.ForeignKey('RecepcionDeCompraDet', models.DO_NOTHING, blank=True, null=True)
    partidas_idx = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'devolucion_de_compra_det'


class DevolucionDeVenta(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    date_created = models.DateTimeField(blank=True, null=True)
    total = models.DecimalField(max_digits=19, decimal_places=2)
    last_updated = models.DateTimeField(blank=True, null=True)
    venta = models.ForeignKey('Venta', models.DO_NOTHING)
    sucursal = models.ForeignKey('Sucursal', models.DO_NOTHING)
    importe_cortes = models.DecimalField(max_digits=19, decimal_places=2)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    fecha = models.DateTimeField()
    fecha_inventario = models.DateTimeField(blank=True, null=True)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    impuesto = models.DecimalField(max_digits=19, decimal_places=2)
    documento = models.BigIntegerField()
    asignado = models.DateTimeField(blank=True, null=True)
    nota_de_credito = models.ForeignKey('NotaDeCredito', models.DO_NOTHING, blank=True, null=True)
    importe = models.DecimalField(max_digits=19, decimal_places=2)
    create_user = models.CharField(max_length=255, blank=True, null=True)
    cobro = models.ForeignKey(Cobro, models.DO_NOTHING, blank=True, null=True)
    parcial = models.TextField(blank=True, null=True)  # This field type is a guess.
    cancelado = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'devolucion_de_venta'


class DevolucionDeVentaDet(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    costo_dev = models.DecimalField(max_digits=19, decimal_places=2)
    date_created = models.DateTimeField(blank=True, null=True)
    cantidad = models.DecimalField(max_digits=19, decimal_places=2)
    inventario = models.ForeignKey('Inventario', models.DO_NOTHING, blank=True, null=True)
    devolucion_de_venta = models.ForeignKey(DevolucionDeVenta, models.DO_NOTHING)
    importe_costo = models.DecimalField(max_digits=19, decimal_places=2)
    last_updated = models.DateTimeField(blank=True, null=True)
    venta_det = models.ForeignKey('VentaDet', models.DO_NOTHING)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    producto = models.ForeignKey('Producto', models.DO_NOTHING)
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    partidas_idx = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'devolucion_de_venta_det'


class DiferenciaCambiaria(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    cobro = models.ForeignKey(Cobro, models.DO_NOTHING, blank=True, null=True)
    cuenta_por_cobrar = models.ForeignKey(CuentaPorCobrar, models.DO_NOTHING, blank=True, null=True)
    mes = models.BigIntegerField()
    last_updated = models.DateTimeField()
    variacion = models.DecimalField(max_digits=19, decimal_places=2)
    moneda = models.CharField(max_length=255)
    anio = models.BigIntegerField()
    tipo_de_cambio = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'diferencia_cambiaria'


class DireccionEntrega(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING)
    direccion_numero_exterior = models.CharField(max_length=50, blank=True, null=True)
    direccion_numero_interior = models.CharField(max_length=50, blank=True, null=True)
    direccion_latitud = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    direccion_longitud = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    direccion_estado = models.CharField(max_length=255, blank=True, null=True)
    direccion_pais = models.CharField(max_length=100, blank=True, null=True)
    direccion_calle = models.CharField(max_length=200, blank=True, null=True)
    direccion_colonia = models.CharField(max_length=255, blank=True, null=True)
    direccion_codigo_postal = models.CharField(max_length=255, blank=True, null=True)
    direccion_municipio = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'direccion_entrega'


class Embarque(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    chofer = models.ForeignKey(Chofer, models.DO_NOTHING, blank=True, null=True)
    date_created = models.DateTimeField()
    last_updated = models.DateTimeField()
    kilos = models.DecimalField(max_digits=19, decimal_places=2)
    sucursal = models.ForeignKey('Sucursal', models.DO_NOTHING)
    salida = models.DateTimeField(blank=True, null=True)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    valor = models.DecimalField(max_digits=19, decimal_places=2)
    regreso = models.DateTimeField(blank=True, null=True)
    fecha = models.DateField()
    comentario = models.CharField(max_length=255, blank=True, null=True)
    documento = models.IntegerField(blank=True, null=True)
    cerrado = models.DateTimeField(blank=True, null=True)
    create_user = models.CharField(max_length=255, blank=True, null=True)
    empleado = models.CharField(max_length=255, blank=True, null=True)
    foraneo = models.TextField(blank=True, null=True)  # This field type is a guess.
    importado = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'embarque'


class Empresa(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    certificado_digital = models.TextField(blank=True, null=True)
    certificado_digital_pfx = models.TextField(blank=True, null=True)
    clave = models.CharField(unique=True, max_length=15)
    date_created = models.DateTimeField()
    last_updated = models.DateTimeField()
    llave_privada = models.TextField(blank=True, null=True)
    nombre = models.CharField(unique=True, max_length=255)
    numero_de_certificado = models.CharField(max_length=20, blank=True, null=True)
    password_pac = models.CharField(max_length=255, blank=True, null=True)
    password_pfx = models.CharField(max_length=255, blank=True, null=True)
    regimen = models.CharField(max_length=300)
    rfc = models.CharField(max_length=13)
    timbrado_de_prueba = models.TextField()  # This field type is a guess.
    usuario_pac = models.CharField(max_length=255, blank=True, null=True)
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
    regimen_clave_sat = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empresa'


class EntityConfiguration(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    after_export = models.CharField(max_length=5000, blank=True, null=True)
    after_import = models.CharField(max_length=5000, blank=True, null=True)
    date_created = models.DateTimeField()
    exclude_insert_columns = models.CharField(max_length=250, blank=True, null=True)
    exclude_update_columns = models.CharField(max_length=250, blank=True, null=True)
    insert_sql = models.CharField(max_length=5000, blank=True, null=True)
    last_updated = models.DateTimeField()
    name = models.CharField(unique=True, max_length=50)
    pk = models.CharField(max_length=50)
    table_name = models.CharField(max_length=50)
    update_sql = models.CharField(max_length=5000)

    class Meta:
        managed = False
        db_table = 'entity_configuration'


class EntityReplicable(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    data_base = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    table_name = models.CharField(max_length=255, blank=True, null=True)
    operativa = models.TextField()  # This field type is a guess.
    replicable = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'entity_replicable'


class EntregaParcial(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    autorizo = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    last_updated = models.DateTimeField()
    estado = models.CharField(max_length=255)
    venta = models.CharField(max_length=255)
    folio_fac = models.BigIntegerField(blank=True, null=True)
    tipo_de_venta = models.CharField(max_length=255)
    inicio = models.DateTimeField()
    entrega_local = models.TextField()  # This field type is a guess.
    tipo = models.CharField(max_length=255)
    fecha = models.DateTimeField()
    comentario = models.CharField(max_length=255, blank=True, null=True)
    facturo = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    documento = models.BigIntegerField()
    nombre = models.CharField(max_length=255)
    cliente = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'entrega_parcial'


class EntregaParcialDet(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    instruccion_de_entrega_parcial = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField()
    cantidad = models.DecimalField(max_digits=19, decimal_places=2)
    clave = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField()
    venta_det = models.CharField(max_length=255, blank=True, null=True)
    entrega_parcial = models.ForeignKey(EntregaParcial, models.DO_NOTHING)
    valor = models.DecimalField(max_digits=19, decimal_places=2)
    producto = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    partidas_idx = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entrega_parcial_det'


class Envio(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    paquetes = models.IntegerField()
    entidad = models.CharField(max_length=255)
    motivo = models.CharField(max_length=255, blank=True, null=True)
    arribo_latitud = models.DecimalField(max_digits=19, decimal_places=2)
    date_created = models.DateTimeField()
    entregado = models.TextField()  # This field type is a guess.
    tipo_documento = models.CharField(max_length=255)
    fecha_documento = models.DateTimeField()
    recepcion = models.DateTimeField(blank=True, null=True)
    completo = models.TextField()  # This field type is a guess.
    last_updated = models.DateTimeField()
    kilos = models.DecimalField(max_digits=19, decimal_places=2)
    arribo_longitud = models.DecimalField(max_digits=19, decimal_places=2)
    forma_pago = models.CharField(max_length=255, blank=True, null=True)
    reporto_puesto = models.CharField(max_length=255, blank=True, null=True)
    impreso = models.TextField()  # This field type is a guess.
    recibio = models.CharField(max_length=255, blank=True, null=True)
    origen = models.CharField(max_length=255)
    cortado = models.TextField()  # This field type is a guess.
    embarque = models.ForeignKey(Embarque, models.DO_NOTHING)
    matratado = models.TextField()  # This field type is a guess.
    total_documento = models.DecimalField(max_digits=19, decimal_places=2)
    recepcion_longitud = models.DecimalField(max_digits=19, decimal_places=2)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    reporto_nombre = models.CharField(max_length=255, blank=True, null=True)
    documento = models.CharField(max_length=255)
    por_cobrar = models.DecimalField(max_digits=19, decimal_places=2)
    recepcion_latitud = models.DecimalField(max_digits=19, decimal_places=2)
    nombre = models.CharField(max_length=255)
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING, blank=True, null=True)
    parcial = models.TextField()  # This field type is a guess.
    arribo = models.DateTimeField(blank=True, null=True)
    area = models.CharField(max_length=255, blank=True, null=True)
    partidas_idx = models.IntegerField(blank=True, null=True)
    valor = models.DecimalField(max_digits=19, decimal_places=2)
    salida = models.DateTimeField(blank=True, null=True)
    callcenter = models.CharField(max_length=255, blank=True, null=True)
    precio_tonelada = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    maniobra = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    comision_por_tonelada = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'envio'


class EnvioComision(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    comision = models.DecimalField(max_digits=19, decimal_places=2)
    date_created = models.DateTimeField()
    last_updated = models.DateTimeField()
    comentario_de_comision = models.CharField(max_length=255, blank=True, null=True)
    venta = models.ForeignKey('Venta', models.DO_NOTHING)
    envio = models.ForeignKey(Envio, models.DO_NOTHING)
    update_user = models.CharField(max_length=255)
    importe_comision = models.DecimalField(max_digits=19, decimal_places=2)
    valor = models.DecimalField(max_digits=19, decimal_places=2)
    fecha_comision = models.DateTimeField(blank=True, null=True)
    comision_por_tonelada = models.DecimalField(max_digits=19, decimal_places=2)
    create_user = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'envio_comision'


class EnvioDet(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    valor = models.DecimalField(max_digits=19, decimal_places=2)
    date_created = models.DateTimeField()
    cantidad = models.DecimalField(max_digits=19, decimal_places=2)
    instruccion_entrega_parcial = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField()
    venta_det = models.ForeignKey('VentaDet', models.DO_NOTHING)
    parcial_det = models.ForeignKey('VentaParcialDet', models.DO_NOTHING, blank=True, null=True)
    producto = models.ForeignKey('Producto', models.DO_NOTHING)
    envio = models.ForeignKey(Envio, models.DO_NOTHING)
    partidas_idx = models.IntegerField(blank=True, null=True)
    kilos = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'envio_det'


class Existencia(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    entrada_compra = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    cantidad = models.DecimalField(max_digits=19, decimal_places=2)
    movimiento_almacen = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    kilos = models.DecimalField(max_digits=19, decimal_places=2)
    devolucion_venta = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    venta = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    sucursal = models.ForeignKey('Sucursal', models.DO_NOTHING)
    transformacion = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    nacional = models.TextField()  # This field type is a guess.
    pedidos_pendiente = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    mes = models.BigIntegerField()
    devolucion_compra = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    producto = models.ForeignKey('Producto', models.DO_NOTHING)
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    traslado = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    anio = models.BigIntegerField()
    existencia_inicial = models.DecimalField(max_digits=19, decimal_places=3, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    clave = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    sucursal_nombre = models.CharField(max_length=255, blank=True, null=True)
    recorte = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    recorte_comentario = models.CharField(max_length=255, blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    recorte_fecha = models.DateField(blank=True, null=True)
    costo_promedio = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    costo = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'existencia'


class ExistenciaConteo(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    cantidad = models.DecimalField(max_digits=19, decimal_places=2)
    existencia = models.ForeignKey(Existencia, models.DO_NOTHING)
    fijado = models.DateTimeField(blank=True, null=True)
    ajuste = models.DecimalField(max_digits=19, decimal_places=2)
    sucursal = models.ForeignKey('Sucursal', models.DO_NOTHING)
    conteo_parcial = models.TextField()  # This field type is a guess.
    diferencia = models.DecimalField(max_digits=19, decimal_places=2)
    sectores = models.CharField(max_length=255, blank=True, null=True)
    existencia_original = models.DecimalField(max_digits=19, decimal_places=2)
    fecha = models.DateField()
    producto = models.ForeignKey('Producto', models.DO_NOTHING)
    existencia_final = models.DecimalField(max_digits=19, decimal_places=2)
    conteo = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'existencia_conteo'


class ExistenciaConteo20191207(models.Model):
    id = models.CharField(max_length=255)
    version = models.BigIntegerField()
    cantidad = models.DecimalField(max_digits=19, decimal_places=2)
    existencia_id = models.CharField(max_length=255)
    fijado = models.DateTimeField(blank=True, null=True)
    ajuste = models.DecimalField(max_digits=19, decimal_places=2)
    sucursal_id = models.CharField(max_length=255)
    conteo_parcial = models.TextField()  # This field type is a guess.
    diferencia = models.DecimalField(max_digits=19, decimal_places=2)
    sectores = models.CharField(max_length=255, blank=True, null=True)
    existencia_original = models.DecimalField(max_digits=19, decimal_places=2)
    fecha = models.DateField()
    producto_id = models.CharField(max_length=255)
    existencia_final = models.DecimalField(max_digits=19, decimal_places=2)
    conteo = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'existencia_conteo20191207'


class ExistenciaConteo20200425(models.Model):
    id = models.CharField(max_length=255)
    version = models.BigIntegerField()
    cantidad = models.DecimalField(max_digits=19, decimal_places=2)
    existencia_id = models.CharField(max_length=255)
    fijado = models.DateTimeField(blank=True, null=True)
    ajuste = models.DecimalField(max_digits=19, decimal_places=2)
    sucursal_id = models.CharField(max_length=255)
    conteo_parcial = models.TextField()  # This field type is a guess.
    diferencia = models.DecimalField(max_digits=19, decimal_places=2)
    sectores = models.CharField(max_length=255, blank=True, null=True)
    existencia_original = models.DecimalField(max_digits=19, decimal_places=2)
    fecha = models.DateField()
    producto_id = models.CharField(max_length=255)
    existencia_final = models.DecimalField(max_digits=19, decimal_places=2)
    conteo = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'existencia_conteo20200425'


class ExistenciaConteo20200509(models.Model):
    id = models.CharField(max_length=255)
    version = models.BigIntegerField()
    cantidad = models.DecimalField(max_digits=19, decimal_places=2)
    existencia_id = models.CharField(max_length=255)
    fijado = models.DateTimeField(blank=True, null=True)
    ajuste = models.DecimalField(max_digits=19, decimal_places=2)
    sucursal_id = models.CharField(max_length=255)
    conteo_parcial = models.TextField()  # This field type is a guess.
    diferencia = models.DecimalField(max_digits=19, decimal_places=2)
    sectores = models.CharField(max_length=255, blank=True, null=True)
    existencia_original = models.DecimalField(max_digits=19, decimal_places=2)
    fecha = models.DateField()
    producto_id = models.CharField(max_length=255)
    existencia_final = models.DecimalField(max_digits=19, decimal_places=2)
    conteo = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'existencia_conteo20200509'


class ExistenciaDic2017(models.Model):
    id = models.CharField(max_length=255)
    version = models.BigIntegerField()
    entrada_compra = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    cantidad = models.DecimalField(max_digits=19, decimal_places=2)
    movimiento_almacen = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    kilos = models.DecimalField(max_digits=19, decimal_places=2)
    devolucion_venta = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    venta = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    sucursal_id = models.CharField(max_length=255)
    transformacion = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    nacional = models.TextField()  # This field type is a guess.
    pedidos_pendiente = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    mes = models.BigIntegerField()
    devolucion_compra = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    producto_id = models.CharField(max_length=255)
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    traslado = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    anio = models.BigIntegerField()
    existencia_inicial = models.DecimalField(max_digits=19, decimal_places=3, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    clave = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    sucursal_nombre = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'existencia_dic_2017'


class ExistenciaTemp(models.Model):
    id = models.CharField(max_length=255)
    version = models.BigIntegerField()
    entrada_compra = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    cantidad = models.DecimalField(max_digits=19, decimal_places=2)
    movimiento_almacen = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    kilos = models.DecimalField(max_digits=19, decimal_places=2)
    devolucion_venta = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    venta = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    sucursal_id = models.CharField(max_length=255)
    transformacion = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    nacional = models.TextField()  # This field type is a guess.
    pedidos_pendiente = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    mes = models.BigIntegerField()
    devolucion_compra = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    producto_id = models.CharField(max_length=255)
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    traslado = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    anio = models.BigIntegerField()
    existencia_inicial = models.DecimalField(max_digits=19, decimal_places=3, blank=True, null=True)
    date_created = models.DateTimeField()
    clave = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField()
    sucursal_nombre = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'existencia_temp'


class FacturistaDeEmbarque(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    last_updated = models.DateTimeField()
    telefono = models.CharField(max_length=255, blank=True, null=True)
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    rfc = models.CharField(max_length=13)
    nombre = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    create_user = models.CharField(max_length=255, blank=True, null=True)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    clave = models.IntegerField(blank=True, null=True)
    descuent_en_prestamo = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    proveedor_id = models.CharField(max_length=255, blank=True, null=True)
    orden = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facturista_de_embarque'


class Ficha(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    total = models.DecimalField(max_digits=19, decimal_places=2)
    cuenta_de_banco = models.ForeignKey(CuentaDeBanco, models.DO_NOTHING)
    last_updated = models.DateTimeField()
    tipo_de_ficha = models.CharField(max_length=12)
    sucursal = models.ForeignKey('Sucursal', models.DO_NOTHING)
    fecha_corte = models.DateTimeField(blank=True, null=True)
    origen = models.CharField(max_length=3)
    folio = models.BigIntegerField()
    fecha = models.DateField()
    cancelada = models.DateTimeField(blank=True, null=True)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    ingreso = models.ForeignKey('MovimientoDeCuenta', models.DO_NOTHING, blank=True, null=True)
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    envio_valores = models.TextField()  # This field type is a guess.
    update_user = models.CharField(max_length=255, blank=True, null=True)
    create_user = models.CharField(max_length=255, blank=True, null=True)
    diferencia_tipo = models.CharField(max_length=255, blank=True, null=True)
    diferencia_usuario = models.CharField(max_length=255, blank=True, null=True)
    diferencia = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ficha'


class FichaDet(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    ficha = models.ForeignKey(Ficha, models.DO_NOTHING)
    cheque = models.DecimalField(max_digits=19, decimal_places=2)
    date_created = models.DateTimeField()
    banco = models.CharField(max_length=50)
    cobro = models.ForeignKey(Cobro, models.DO_NOTHING)
    last_updated = models.DateTimeField()
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    efectivo = models.DecimalField(max_digits=19, decimal_places=2)
    partidas_idx = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ficha_det'


class Folio(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    entidad = models.CharField(max_length=30)
    folio = models.BigIntegerField()
    serie = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'folio'
        unique_together = (('serie', 'entidad', 'folio'),)


class FondoFijo(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    last_updated = models.DateTimeField()
    sucursal = models.ForeignKey('Sucursal', models.DO_NOTHING)
    rembolso = models.TextField()  # This field type is a guess.
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

    class Meta:
        managed = False
        db_table = 'fondo_fijo'


class Gasto(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    retencion_iva = models.DecimalField(max_digits=19, decimal_places=2)
    cxp = models.ForeignKey(CuentaPorPagar, models.DO_NOTHING)
    date_created = models.DateTimeField()
    cantidad = models.DecimalField(max_digits=19, decimal_places=2)
    retencion_isr_tasa = models.DecimalField(max_digits=19, decimal_places=2)
    last_updated = models.DateTimeField()
    unidad = models.CharField(max_length=255)
    valor_unitario = models.DecimalField(max_digits=19, decimal_places=2)
    tasa_iva = models.DecimalField(max_digits=19, decimal_places=2)
    retencion_iva_tasa = models.DecimalField(max_digits=19, decimal_places=2)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    sw2 = models.BigIntegerField(blank=True, null=True)
    retencion_isr = models.DecimalField(max_digits=19, decimal_places=2)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    importe = models.DecimalField(max_digits=19, decimal_places=4)
    gastos_idx = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gasto'


class IncidenciaChofer(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    chofer = models.ForeignKey(Chofer, models.DO_NOTHING)
    fecha = models.DateTimeField()
    comentario = models.CharField(max_length=255, blank=True, null=True)
    suspendido = models.TextField()  # This field type is a guess.
    incidencia = models.CharField(max_length=13)

    class Meta:
        managed = False
        db_table = 'incidencia_chofer'


class IneEntidad(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    ambito = models.CharField(max_length=255)
    clave = models.CharField(max_length=255)
    complementoine = models.ForeignKey('VentaIne', models.DO_NOTHING)
    contabilidades = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ine_entidad'


class InstruccionCorte(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    ancho = models.DecimalField(max_digits=19, decimal_places=2)
    tipo = models.CharField(max_length=50, blank=True, null=True)
    cantidad = models.BigIntegerField()
    seleccion_calculo = models.CharField(max_length=255, blank=True, null=True)
    precio = models.DecimalField(max_digits=19, decimal_places=2)
    instruccion = models.CharField(max_length=255, blank=True, null=True)
    venta_det = models.ForeignKey('VentaDet', models.DO_NOTHING)
    largo = models.DecimalField(max_digits=19, decimal_places=2)
    instruccion_empacado = models.CharField(max_length=255, blank=True, null=True)
    refinado = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'instruccion_corte'


class Inventario(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    renglon = models.IntegerField(blank=True, null=True)
    costo_ultima_compra = models.DecimalField(max_digits=19, decimal_places=2)
    date_created = models.DateTimeField(blank=True, null=True)
    cantidad = models.DecimalField(max_digits=19, decimal_places=2)
    last_updated = models.DateTimeField(blank=True, null=True)
    kilos = models.DecimalField(max_digits=19, decimal_places=2)
    sucursal = models.ForeignKey('Sucursal', models.DO_NOTHING)
    costo_promedio = models.DecimalField(max_digits=19, decimal_places=2)
    costo = models.DecimalField(max_digits=19, decimal_places=2)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    nacional = models.TextField()  # This field type is a guess.
    costo_reposicion = models.DecimalField(max_digits=19, decimal_places=2)
    tipo = models.CharField(max_length=255, blank=True, null=True)
    fecha = models.DateTimeField()
    comentario = models.CharField(max_length=255, blank=True, null=True)
    producto = models.ForeignKey('Producto', models.DO_NOTHING)
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    documento = models.BigIntegerField()
    tipo_venta = models.CharField(max_length=255, blank=True, null=True)
    create_user = models.CharField(max_length=255, blank=True, null=True)
    clave = models.CharField(max_length=30, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    sucursal_nombre = models.CharField(max_length=40, blank=True, null=True)
    gasto = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventario'


class Linea(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    activa = models.TextField()  # This field type is a guess.
    date_created = models.DateTimeField()
    last_updated = models.DateTimeField()
    linea = models.CharField(unique=True, max_length=50)
    descripcion = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'linea'


class ListaDePreciosPorProveedor(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    fecha_inicial = models.DateField()
    date_created = models.DateTimeField()
    last_updated = models.DateTimeField()
    fecha_final = models.DateField()
    descuento_financiero = models.DecimalField(max_digits=19, decimal_places=2)
    proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING)
    sw2 = models.BigIntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    linea = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'lista_de_precios_por_proveedor'


class ListaDePreciosPorProveedorDet(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    precio = models.DecimalField(max_digits=19, decimal_places=2)
    descuento1 = models.DecimalField(max_digits=19, decimal_places=2)
    last_updated = models.DateTimeField()
    moneda = models.CharField(max_length=255)
    precio_anterior = models.DecimalField(max_digits=19, decimal_places=2)
    descuento4 = models.DecimalField(max_digits=19, decimal_places=2)
    descuento_financiero = models.DecimalField(max_digits=19, decimal_places=2)
    descuento2 = models.DecimalField(max_digits=19, decimal_places=2)
    producto = models.ForeignKey('Producto', models.DO_NOTHING)
    descuento3 = models.DecimalField(max_digits=19, decimal_places=2)
    lista = models.ForeignKey(ListaDePreciosPorProveedor, models.DO_NOTHING)
    neto = models.DecimalField(max_digits=19, decimal_places=2)
    partidas_idx = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lista_de_precios_por_proveedor_det'


class ListaDePreciosVenta(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    folio = models.BigIntegerField(unique=True)
    date_created = models.DateTimeField()
    last_updated = models.DateTimeField()
    tipo_de_cambio_dolar = models.DecimalField(max_digits=19, decimal_places=6)
    sw2 = models.BigIntegerField(blank=True, null=True)
    autorizacion = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.CharField(max_length=255)
    inicio = models.DateTimeField()
    aplicada = models.DateTimeField(blank=True, null=True)
    linea = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'lista_de_precios_venta'


class ListaDePreciosVentaDet(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    last_updated = models.DateTimeField()
    incremento = models.DecimalField(max_digits=19, decimal_places=2)
    factor_credito = models.DecimalField(max_digits=19, decimal_places=2)
    precio_anterior_credito = models.DecimalField(max_digits=19, decimal_places=2)
    costo_ultimo = models.DecimalField(max_digits=19, decimal_places=2)
    proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, blank=True, null=True)
    precio_anterior_contado = models.DecimalField(max_digits=19, decimal_places=2)
    costo = models.DecimalField(max_digits=19, decimal_places=2)
    factor_contado = models.DecimalField(max_digits=19, decimal_places=2)
    precio_credito = models.DecimalField(max_digits=19, decimal_places=2)
    producto = models.ForeignKey('Producto', models.DO_NOTHING)
    precio_contado = models.DecimalField(max_digits=19, decimal_places=2)
    lista = models.ForeignKey(ListaDePreciosVenta, models.DO_NOTHING)
    partidas_idx = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lista_de_precios_venta_det'


class Marca(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    activa = models.TextField()  # This field type is a guess.
    date_created = models.DateTimeField()
    last_updated = models.DateTimeField()
    marca = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'marca'


class MesaDeEmpaque(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    empacador6 = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    empacador3 = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    empacador8 = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    empacador1 = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    empacador2 = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    cortador = models.ForeignKey('User', models.DO_NOTHING)
    empacador4 = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    empacador5 = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    fecha = models.DateTimeField()
    empacador7 = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mesa_de_empaque'


class MesaEmpaque(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    empacador6 = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    date_created = models.DateTimeField()
    last_updated = models.DateTimeField()
    empacador3 = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    empacador8 = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    empacador1 = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    empacador2 = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    cortador = models.ForeignKey('User', models.DO_NOTHING)
    empacador4 = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    empacador5 = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    fecha = models.DateTimeField()
    empacador7 = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mesa_empaque'


class ModuloTipo(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    tipo = models.CharField(max_length=255)
    modulo = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'modulo_tipo'


class Morralla(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    tipo = models.CharField(max_length=255)
    fecha = models.DateTimeField()
    comentario = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField()
    sucursal = models.ForeignKey('Sucursal', models.DO_NOTHING)
    importe = models.DecimalField(max_digits=19, decimal_places=2)
    create_user = models.CharField(max_length=255, blank=True, null=True)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    movimiento_de_cuenta_id = models.CharField(max_length=255, blank=True, null=True)
    proveedor = models.CharField(max_length=255, blank=True, null=True)
    egreso_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'morralla'


class MovimientoDeAlmacen(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    por_inventario = models.TextField()  # This field type is a guess.
    sucursal = models.ForeignKey('Sucursal', models.DO_NOTHING)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    tipo = models.CharField(max_length=255)
    fecha = models.DateTimeField()
    fecha_inventario = models.DateTimeField(blank=True, null=True)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    documento = models.BigIntegerField()
    create_user = models.CharField(max_length=255, blank=True, null=True)
    cancelado = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movimiento_de_almacen'


class MovimientoDeAlmacenDet(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    movimiento_de_almacen = models.ForeignKey(MovimientoDeAlmacen, models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    inventario = models.ForeignKey(Inventario, models.DO_NOTHING, blank=True, null=True)
    cantidad = models.DecimalField(max_digits=19, decimal_places=2)
    tipocis = models.CharField(max_length=255, blank=True, null=True)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    producto = models.ForeignKey('Producto', models.DO_NOTHING)
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    partidas_idx = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movimiento_de_almacen_det'


class MovimientoDeCuenta(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    forma_de_pago = models.CharField(max_length=255)
    last_updated = models.DateTimeField()
    referencia = models.CharField(max_length=255, blank=True, null=True)
    moneda = models.CharField(max_length=255)
    tipo_de_cambio = models.DecimalField(max_digits=19, decimal_places=6)
    tipo = models.CharField(max_length=255)
    fecha = models.DateField()
    comentario = models.CharField(max_length=255, blank=True, null=True)
    sw2 = models.BigIntegerField(blank=True, null=True)
    afavor = models.CharField(max_length=255)
    concepto = models.CharField(max_length=50, blank=True, null=True)
    cuenta = models.ForeignKey(CuentaDeBanco, models.DO_NOTHING)
    importe = models.DecimalField(max_digits=19, decimal_places=4)
    sucursal = models.CharField(max_length=255, blank=True, null=True)
    por_identificar = models.TextField(blank=True, null=True)  # This field type is a guess.
    concepto_reporte = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movimiento_de_cuenta'


class MovimientoDeTesoreria(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    folio = models.BigIntegerField()
    date_created = models.DateTimeField()
    fecha = models.DateField()
    comentario = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField()
    movimiento = models.ForeignKey(MovimientoDeCuenta, models.DO_NOTHING)
    concepto = models.CharField(max_length=255)
    cuenta = models.ForeignKey(CuentaDeBanco, models.DO_NOTHING)
    importe = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'movimiento_de_tesoreria'


class NotaDeCargo(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    total = models.DecimalField(max_digits=19, decimal_places=2)
    forma_de_pago = models.CharField(max_length=255)
    last_updated = models.DateTimeField()
    tipo_de_documento = models.CharField(max_length=255, blank=True, null=True)
    moneda = models.CharField(max_length=255)
    tipo_de_cambio = models.DecimalField(max_digits=19, decimal_places=6)
    cargo = models.DecimalField(max_digits=19, decimal_places=2)
    update_user = models.CharField(max_length=255)
    fecha = models.DateTimeField()
    cuenta_por_cobrar = models.ForeignKey(CuentaPorCobrar, models.DO_NOTHING, blank=True, null=True)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    impuesto = models.DecimalField(max_digits=19, decimal_places=2)
    documento = models.BigIntegerField()
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING)
    importe = models.DecimalField(max_digits=19, decimal_places=2)
    create_user = models.CharField(max_length=255)
    uso_de_cfdi = models.CharField(max_length=3)
    sucursal = models.ForeignKey('Sucursal', models.DO_NOTHING)
    serie = models.CharField(max_length=20)
    folio = models.BigIntegerField()
    tipo = models.CharField(max_length=255)
    tipo_de_calculo = models.CharField(max_length=10)
    cfdi = models.ForeignKey(Cfdi, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nota_de_cargo'


class NotaDeCargoDet(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    nota = models.ForeignKey(NotaDeCargo, models.DO_NOTHING)
    cuenta_por_cobrar = models.ForeignKey(CuentaPorCobrar, models.DO_NOTHING, blank=True, null=True)
    last_updated = models.DateTimeField()
    sw2 = models.CharField(max_length=255)
    concepto = models.CharField(max_length=255, blank=True, null=True)
    importe = models.DecimalField(max_digits=19, decimal_places=2)
    cargo = models.DecimalField(max_digits=19, decimal_places=2)
    partidas_idx = models.IntegerField(blank=True, null=True)
    documento_total = models.DecimalField(max_digits=19, decimal_places=2)
    total = models.DecimalField(max_digits=19, decimal_places=2)
    sucursal = models.CharField(max_length=20)
    documento_saldo = models.DecimalField(max_digits=19, decimal_places=2)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    documento_fecha = models.DateField()
    impuesto = models.DecimalField(max_digits=19, decimal_places=2)
    documento_tipo = models.CharField(max_length=10)
    documento = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'nota_de_cargo_det'


class NotaDeCredito(models.Model):
    id = models.BigIntegerField(primary_key=True)
    version = models.BigIntegerField()
    diferencia_fecha = models.DateTimeField()
    date_created = models.DateTimeField()
    tc = models.DecimalField(max_digits=19, decimal_places=4)
    total = models.DecimalField(max_digits=19, decimal_places=2)
    modo_de_calculo = models.CharField(max_length=255)
    last_updated = models.DateTimeField()
    sucursal = models.ForeignKey('Sucursal', models.DO_NOTHING)
    serie = models.CharField(max_length=20)
    moneda = models.CharField(max_length=255)
    aplicado = models.DecimalField(max_digits=19, decimal_places=2)
    impreso = models.DateTimeField()
    primera_aplicacion = models.DateTimeField()
    descuento = models.DecimalField(max_digits=19, decimal_places=2)
    folio = models.BigIntegerField()
    disponible = models.DecimalField(max_digits=19, decimal_places=2)
    diferencia = models.DecimalField(max_digits=19, decimal_places=2)
    tipo_de_operacion = models.CharField(max_length=255)
    tipo = models.CharField(max_length=12)
    fecha = models.DateTimeField()
    comentario = models.CharField(max_length=255, blank=True, null=True)
    autorizacion = models.ForeignKey(Autorizacion, models.DO_NOTHING)
    impuesto = models.DecimalField(max_digits=19, decimal_places=2)
    impuesto_tasa = models.DecimalField(max_digits=19, decimal_places=2)
    nombre = models.CharField(max_length=255)
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING)
    importe = models.DecimalField(max_digits=19, decimal_places=2)
    cfdi = models.ForeignKey(ComprobanteFiscal, models.DO_NOTHING, blank=True, null=True)
    cobro = models.ForeignKey(Cobro, models.DO_NOTHING, blank=True, null=True)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    tipo_cartera = models.CharField(max_length=3)
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    create_user = models.CharField(max_length=255, blank=True, null=True)
    rmd = models.BigIntegerField(blank=True, null=True)
    forma_de_pago = models.CharField(max_length=40, blank=True, null=True)
    rmd_sucursal = models.CharField(max_length=30, blank=True, null=True)
    sin_referencia = models.TextField()  # This field type is a guess.
    uso_de_cfdi = models.CharField(max_length=3, blank=True, null=True)
    descuento2 = models.DecimalField(max_digits=19, decimal_places=2)
    tipo_de_calculo = models.CharField(max_length=20, blank=True, null=True)
    financiero = models.TextField()  # This field type is a guess.
    base_del_calculo = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nota_de_credito'
        unique_together = (('serie', 'folio'),)


class NotaDeCreditoDet(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    cantidad = models.DecimalField(max_digits=19, decimal_places=2)
    nota = models.ForeignKey(NotaDeCredito, models.DO_NOTHING)
    last_updated = models.DateTimeField()
    unidad = models.CharField(max_length=100)
    valor_unitario = models.DecimalField(max_digits=19, decimal_places=2)
    descuento = models.DecimalField(max_digits=19, decimal_places=2)
    cuenta_por_cobrar = models.ForeignKey(CuentaPorCobrar, models.DO_NOTHING, blank=True, null=True)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.CharField(max_length=255)
    numero_de_identificacion = models.CharField(max_length=50)
    concepto = models.CharField(max_length=255)
    importe = models.DecimalField(max_digits=19, decimal_places=2)
    partidas_idx = models.IntegerField(blank=True, null=True)
    fecha_documento = models.DateField()
    tipo_de_documento = models.CharField(max_length=10)
    sucursal = models.CharField(max_length=20)
    total_documento = models.DecimalField(max_digits=19, decimal_places=2)
    saldo_documento = models.DecimalField(max_digits=19, decimal_places=2)
    documento = models.BigIntegerField()
    base = models.DecimalField(max_digits=19, decimal_places=2)
    impuesto = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'nota_de_credito_det'


class OtrosProductos(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    diferencia = models.DecimalField(max_digits=19, decimal_places=2)
    date_created = models.DateTimeField()
    cobro = models.ForeignKey(Cobro, models.DO_NOTHING)
    last_updated = models.DateTimeField()
    diferencia_fecha = models.DateTimeField(blank=True, null=True)
    create_user = models.CharField(max_length=255)
    update_user = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'otros_productos'


class Poliza(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    cierre = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField()
    manual = models.TextField()  # This field type is a guess.
    ejercicio = models.IntegerField()
    haber = models.DecimalField(max_digits=19, decimal_places=6)
    subtipo = models.CharField(max_length=30)
    debe = models.DecimalField(max_digits=19, decimal_places=6)
    folio = models.IntegerField()
    tipo = models.CharField(max_length=7)
    fecha = models.DateField()
    mes = models.IntegerField()
    concepto = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'poliza'
        unique_together = (('subtipo', 'mes', 'ejercicio', 'folio'),)


class PolizaDet(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    entidad = models.CharField(max_length=50, blank=True, null=True)
    date_created = models.DateTimeField()
    asiento = models.CharField(max_length=20, blank=True, null=True)
    last_updated = models.DateTimeField()
    poliza = models.ForeignKey(Poliza, models.DO_NOTHING)
    referencia = models.CharField(max_length=255, blank=True, null=True)
    haber = models.DecimalField(max_digits=19, decimal_places=2)
    debe = models.DecimalField(max_digits=19, decimal_places=2)
    origen = models.CharField(max_length=20, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    concepto = models.CharField(max_length=300, blank=True, null=True)
    cuenta = models.ForeignKey(CuentaContable, models.DO_NOTHING)
    partidas_idx = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'poliza_det'


class PolizaFolio(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    sub_tipo = models.CharField(max_length=50)
    folio = models.BigIntegerField()
    date_created = models.DateTimeField()
    mes = models.IntegerField()
    last_updated = models.DateTimeField()
    ejercicio = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'poliza_folio'
        unique_together = (('ejercicio', 'mes', 'sub_tipo', 'folio'),)


class PreciosPorCliente(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    descuento = models.DecimalField(max_digits=19, decimal_places=2)
    date_created = models.DateTimeField()
    activo = models.TextField()  # This field type is a guess.
    comentario = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField()
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    cliente_id = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'precios_por_cliente'


class PreciosPorClienteDet(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    precio = models.DecimalField(max_digits=19, decimal_places=2)
    clave = models.CharField(max_length=255)
    moneda = models.CharField(max_length=255)
    costo = models.DecimalField(max_digits=19, decimal_places=2)
    tipo_de_cambio = models.CharField(max_length=255)
    precio_de_lista = models.DecimalField(max_digits=19, decimal_places=2)
    descuento = models.DecimalField(max_digits=19, decimal_places=2)
    precios_por_cliente_id = models.CharField(max_length=255)
    costop = models.DecimalField(max_digits=19, decimal_places=2)
    producto_id = models.CharField(max_length=255)
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.CharField(max_length=255)
    precio_por_kilo = models.DecimalField(max_digits=19, decimal_places=2)
    costou = models.DecimalField(max_digits=19, decimal_places=2)
    partidas_idx = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'precios_por_cliente_det'


class Producto(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    acabado = models.CharField(max_length=20, blank=True, null=True)
    activo = models.TextField()  # This field type is a guess.
    ajuste = models.BigIntegerField()
    ancho = models.DecimalField(db_column='ANCHO', max_digits=19, decimal_places=3)  # Field name made lowercase.
    calibre = models.DecimalField(max_digits=19, decimal_places=2)
    caras = models.IntegerField()
    clase = models.ForeignKey(Clase, models.DO_NOTHING, blank=True, null=True)
    clave = models.CharField(max_length=255)
    codigo = models.CharField(max_length=255, blank=True, null=True)
    color = models.CharField(max_length=15, blank=True, null=True)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField()
    de_linea = models.TextField()  # This field type is a guess.
    descripcion = models.CharField(max_length=255)
    fecha_lista = models.DateTimeField(blank=True, null=True)
    gramos = models.DecimalField(max_digits=19, decimal_places=2)
    inventariable = models.TextField()  # This field type is a guess.
    kilos = models.DecimalField(max_digits=19, decimal_places=3)
    largo = models.DecimalField(max_digits=19, decimal_places=3)
    last_updated = models.DateTimeField()
    linea = models.ForeignKey(Linea, models.DO_NOTHING, blank=True, null=True)
    m2xmillar = models.DecimalField(max_digits=19, decimal_places=3)
    marca = models.ForeignKey(Marca, models.DO_NOTHING, blank=True, null=True)
    modo_venta = models.CharField(max_length=1)
    nacional = models.TextField()  # This field type is a guess.
    precio_contado = models.DecimalField(max_digits=19, decimal_places=2)
    precio_credito = models.DecimalField(max_digits=19, decimal_places=2)
    presentacion = models.CharField(max_length=9)
    proveedor_favorito = models.ForeignKey('Proveedor', models.DO_NOTHING, blank=True, null=True)
    sw2 = models.BigIntegerField(blank=True, null=True)
    unidad = models.CharField(max_length=10)
    clase_0 = models.CharField(db_column='clase', max_length=255, blank=True, null=True)  # Field renamed because of name conflict.
    linea_0 = models.CharField(db_column='linea', max_length=255, blank=True, null=True)  # Field renamed because of name conflict.
    marca_0 = models.CharField(db_column='marca', max_length=255, blank=True, null=True)  # Field renamed because of name conflict.
    producto_sat = models.ForeignKey('ProductoSat', models.DO_NOTHING, blank=True, null=True)
    unidad_sat = models.ForeignKey('UnidadSat', models.DO_NOTHING, blank=True, null=True)
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
    precio_tarjeta = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producto'


class ProductoSat(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    clave_prod_serv = models.CharField(unique=True, max_length=255)
    descripcion = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'producto_sat'


class ProductoServicio(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    cuenta_contable = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'producto_servicio'


class Proveedor(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    activo = models.TextField()  # This field type is a guess.
    clave = models.CharField(unique=True, max_length=255)
    cuenta_bancaria = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField()
    last_updated = models.DateTimeField()
    nacional = models.TextField()  # This field type is a guess.
    nombre = models.CharField(unique=True, max_length=255)
    rfc = models.CharField(max_length=13)
    sw2 = models.BigIntegerField(blank=True, null=True)
    telefono1 = models.CharField(max_length=30, blank=True, null=True)
    telefono2 = models.CharField(max_length=30, blank=True, null=True)
    telefono3 = models.CharField(max_length=30, blank=True, null=True)
    tipo = models.CharField(max_length=26)
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
    plazo = models.IntegerField()
    fecha_revision = models.IntegerField(blank=True, null=True)
    imprimir_costo = models.IntegerField(blank=True, null=True)
    descuentof = models.BigIntegerField(blank=True, null=True)
    diasdf = models.BigIntegerField(blank=True, null=True)
    limite_de_credito = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    create_user = models.CharField(max_length=255, blank=True, null=True)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    banco = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proveedor'


class ProveedorCompras(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    cuenta_contable = models.CharField(max_length=255, blank=True, null=True)
    descuentof = models.BigIntegerField()
    diasdf = models.BigIntegerField()
    fecha_revision = models.TextField()  # This field type is a guess.
    imprimir_costo = models.TextField()  # This field type is a guess.
    plazo = models.BigIntegerField()
    proveedor = models.ForeignKey(Proveedor, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proveedor_compras'


class ProveedorComunicacionEmpresa(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    activo = models.TextField()  # This field type is a guess.
    comentario = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    proveedor = models.ForeignKey(Proveedor, models.DO_NOTHING)
    sw2 = models.BigIntegerField()
    tipo = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'proveedor_comunicacion_empresa'


class ProveedorContactos(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    activo = models.TextField()  # This field type is a guess.
    email = models.CharField(max_length=255, blank=True, null=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    proveedor = models.ForeignKey(Proveedor, models.DO_NOTHING)
    puesto = models.CharField(max_length=255, blank=True, null=True)
    sw2 = models.BigIntegerField()
    telefono = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proveedor_contactos'


class ProveedorDeFlete(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'proveedor_de_flete'


class ProveedorProducto(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    clave_proveedor = models.CharField(max_length=255, blank=True, null=True)
    codigo_proveedor = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    descripcion_proveedor = models.CharField(max_length=255, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    paquete_tarima = models.IntegerField()
    pieza_paquete = models.IntegerField()
    precio = models.DecimalField(max_digits=19, decimal_places=2)
    producto = models.ForeignKey(Producto, models.DO_NOTHING)
    proveedor = models.ForeignKey(Proveedor, models.DO_NOTHING)
    precio_bruto = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    moneda = models.CharField(max_length=5, blank=True, null=True)
    desc3 = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    aplicado = models.DateTimeField(blank=True, null=True)
    desc2 = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    desc1 = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    desc4 = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    lista = models.BigIntegerField(blank=True, null=True)
    create_user = models.CharField(max_length=255, blank=True, null=True)
    suspendido = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proveedor_producto'


class RecepcionDeCompra(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    sucursal = models.ForeignKey('Sucursal', models.DO_NOTHING)
    compra = models.ForeignKey(Compra, models.DO_NOTHING)
    remision = models.CharField(max_length=255, blank=True, null=True)
    proveedor = models.ForeignKey(Proveedor, models.DO_NOTHING)
    fecha_remision = models.DateTimeField(blank=True, null=True)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    fecha = models.DateField()
    fecha_inventario = models.DateTimeField(blank=True, null=True)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    documento = models.BigIntegerField()
    create_user = models.CharField(max_length=255, blank=True, null=True)
    cancelado = models.DateTimeField(blank=True, null=True)
    pendiente_de_analisis = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recepcion_de_compra'


class RecepcionDeCompraDet(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    cantidad = models.DecimalField(max_digits=19, decimal_places=2)
    inventario = models.ForeignKey(Inventario, models.DO_NOTHING, blank=True, null=True)
    recepcion = models.ForeignKey(RecepcionDeCompra, models.DO_NOTHING)
    last_updated = models.DateTimeField()
    kilos = models.DecimalField(max_digits=19, decimal_places=2)
    compra_det = models.ForeignKey(CompraDet, models.DO_NOTHING, blank=True, null=True)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    producto = models.ForeignKey(Producto, models.DO_NOTHING)
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    partidas_idx = models.IntegerField(blank=True, null=True)
    devuelto = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    analizado = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    inventariox = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recepcion_de_compra_det'


class Recorte(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    comentario = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField()
    producto = models.ForeignKey(Producto, models.DO_NOTHING)
    sucursal = models.ForeignKey('Sucursal', models.DO_NOTHING)
    create_user = models.CharField(max_length=255)
    update_user = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'recorte'


class RecorteDet(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    fecha = models.DateTimeField()
    cantidad = models.DecimalField(max_digits=19, decimal_places=2)
    clasificacion = models.CharField(max_length=10)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    responsable1 = models.CharField(max_length=255)
    responsable2 = models.CharField(max_length=255, blank=True, null=True)
    create_user = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'recorte_det'


class RecorteRecorteDet(models.Model):
    recorte_partidas_id = models.CharField(max_length=255)
    recorte_det = models.ForeignKey(RecorteDet, models.DO_NOTHING, blank=True, null=True)
    partidas_idx = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recorte_recorte_det'


class Requisicion(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    total = models.DecimalField(max_digits=19, decimal_places=4)
    forma_de_pago = models.CharField(max_length=13)
    last_updated = models.DateTimeField()
    moneda = models.CharField(max_length=255)
    descuento_financiero = models.DecimalField(max_digits=19, decimal_places=4)
    proveedor = models.ForeignKey(Proveedor, models.DO_NOTHING)
    tipo_de_cambio = models.DecimalField(max_digits=19, decimal_places=2)
    fecha_de_pago = models.DateField()
    tipo = models.CharField(max_length=7)
    fecha = models.DateField()
    comentario = models.CharField(max_length=255, blank=True, null=True)
    autorizacion = models.ForeignKey(Autorizacion, models.DO_NOTHING, blank=True, null=True)
    sw2 = models.BigIntegerField(blank=True, null=True)
    afavor = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'requisicion'


class RequisicionDeMaterial(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    clave = models.CharField(max_length=15)
    last_updated = models.DateTimeField()
    sucursal = models.CharField(max_length=255)
    compra = models.CharField(max_length=255, blank=True, null=True)
    moneda = models.CharField(max_length=3)
    rfc = models.CharField(max_length=14)
    proveedor = models.CharField(max_length=255)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    folio = models.BigIntegerField()
    fecha = models.DateField()
    comentario = models.CharField(max_length=255, blank=True, null=True)
    cerrada = models.DateField(blank=True, null=True)
    create_user = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'requisicion_de_material'
        unique_together = (('sucursal', 'folio'),)


class RequisicionDeMaterialDet(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    solicitado = models.DecimalField(max_digits=19, decimal_places=2)
    date_created = models.DateTimeField()
    last_updated = models.DateTimeField()
    unidad = models.CharField(max_length=10)
    sucursal = models.CharField(max_length=255)
    requisicion = models.ForeignKey(RequisicionDeMaterial, models.DO_NOTHING)
    update_user = models.CharField(max_length=255)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    producto = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=255)
    create_user = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'requisicion_de_material_det'


class RequisicionDet(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    cxp = models.ForeignKey(CuentaPorPagar, models.DO_NOTHING, blank=True, null=True)
    analizado = models.DecimalField(max_digits=19, decimal_places=2)
    date_created = models.DateTimeField()
    a_pagar = models.DecimalField(max_digits=19, decimal_places=2)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField()
    requisicion = models.ForeignKey(Requisicion, models.DO_NOTHING)
    descuento_financiero = models.DecimalField(max_digits=19, decimal_places=2)
    partidas_idx = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'requisicion_det'


class Role(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    authority = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'role'


class Ruteo(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    d_tipo_asentamiento = models.CharField(max_length=255)
    d_cp = models.CharField(max_length=255)
    c_oficina = models.CharField(max_length=255)
    c_cp = models.CharField(max_length=255)
    d_municipio = models.CharField(max_length=255)
    d_asentamiento = models.CharField(max_length=255)
    d_zona = models.CharField(max_length=255)
    d_ciudad = models.CharField(max_length=255)
    c_municipio = models.CharField(max_length=255)
    d_codigo = models.CharField(max_length=255)
    id_asentamiento_cp = models.CharField(max_length=255)
    d_estado = models.CharField(max_length=255)
    c_tipo_asentamiento = models.CharField(max_length=255)
    suc_asignada = models.ForeignKey('Sucursal', models.DO_NOTHING, blank=True, null=True)
    c_cve_ciudad = models.CharField(max_length=255)
    c_estado = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ruteo'


class SaldoPorCuentaDeBanco(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    egresos = models.DecimalField(max_digits=19, decimal_places=2)
    saldo_inicial = models.DecimalField(max_digits=19, decimal_places=2)
    date_created = models.DateTimeField()
    saldo_final = models.DecimalField(max_digits=19, decimal_places=2)
    cierre = models.DateTimeField(blank=True, null=True)
    mes = models.IntegerField()
    last_updated = models.DateTimeField()
    ejercicio = models.IntegerField()
    ingresos = models.DecimalField(max_digits=19, decimal_places=2)
    cuenta = models.ForeignKey(CuentaDeBanco, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'saldo_por_cuenta_de_banco'
        unique_together = (('mes', 'ejercicio', 'cuenta'),)


class SatBanco(models.Model):
    id = models.BigIntegerField(primary_key=True)
    version = models.BigIntegerField()
    clave = models.CharField(unique=True, max_length=20)
    nombre_corto = models.CharField(max_length=255)
    razon_social = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'sat_banco'


class SatCuenta(models.Model):
    id = models.BigIntegerField(primary_key=True)
    version = models.BigIntegerField()
    codigo = models.CharField(unique=True, max_length=20)
    nivel = models.IntegerField()
    nombre = models.CharField(max_length=255)
    tipo = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sat_cuenta'


class Sector(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    comentario = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField()
    responsable1 = models.CharField(max_length=255, blank=True, null=True)
    sucursal = models.ForeignKey('Sucursal', models.DO_NOTHING)
    sector_folio = models.BigIntegerField()
    responsable2 = models.CharField(max_length=255, blank=True, null=True)
    create_user = models.CharField(max_length=255, blank=True, null=True)
    update_user = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sector'


class SectorDet(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    cantidad = models.DecimalField(max_digits=19, decimal_places=2)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    producto = models.ForeignKey(Producto, models.DO_NOTHING)
    indice = models.DecimalField(max_digits=19, decimal_places=2)
    sector = models.ForeignKey(Sector, models.DO_NOTHING)
    partidas_idx = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sector_det'


class Socio(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    clave = models.CharField(max_length=255)
    sw2 = models.BigIntegerField(blank=True, null=True)
    vendedor = models.ForeignKey('Vendedor', models.DO_NOTHING, blank=True, null=True)
    nombre = models.CharField(max_length=255)
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING)
    comision_cobrador = models.DecimalField(max_digits=19, decimal_places=2)
    comision_vendedor = models.DecimalField(max_digits=19, decimal_places=2)
    direccion = models.CharField(max_length=255)
    direccion_fiscal_numero_exterior = models.CharField(max_length=50, blank=True, null=True)
    direccion_fiscal_numero_interior = models.CharField(max_length=50, blank=True, null=True)
    direccion_fiscal_latitud = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    direccion_fiscal_longitud = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    direccion_fiscal_estado = models.CharField(max_length=255, blank=True, null=True)
    direccion_fiscal_pais = models.CharField(max_length=100, blank=True, null=True)
    direccion_fiscal_calle = models.CharField(max_length=200, blank=True, null=True)
    direccion_fiscal_colonia = models.CharField(max_length=255, blank=True, null=True)
    direccion_fiscal_codigo_postal = models.CharField(max_length=255, blank=True, null=True)
    direccion_fiscal_municipio = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'socio'


class SolicitudCambio(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    comentario_autorizacion = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField()
    documento_desrcipcion = models.CharField(max_length=255, blank=True, null=True)
    fecha_documento = models.CharField(max_length=255, blank=True, null=True)
    autorizo = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    last_updated = models.DateTimeField()
    estado = models.CharField(max_length=10)
    sucursal = models.ForeignKey('Sucursal', models.DO_NOTHING)
    atencion = models.DateTimeField(blank=True, null=True)
    solicitud = models.DateTimeField(blank=True, null=True)
    folio = models.IntegerField()
    tipo = models.CharField(max_length=255, blank=True, null=True)
    fecha = models.DateTimeField()
    usuario = models.ForeignKey('User', models.DO_NOTHING)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    comentario_atencion = models.CharField(max_length=255, blank=True, null=True)
    autorizacion = models.DateTimeField(blank=True, null=True)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    documento = models.CharField(max_length=255, blank=True, null=True)
    atendio = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    modulo = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'solicitud_cambio'


class SolicitudDeDeposito(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    cheque = models.DecimalField(max_digits=19, decimal_places=2)
    date_created = models.DateTimeField()
    cobro = models.ForeignKey(Cobro, models.DO_NOTHING, blank=True, null=True)
    total = models.DecimalField(max_digits=19, decimal_places=2)
    last_updated = models.DateTimeField()
    sucursal = models.ForeignKey('Sucursal', models.DO_NOTHING)
    referencia = models.CharField(max_length=255)
    cancelacion = models.DateTimeField(blank=True, null=True)
    transferencia = models.DecimalField(max_digits=19, decimal_places=2)
    efectivo = models.DecimalField(max_digits=19, decimal_places=2)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    folio = models.IntegerField()
    tipo = models.CharField(max_length=255)
    banco = models.ForeignKey(Banco, models.DO_NOTHING)
    fecha = models.DateTimeField()
    comentario = models.CharField(max_length=255, blank=True, null=True)
    enviado = models.TextField()  # This field type is a guess.
    fecha_deposito = models.DateField(blank=True, null=True)
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    cuenta = models.ForeignKey(CuentaDeBanco, models.DO_NOTHING)
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING)
    create_user = models.CharField(max_length=255, blank=True, null=True)
    cancelacion_comentario = models.CharField(max_length=255, blank=True, null=True)
    tarjeta = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    autorizacion = models.ForeignKey(Autorizacion, models.DO_NOTHING, blank=True, null=True)
    auth_uid = models.CharField(max_length=30, blank=True, null=True)
    auth_fecha = models.DateTimeField(blank=True, null=True)
    auth_comentario = models.CharField(max_length=200, blank=True, null=True)
    auth_create_user = models.CharField(max_length=50, blank=True, null=True)
    rechazo_motivo = models.CharField(max_length=50, blank=True, null=True)
    rechazo_uid = models.CharField(max_length=30, blank=True, null=True)
    rechazo_date_created = models.DateTimeField(blank=True, null=True)
    rechazo_comentario = models.CharField(max_length=250, blank=True, null=True)
    rechazo_replicado = models.DateTimeField(blank=True, null=True)
    rechazo_create_user = models.CharField(max_length=50, blank=True, null=True)
    replicado_firestore = models.DateTimeField(blank=True, null=True)
    callcenter = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'solicitud_de_deposito'


class SolicitudDeTraslado(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    referencia = models.CharField(max_length=255, blank=True, null=True)
    clasificacion_vale = models.CharField(max_length=255, blank=True, null=True)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    fecha = models.DateTimeField()
    sucursal_solicita = models.ForeignKey('Sucursal', models.DO_NOTHING)
    fecha_inventario = models.DateTimeField(blank=True, null=True)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    documento = models.BigIntegerField()
    no_atender = models.TextField()  # This field type is a guess.
    sucursal_atiende = models.ForeignKey('Sucursal', models.DO_NOTHING)
    create_user = models.CharField(max_length=255, blank=True, null=True)
    venta = models.CharField(max_length=255, blank=True, null=True)
    atender = models.DateTimeField(blank=True, null=True)
    cancelado = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'solicitud_de_traslado'


class SolicitudDeTrasladoDet(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    recibido = models.DecimalField(max_digits=19, decimal_places=2)
    cortes = models.BigIntegerField()
    cortes_instruccion = models.CharField(max_length=255, blank=True, null=True)
    solicitado = models.DecimalField(max_digits=19, decimal_places=2)
    date_created = models.DateTimeField()
    solicitud_de_traslado = models.ForeignKey(SolicitudDeTraslado, models.DO_NOTHING)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField()
    producto = models.ForeignKey(Producto, models.DO_NOTHING)
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    partidas_idx = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'solicitud_de_traslado_det'


class SubTipoDePoliza(models.Model):
    id = models.BigIntegerField(primary_key=True)
    version = models.BigIntegerField()
    orden = models.IntegerField()
    tipo = models.CharField(max_length=7)
    clave = models.CharField(unique=True, max_length=20)
    procesador = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'sub_tipo_de_poliza'


class Sucursal(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    activa = models.TextField()  # This field type is a guess.
    clave = models.CharField(unique=True, max_length=20)
    date_created = models.DateTimeField()
    last_updated = models.DateTimeField()
    nombre = models.CharField(unique=True, max_length=255)
    sw2 = models.BigIntegerField(blank=True, null=True)
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
    almacen = models.TextField()  # This field type is a guess.
    db_url = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'sucursal'


class Surtido(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    entidad = models.CharField(max_length=3)
    depurado = models.DateTimeField(blank=True, null=True)
    cerro = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    entregado = models.DateTimeField(blank=True, null=True)
    valido = models.TextField()  # This field type is a guess.
    depurado_usuario = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    kilos = models.DecimalField(max_digits=19, decimal_places=2)
    folio_fac = models.BigIntegerField()
    tipo_de_venta = models.CharField(max_length=255)
    clasificacion_vale = models.CharField(max_length=255)
    user_last_update = models.ForeignKey('User', models.DO_NOTHING)
    revision_usuario = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    origen = models.CharField(max_length=255)
    corte_inicio = models.DateTimeField(blank=True, null=True)
    entrega_local = models.TextField()  # This field type is a guess.
    reimportado = models.TextField()  # This field type is a guess.
    asignacion_corte = models.DateTimeField(blank=True, null=True)
    entrego = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    cortador = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    tiempo_surtido = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    fecha = models.DateTimeField()
    comentario = models.CharField(max_length=255, blank=True, null=True)
    kilos_corte = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    prods_corte = models.IntegerField(blank=True, null=True)
    comportamiento = models.CharField(max_length=255, blank=True, null=True)
    corte_fin = models.DateTimeField(blank=True, null=True)
    documento = models.BigIntegerField()
    iniciado = models.DateTimeField(blank=True, null=True)
    asignado = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    revision = models.DateTimeField(blank=True, null=True)
    nombre = models.CharField(max_length=255)
    prods = models.IntegerField()
    tiempo_corte = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    parcial = models.TextField()  # This field type is a guess.
    cierre_surtido = models.DateTimeField(blank=True, null=True)
    date_created = models.DateTimeField()
    autorizo = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    last_updated = models.DateTimeField()
    estado = models.CharField(max_length=255)
    inicio = models.DateTimeField(blank=True, null=True)
    depuro = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    tipo = models.CharField(max_length=3)
    reviso = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    cancelo = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    facturo = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    cancelado = models.DateTimeField(blank=True, null=True)
    revisado = models.DateTimeField(blank=True, null=True)
    asignado_corte = models.DateTimeField(blank=True, null=True)
    cerrado = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'surtido'


class SurtidoAuxiliar(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    auxiliar_surtido = models.ForeignKey('User', models.DO_NOTHING)
    surtido = models.ForeignKey(Surtido, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'surtido_auxiliar'


class SurtidoDet(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    valor = models.DecimalField(max_digits=19, decimal_places=2)
    instruccion_de_entrega_parcial = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField()
    cantidad = models.DecimalField(max_digits=19, decimal_places=2)
    entrega_parcial_det = models.CharField(max_length=255)
    clave = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField()
    surtido = models.ForeignKey(Surtido, models.DO_NOTHING)
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    parciales_idx = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'surtido_det'


class Tarjeta(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'tarjeta'


class TipoDeCambio(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    fecha = models.DateField()
    fuente = models.CharField(max_length=200)
    last_updated = models.DateTimeField()
    moneda = models.CharField(max_length=255)
    tipo_de_cambio = models.DecimalField(max_digits=19, decimal_places=6)

    class Meta:
        managed = False
        db_table = 'tipo_de_cambio'


class Transformacion(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    por_inventario = models.TextField(blank=True, null=True)  # This field type is a guess.
    venta = models.ForeignKey('Venta', models.DO_NOTHING, blank=True, null=True)
    sucursal = models.ForeignKey(Sucursal, models.DO_NOTHING)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    tipo = models.CharField(max_length=255, blank=True, null=True)
    fecha = models.DateTimeField()
    fecha_inventario = models.DateTimeField(blank=True, null=True)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    autorizacion = models.ForeignKey(Autorizacion, models.DO_NOTHING, blank=True, null=True)
    documento = models.BigIntegerField()
    create_user = models.CharField(max_length=255, blank=True, null=True)
    cancelado = models.DateField(blank=True, null=True)
    surtido = models.IntegerField(blank=True, null=True)
    chofer_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transformacion'


class TransformacionDet(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    cortes = models.BigIntegerField()
    date_created = models.DateTimeField(blank=True, null=True)
    cantidad = models.DecimalField(max_digits=19, decimal_places=2)
    inventario = models.ForeignKey(Inventario, models.DO_NOTHING, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    transformacion = models.ForeignKey(Transformacion, models.DO_NOTHING)
    cortes_instruccion = models.CharField(max_length=255, blank=True, null=True)
    destino = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    producto = models.ForeignKey(Producto, models.DO_NOTHING)
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    partidas_idx = models.IntegerField(blank=True, null=True)
    costo = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transformacion_det'


class Transporte(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    chofer = models.ForeignKey(Chofer, models.DO_NOTHING, blank=True, null=True)
    date_created = models.DateTimeField()
    last_updated = models.DateTimeField()
    capacidad = models.DecimalField(max_digits=19, decimal_places=2)
    modelo = models.CharField(max_length=255, blank=True, null=True)
    numero = models.CharField(max_length=30)
    facturista = models.ForeignKey(FacturistaDeEmbarque, models.DO_NOTHING, blank=True, null=True)
    placa = models.CharField(max_length=255, blank=True, null=True)
    marca = models.CharField(max_length=255, blank=True, null=True)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.CharField(max_length=255)
    anio = models.CharField(max_length=255, blank=True, null=True)
    create_user = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transporte'


class TransporteEmpresa(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    telefono3 = models.CharField(max_length=255, blank=True, null=True)
    telefono2 = models.CharField(max_length=255, blank=True, null=True)
    nombre = models.CharField(max_length=255)
    telefono1 = models.CharField(max_length=255, blank=True, null=True)
    direccion_numero_exterior = models.CharField(max_length=50, blank=True, null=True)
    direccion_numero_interior = models.CharField(max_length=50, blank=True, null=True)
    direccion_latitud = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    direccion_longitud = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    direccion_estado = models.CharField(max_length=255, blank=True, null=True)
    direccion_pais = models.CharField(max_length=100, blank=True, null=True)
    direccion_calle = models.CharField(max_length=200, blank=True, null=True)
    direccion_colonia = models.CharField(max_length=255, blank=True, null=True)
    direccion_codigo_postal = models.CharField(max_length=255, blank=True, null=True)
    direccion_municipio = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transporte_empresa'


class Traslado(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    date_created = models.DateTimeField(blank=True, null=True)
    inventario = models.ForeignKey(Inventario, models.DO_NOTHING, blank=True, null=True)
    solicitud_de_traslado = models.ForeignKey(SolicitudDeTraslado, models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    por_inventario = models.TextField(blank=True, null=True)  # This field type is a guess.
    kilos = models.DecimalField(max_digits=19, decimal_places=2)
    sucursal = models.ForeignKey(Sucursal, models.DO_NOTHING)
    clasificacion_vale = models.CharField(max_length=255, blank=True, null=True)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    tipo = models.CharField(max_length=255, blank=True, null=True)
    fecha = models.DateTimeField()
    fecha_inventario = models.DateTimeField(blank=True, null=True)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    documento = models.BigIntegerField()
    asignado = models.DateTimeField(blank=True, null=True)
    cfdi = models.ForeignKey(Cfdi, models.DO_NOTHING, blank=True, null=True)
    create_user = models.CharField(max_length=255, blank=True, null=True)
    chofer = models.ForeignKey(Chofer, models.DO_NOTHING, blank=True, null=True)
    uuid = models.CharField(max_length=255, blank=True, null=True)
    cancelado = models.DateField(blank=True, null=True)
    surtido = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'traslado'


class TrasladoDet(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    cortes = models.BigIntegerField()
    solicitado = models.DecimalField(max_digits=19, decimal_places=2)
    date_created = models.DateTimeField()
    cantidad = models.DecimalField(max_digits=19, decimal_places=2)
    inventario = models.ForeignKey(Inventario, models.DO_NOTHING, blank=True, null=True)
    last_updated = models.DateTimeField()
    kilos = models.DecimalField(max_digits=19, decimal_places=2)
    cortes_instruccion = models.CharField(max_length=255, blank=True, null=True)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    producto = models.ForeignKey(Producto, models.DO_NOTHING)
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    traslado = models.ForeignKey(Traslado, models.DO_NOTHING)
    partidas_idx = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'traslado_det'


class Traspaso(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    comision = models.DecimalField(max_digits=19, decimal_places=2)
    date_created = models.DateTimeField()
    last_updated = models.DateTimeField()
    cuenta_origen = models.ForeignKey(CuentaDeBanco, models.DO_NOTHING)
    moneda = models.CharField(max_length=255)
    cuenta_destino = models.ForeignKey(CuentaDeBanco, models.DO_NOTHING)
    fecha = models.DateField()
    comentario = models.CharField(max_length=255)
    impuesto = models.DecimalField(max_digits=19, decimal_places=2)
    importe = models.DecimalField(max_digits=19, decimal_places=2)
    class_field = models.CharField(db_column='class', max_length=255)  # Field renamed because it was a Python reserved word.
    rendimiento_calculado = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    tasa_isr = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    rendimiento_fecha = models.DateField(blank=True, null=True)
    plazo = models.IntegerField(blank=True, null=True)
    tasa = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    rendimiento_real = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    vencimiento = models.DateTimeField(blank=True, null=True)
    importe_isr = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    rendimiento_impuesto = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'traspaso'


class TraspasoMovimientoDeCuenta(models.Model):
    traspaso_movimientos = models.ForeignKey(Traspaso, models.DO_NOTHING)
    movimiento_de_cuenta = models.ForeignKey(MovimientoDeCuenta, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'traspaso_movimiento_de_cuenta'


class UnidadSat(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    clave_unidad_sat = models.CharField(max_length=255, blank=True, null=True)
    unidad_sat = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unidad_sat'


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    account_expired = models.TextField()  # This field type is a guess.
    account_locked = models.TextField()  # This field type is a guess.
    apellido_materno = models.CharField(max_length=255)
    apellido_paterno = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True, null=True)
    enabled = models.TextField()  # This field type is a guess.
    nombre = models.CharField(max_length=255)
    nombres = models.CharField(max_length=255)
    numero_de_empleado = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=255)
    password_expired = models.TextField()  # This field type is a guess.
    puesto = models.CharField(max_length=30, blank=True, null=True)
    sucursal = models.CharField(max_length=20, blank=True, null=True)
    username = models.CharField(unique=True, max_length=255)
    nip = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class UserRole(models.Model):
    user = models.OneToOneField(User, models.DO_NOTHING, primary_key=True)
    role = models.ForeignKey(Role, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_role'
        unique_together = (('user', 'role'),)


class UserTemp(models.Model):
    id = models.BigIntegerField()
    version = models.BigIntegerField()
    account_expired = models.TextField()  # This field type is a guess.
    account_locked = models.TextField()  # This field type is a guess.
    apellido_materno = models.CharField(max_length=255)
    apellido_paterno = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True, null=True)
    enabled = models.TextField()  # This field type is a guess.
    nombre = models.CharField(max_length=255)
    nombres = models.CharField(max_length=255)
    numero_de_empleado = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=255)
    password_expired = models.TextField()  # This field type is a guess.
    puesto = models.CharField(max_length=30, blank=True, null=True)
    sucursal = models.CharField(max_length=20, blank=True, null=True)
    username = models.CharField(max_length=255)
    nip = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_temp'


class Vendedor(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    activo = models.TextField(blank=True, null=True)  # This field type is a guess.
    apellido_materno = models.CharField(max_length=255, blank=True, null=True)
    apellido_paterno = models.CharField(max_length=255, blank=True, null=True)
    comision_contado = models.DecimalField(max_digits=19, decimal_places=2)
    comision_credito = models.DecimalField(max_digits=19, decimal_places=2)
    curp = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField()
    last_updated = models.DateTimeField()
    nombres = models.CharField(max_length=255, blank=True, null=True)
    rfc = models.CharField(max_length=255, blank=True, null=True)
    sw2 = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vendedor'


class Venta(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    comision_tarjeta_importe = models.DecimalField(max_digits=19, decimal_places=2)
    vale = models.TextField()  # This field type is a guess.
    facturar = models.DateTimeField(blank=True, null=True)
    date_created = models.DateTimeField()
    cfdi_mail = models.CharField(max_length=255, blank=True, null=True)
    total = models.DecimalField(max_digits=19, decimal_places=2)
    forma_de_pago = models.CharField(max_length=255)
    last_updated = models.DateTimeField()
    uso_de_cfdi = models.CharField(max_length=3, blank=True, null=True)
    kilos = models.DecimalField(max_digits=19, decimal_places=2)
    sucursal = models.ForeignKey(Sucursal, models.DO_NOTHING)
    descuento_original = models.DecimalField(max_digits=19, decimal_places=2)
    moneda = models.CharField(max_length=255)
    vendedor = models.ForeignKey(Vendedor, models.DO_NOTHING)
    atencion = models.CharField(max_length=10)
    corte_importe = models.DecimalField(max_digits=19, decimal_places=2)
    puesto = models.DateTimeField(blank=True, null=True)
    clasificacion_vale = models.CharField(max_length=30, blank=True, null=True)
    impreso = models.DateTimeField(blank=True, null=True)
    tipo_de_cambio = models.DecimalField(max_digits=19, decimal_places=6)
    descuento_importe = models.DecimalField(max_digits=19, decimal_places=2)
    update_user = models.CharField(max_length=100, blank=True, null=True)
    cod = models.TextField()  # This field type is a guess.
    descuento = models.DecimalField(max_digits=19, decimal_places=2)
    tipo = models.CharField(max_length=3)
    sucursal_vale = models.ForeignKey(Sucursal, models.DO_NOTHING, blank=True, null=True)
    fecha = models.DateField()
    comision_tarjeta = models.DecimalField(max_digits=19, decimal_places=2)
    cuenta_por_cobrar = models.ForeignKey(CuentaPorCobrar, models.DO_NOTHING, blank=True, null=True)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    sucursal_venta = models.ForeignKey(Sucursal, models.DO_NOTHING, blank=True, null=True)
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    impuesto = models.DecimalField(max_digits=19, decimal_places=2)
    subtotal = models.DecimalField(max_digits=19, decimal_places=2)
    documento = models.BigIntegerField()
    cargos_por_maniobra = models.DecimalField(max_digits=19, decimal_places=2)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    cliente = models.ForeignKey(Cliente, models.DO_NOTHING)
    comprador = models.CharField(max_length=255, blank=True, null=True)
    parcial = models.TextField()  # This field type is a guess.
    importe = models.DecimalField(max_digits=19, decimal_places=2)
    create_user = models.CharField(max_length=100, blank=True, null=True)
    sin_existencia = models.TextField(blank=True, null=True)  # This field type is a guess.
    socio = models.ForeignKey(Socio, models.DO_NOTHING, blank=True, null=True)
    cheque_post_fechado = models.TextField(blank=True, null=True)  # This field type is a guess.
    facturar_usuario = models.CharField(max_length=255, blank=True, null=True)
    venta_ine = models.TextField(blank=True, null=True)  # This field type is a guess.
    no_facturable = models.TextField(blank=True, null=True)  # This field type is a guess.
    surtido = models.TextField()  # This field type is a guess.
    callcenter = models.TextField()  # This field type is a guess.
    callcenter_version = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'venta'


class VentaAnticipo(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    venta = models.ForeignKey(Venta, models.DO_NOTHING)
    importe = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'venta_anticipo'


class VentaCancelada(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    fecha = models.DateField()
    usuario = models.CharField(max_length=255, blank=True, null=True)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField()
    venta = models.ForeignKey(Venta, models.DO_NOTHING)
    autorizacion = models.CharField(max_length=255)
    sw2 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'venta_cancelada'


class VentaCredito(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    operador = models.IntegerField()
    last_updated = models.DateTimeField()
    venta = models.ForeignKey(Venta, models.DO_NOTHING)
    fecha_pago = models.DateField()
    reprogramar_pago = models.DateField(blank=True, null=True)
    plazo = models.IntegerField()
    revisada = models.TextField()  # This field type is a guess.
    update_user = models.CharField(max_length=255)
    fecha_revision = models.DateField()
    fecha_revision_cxc = models.DateField()
    descuento = models.DecimalField(max_digits=19, decimal_places=2)
    socio = models.ForeignKey(Socio, models.DO_NOTHING, blank=True, null=True)
    cobrador = models.ForeignKey(Cobrador, models.DO_NOTHING)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    vencimiento = models.DateField()
    comentario_reprogramar_pago = models.CharField(max_length=255, blank=True, null=True)
    dia_revision = models.IntegerField()
    dia_pago = models.IntegerField()
    vencimiento_factura = models.TextField()  # This field type is a guess.
    sw2 = models.CharField(max_length=255)
    fecha_recepcion_cxc = models.DateField(blank=True, null=True)
    revision = models.TextField()  # This field type is a guess.
    create_user = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'venta_credito'


class VentaDet(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    total = models.DecimalField(max_digits=19, decimal_places=2)
    cantidad = models.DecimalField(max_digits=19, decimal_places=2)
    inventario = models.ForeignKey(Inventario, models.DO_NOTHING, blank=True, null=True)
    precio = models.DecimalField(max_digits=19, decimal_places=2)
    last_updated = models.DateTimeField()
    precio_original = models.DecimalField(max_digits=19, decimal_places=2)
    kilos = models.DecimalField(max_digits=19, decimal_places=2)
    venta = models.ForeignKey(Venta, models.DO_NOTHING)
    sucursal = models.ForeignKey(Sucursal, models.DO_NOTHING)
    descuento_original = models.DecimalField(max_digits=19, decimal_places=2)
    importe_cortes = models.DecimalField(max_digits=19, decimal_places=2)
    descuento_importe = models.DecimalField(max_digits=19, decimal_places=2)
    nacional = models.TextField()  # This field type is a guess.
    descuento = models.DecimalField(max_digits=19, decimal_places=2)
    con_vale = models.TextField()  # This field type is a guess.
    precio_lista = models.DecimalField(max_digits=19, decimal_places=2)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    producto = models.ForeignKey(Producto, models.DO_NOTHING)
    sw2 = models.CharField(max_length=255, blank=True, null=True)
    impuesto = models.DecimalField(max_digits=19, decimal_places=2)
    subtotal = models.DecimalField(max_digits=19, decimal_places=2)
    impuesto_tasa = models.DecimalField(max_digits=19, decimal_places=2)
    importe = models.DecimalField(max_digits=19, decimal_places=2)
    partidas_idx = models.IntegerField(blank=True, null=True)
    sin_existencia = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'venta_det'


class VentaIne(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    contabilidad = models.BigIntegerField()
    venta = models.ForeignKey(Venta, models.DO_NOTHING)
    tipo_de_proceso = models.CharField(max_length=255, blank=True, null=True)
    tipo_de_comite = models.CharField(max_length=255, blank=True, null=True)
    cfdi = models.ForeignKey(Cfdi, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'venta_ine'


class VentaParcialDet(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    valor = models.DecimalField(max_digits=19, decimal_places=2)
    instruccion_de_entrega_parcial = models.CharField(max_length=255, blank=True, null=True)
    cantidad = models.DecimalField(max_digits=19, decimal_places=2)
    venta_det = models.ForeignKey(VentaDet, models.DO_NOTHING, blank=True, null=True)
    producto = models.ForeignKey(Producto, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'venta_parcial_det'


class Zona(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    area = models.CharField(max_length=255)
    asignacion = models.CharField(max_length=255)
    cp_fin = models.CharField(max_length=255)
    cp_ini = models.CharField(max_length=255)
    division_zona = models.CharField(max_length=255, blank=True, null=True)
    entidad = models.CharField(max_length=255)
    entidad_id = models.BigIntegerField()
    sector = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'zona'


class ZonasRuteo(models.Model):
    d_codigo = models.CharField(max_length=255, blank=True, null=True)
    d_asentamiento = models.CharField(max_length=255, blank=True, null=True)
    d_tipo_asentamiento = models.CharField(max_length=255, blank=True, null=True)
    d_municipio = models.CharField(max_length=255, blank=True, null=True)
    d_estado = models.CharField(max_length=255, blank=True, null=True)
    d_ciudad = models.CharField(max_length=255, blank=True, null=True)
    d_cp = models.CharField(max_length=255, blank=True, null=True)
    c_estado = models.CharField(max_length=255, blank=True, null=True)
    c_oficina = models.CharField(max_length=255, blank=True, null=True)
    c_cp = models.CharField(max_length=255, blank=True, null=True)
    c_tipo_asentamiento = models.CharField(max_length=255, blank=True, null=True)
    c_municipoioi = models.CharField(max_length=255, blank=True, null=True)
    id_asentamiento_cp = models.CharField(max_length=255, blank=True, null=True)
    d_zona = models.CharField(max_length=255, blank=True, null=True)
    c_cuve_ciudad = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zonas_ruteo'
