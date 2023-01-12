# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AcumuladoPorConcepto(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    acumulado_excento = models.DecimalField(max_digits=19, decimal_places=2)
    acumulado_gravado = models.DecimalField(max_digits=19, decimal_places=2)
    concepto = models.ForeignKey('ConceptoDeNomina', models.DO_NOTHING)
    date_created = models.DateTimeField()
    ejercicio = models.IntegerField()
    empleado = models.ForeignKey('Empleado', models.DO_NOTHING)
    last_updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'acumulado_por_concepto'


class Aguinaldo(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    aguinaldo = models.DecimalField(max_digits=19, decimal_places=2)
    aguinaldo_excento = models.DecimalField(max_digits=19, decimal_places=2)
    aguinaldo_gravado = models.DecimalField(max_digits=19, decimal_places=2)
    beneficio_perjuicio = models.DecimalField(max_digits=19, decimal_places=2)
    bono = models.DecimalField(max_digits=19, decimal_places=2)
    bono_preliminar = models.DecimalField(max_digits=19, decimal_places=2)
    date_created = models.DateTimeField()
    dias_de_aguinaldo = models.IntegerField()
    dias_de_bono = models.IntegerField()
    dias_para_aguinaldo = models.IntegerField()
    dias_para_bono = models.IntegerField()
    dif_isr_mensual_promedio = models.DecimalField(max_digits=19, decimal_places=2)
    ejercicio = models.IntegerField()
    empleado = models.ForeignKey('Empleado', models.DO_NOTHING)
    faltas = models.IntegerField()
    fecha_final = models.DateField()
    fecha_inicial = models.DateField()
    incapacidades = models.IntegerField()
    isr_ejer_ant = models.DecimalField(max_digits=19, decimal_places=2)
    isr_mensual = models.DecimalField(max_digits=19, decimal_places=2)
    isrosubsidio = models.DecimalField(max_digits=19, decimal_places=2)
    isr_por_retener = models.DecimalField(max_digits=19, decimal_places=2)
    isr_promedio = models.DecimalField(max_digits=19, decimal_places=2)
    last_updated = models.DateTimeField()
    neto_pagado = models.DecimalField(max_digits=19, decimal_places=2)
    nomina_por_empleado = models.ForeignKey('NominaPorEmpleado', models.DO_NOTHING, blank=True, null=True)
    otras_ded = models.DecimalField(max_digits=19, decimal_places=2)
    pensiona = models.DecimalField(max_digits=19, decimal_places=2)
    permiso_especial = models.IntegerField()
    porcentaje_bono = models.DecimalField(max_digits=19, decimal_places=8)
    prestamo = models.DecimalField(max_digits=19, decimal_places=2)
    promedio_gravable = models.DecimalField(max_digits=19, decimal_places=2)
    proporcion_promedio_mensual = models.DecimalField(max_digits=19, decimal_places=2)
    resultado_isr_subsidio = models.DecimalField(max_digits=19, decimal_places=2)
    salario = models.DecimalField(max_digits=19, decimal_places=2)
    sub_total = models.DecimalField(max_digits=19, decimal_places=2)
    subsidio = models.DecimalField(max_digits=19, decimal_places=2)
    sueldo_mensual = models.DecimalField(max_digits=19, decimal_places=2)
    tabla_normal_isr_sub = models.DecimalField(max_digits=19, decimal_places=2)
    tasa = models.DecimalField(max_digits=19, decimal_places=4)
    total_gravable = models.DecimalField(max_digits=19, decimal_places=2)
    incapacidadesmat = models.IntegerField()
    incapacidadesrte = models.IntegerField()
    incapacidadesrtt = models.IntegerField()
    manual = models.TextField()  # This field type is a guess.
    bono_otras_ded = models.DecimalField(max_digits=19, decimal_places=2)
    bono_pensiona = models.DecimalField(max_digits=19, decimal_places=2)
    bono_prestamo = models.DecimalField(max_digits=19, decimal_places=2)
    nomina_por_empleado_bono = models.ForeignKey('NominaPorEmpleado', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aguinaldo'
        unique_together = (('id', 'promedio_gravable'), ('ejercicio', 'empleado'), ('ejercicio', 'empleado'),)


class Asistencia(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    asistencias = models.IntegerField()
    calendario_det = models.ForeignKey('CalendarioDet', models.DO_NOTHING, blank=True, null=True)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField()
    empleado = models.ForeignKey('Empleado', models.DO_NOTHING)
    faltas = models.IntegerField()
    incapacidades = models.IntegerField()
    incidencias = models.IntegerField()
    last_updated = models.DateTimeField()
    periodo_fecha_final = models.DateTimeField()
    periodo_fecha_inicial = models.DateTimeField()
    retardo_comida = models.IntegerField()
    retardo_mayor = models.IntegerField()
    retardo_menor = models.IntegerField()
    tipo = models.CharField(max_length=9)
    vacaciones = models.IntegerField()
    dias_trabajados = models.DecimalField(max_digits=19, decimal_places=4)
    vacacionesp = models.IntegerField()
    minutos_no_laborados = models.IntegerField()
    horas_trabajadas = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    retardo_menor_comida = models.IntegerField()
    minutos_por_descontar = models.IntegerField()
    paternidad = models.IntegerField(blank=True, null=True)
    orden = models.IntegerField()
    faltas_manuales = models.DecimalField(max_digits=19, decimal_places=2)
    checado_incompleto = models.TextField()  # This field type is a guess.
    entrada1 = models.TimeField(blank=True, null=True)
    entrada2 = models.TimeField(blank=True, null=True)
    entrada3 = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asistencia'
        unique_together = (('empleado', 'calendario_det'),)


class AsistenciaDet(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    asistencia = models.ForeignKey(Asistencia, models.DO_NOTHING)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField()
    entrada1 = models.TimeField(blank=True, null=True)
    entrada2 = models.TimeField(blank=True, null=True)
    entrada3 = models.TimeField(blank=True, null=True)
    fecha = models.DateField()
    last_updated = models.DateTimeField()
    retardo_comida = models.IntegerField()
    retardo_mayor = models.IntegerField()
    retardo_menor = models.IntegerField()
    salida1 = models.TimeField(blank=True, null=True)
    salida2 = models.TimeField(blank=True, null=True)
    salida3 = models.TimeField(blank=True, null=True)
    tipo = models.CharField(max_length=20)
    partidas_idx = models.IntegerField(blank=True, null=True)
    minutos_no_laborados = models.IntegerField()
    horas_trabajadas = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    ubicacion = models.ForeignKey('Ubicacion', models.DO_NOTHING, blank=True, null=True)
    manual = models.TextField(blank=True, null=True)  # This field type is a guess.
    turno_det = models.ForeignKey('TurnoDet', models.DO_NOTHING, blank=True, null=True)
    retardo_menor_comida = models.IntegerField()
    cancelar_incentivo = models.TextField()  # This field type is a guess.
    pagar_tiempo_extra = models.TextField()  # This field type is a guess.
    excentar_checadas = models.TextField()  # This field type is a guess.
    cierre_anual = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asistencia_det'


class AsistenciaEspecial(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    asistencias = models.IntegerField()
    calendario_det = models.ForeignKey('CalendarioDet', models.DO_NOTHING, blank=True, null=True)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField()
    dias_trabajados = models.DecimalField(max_digits=19, decimal_places=2)
    empleado = models.ForeignKey('Empleado', models.DO_NOTHING)
    faltas = models.IntegerField()
    faltas_manuales = models.DecimalField(max_digits=19, decimal_places=2)
    horas_trabajadas = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    incapacidades = models.IntegerField()
    incidencias = models.IntegerField()
    last_updated = models.DateTimeField()
    minutos_no_laborados = models.IntegerField()
    minutos_por_descontar = models.IntegerField()
    orden = models.IntegerField()
    paternidad = models.IntegerField(blank=True, null=True)
    periodo_fecha_final = models.DateTimeField()
    periodo_fecha_inicial = models.DateTimeField()
    retardo_comida = models.IntegerField()
    retardo_mayor = models.IntegerField()
    retardo_menor = models.IntegerField()
    retardo_menor_comida = models.IntegerField()
    tipo = models.CharField(max_length=9)
    vacaciones = models.IntegerField()
    vacacionesp = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'asistencia_especial'


class AsistenciaEspecialDet(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    asistencia = models.ForeignKey(AsistenciaEspecial, models.DO_NOTHING)
    cancelar_incentivo = models.TextField()  # This field type is a guess.
    cierre_anual = models.TextField()  # This field type is a guess.
    comentario = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField()
    entrada1 = models.TimeField(blank=True, null=True)
    entrada2 = models.TimeField(blank=True, null=True)
    entrada3 = models.TimeField(blank=True, null=True)
    excentar_checadas = models.TextField()  # This field type is a guess.
    fecha = models.DateField()
    horas_trabajadas = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    last_updated = models.DateTimeField()
    manual = models.TextField(blank=True, null=True)  # This field type is a guess.
    minutos_no_laborados = models.IntegerField()
    pagar_tiempo_extra = models.TextField()  # This field type is a guess.
    retardo_comida = models.IntegerField()
    retardo_mayor = models.IntegerField()
    retardo_menor = models.IntegerField()
    retardo_menor_comida = models.IntegerField()
    salida1 = models.TimeField(blank=True, null=True)
    salida2 = models.TimeField(blank=True, null=True)
    salida3 = models.TimeField(blank=True, null=True)
    tipo = models.CharField(max_length=12)
    turno_det = models.ForeignKey('TurnoDet', models.DO_NOTHING, blank=True, null=True)
    ubicacion = models.ForeignKey('Ubicacion', models.DO_NOTHING, blank=True, null=True)
    partidas_idx = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asistencia_especial_det'


class AsistenciaImss(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    asistencia = models.ForeignKey(Asistencia, models.DO_NOTHING)
    calendario_det = models.ForeignKey('CalendarioDet', models.DO_NOTHING)
    date_created = models.DateTimeField()
    empleado = models.ForeignKey('Empleado', models.DO_NOTHING)
    fin_asistencia = models.DateField()
    fin_nomina = models.DateField()
    inicio_asistencia = models.DateField()
    inicio_nomina = models.DateField()
    last_updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'asistencia_imss'


class AsistenciaImssDet(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    asistencia_imss = models.ForeignKey(AsistenciaImss, models.DO_NOTHING)
    cambio = models.DateField(blank=True, null=True)
    date_created = models.DateTimeField()
    fecha = models.DateField()
    last_updated = models.DateTimeField()
    sub_tipo = models.CharField(max_length=200, blank=True, null=True)
    tipo = models.CharField(max_length=11)
    excluir = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'asistencia_imss_det'


class AuditLog(models.Model):
    id = models.BigIntegerField(primary_key=True)
    actor = models.CharField(max_length=255, blank=True, null=True)
    class_name = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField()
    event_name = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField()
    new_value = models.CharField(max_length=255, blank=True, null=True)
    old_value = models.CharField(max_length=255, blank=True, null=True)
    persisted_object_id = models.CharField(max_length=255, blank=True, null=True)
    persisted_object_version = models.BigIntegerField(blank=True, null=True)
    property_name = models.CharField(max_length=255, blank=True, null=True)
    uri = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'audit_log'


class Autorizacion(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    autorizo = models.ForeignKey('User', models.DO_NOTHING)
    date_created = models.DateTimeField()
    descripcion = models.CharField(max_length=255)
    last_updated = models.DateTimeField()
    modulo = models.CharField(max_length=255, blank=True, null=True)
    tipo = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'autorizacion'


class BajaDeEmpleado(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    causa = models.ForeignKey('MotivoDeSeparacion', models.DO_NOTHING)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField()
    empleado = models.OneToOneField('Empleado', models.DO_NOTHING)
    fecha = models.DateTimeField()
    last_updated = models.DateTimeField()
    motivo = models.ForeignKey('MotivoDeBaja', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'baja_de_empleado'


class Bono(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    beneficio_perjuicio = models.DecimalField(max_digits=19, decimal_places=2)
    bono = models.DecimalField(max_digits=19, decimal_places=2)
    bono_inicial = models.DecimalField(max_digits=19, decimal_places=2)
    bono_preliminar = models.DecimalField(max_digits=19, decimal_places=2)
    date_created = models.DateTimeField()
    dif_isr_mensual_promedio = models.DecimalField(max_digits=19, decimal_places=2)
    ejercicio = models.IntegerField()
    empleado = models.ForeignKey('Empleado', models.DO_NOTHING)
    factor_para_bono = models.DecimalField(max_digits=19, decimal_places=2)
    faltas = models.IntegerField()
    faltas_incapacidades_factor = models.DecimalField(max_digits=19, decimal_places=2)
    fecha_final = models.DateField()
    fecha_inicial = models.DateField()
    incapacidades = models.IntegerField()
    isr_ejer_ant = models.DecimalField(max_digits=19, decimal_places=2)
    isr_mensual = models.DecimalField(max_digits=19, decimal_places=2)
    isrosubsidio = models.DecimalField(max_digits=19, decimal_places=2)
    isr_por_retener = models.DecimalField(max_digits=19, decimal_places=2)
    isr_promedio = models.DecimalField(max_digits=19, decimal_places=2)
    last_updated = models.DateTimeField()
    manual = models.TextField()  # This field type is a guess.
    monto_bono_total = models.DecimalField(max_digits=19, decimal_places=2)
    neto_pagado = models.DecimalField(max_digits=19, decimal_places=2)
    nomina_por_empleado = models.ForeignKey('NominaPorEmpleado', models.DO_NOTHING, blank=True, null=True)
    otras_ded = models.DecimalField(max_digits=19, decimal_places=2)
    pensiona = models.DecimalField(max_digits=19, decimal_places=2)
    porcentaje_bono = models.DecimalField(max_digits=19, decimal_places=2)
    prestamo = models.DecimalField(max_digits=19, decimal_places=2)
    productividad = models.TextField()  # This field type is a guess.
    productividad_factor = models.DecimalField(max_digits=19, decimal_places=2)
    promedio_gravable = models.DecimalField(max_digits=19, decimal_places=2)
    proporcion_promedio_mensual = models.DecimalField(max_digits=19, decimal_places=2)
    ptu = models.DecimalField(max_digits=19, decimal_places=2)
    resultado_isr_subsidio = models.DecimalField(max_digits=19, decimal_places=2)
    retardo_factor = models.DecimalField(max_digits=19, decimal_places=2)
    retardos = models.IntegerField()
    salario = models.DecimalField(max_digits=19, decimal_places=2)
    sub_total = models.DecimalField(max_digits=19, decimal_places=2)
    subsidio = models.DecimalField(max_digits=19, decimal_places=2)
    sueldo_mensual = models.DecimalField(max_digits=19, decimal_places=2)
    tabla_normal_isr_sub = models.DecimalField(max_digits=19, decimal_places=2)
    tasa = models.DecimalField(max_digits=19, decimal_places=4)
    tipo = models.CharField(max_length=255)
    total_gravable = models.DecimalField(max_digits=19, decimal_places=2)
    incentivo = models.DecimalField(max_digits=19, decimal_places=2)
    ptu_gravado = models.DecimalField(max_digits=19, decimal_places=2)
    por_regla = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'bono'
        unique_together = (('ejercicio', 'empleado'),)


class BrConcepto(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'br_concepto'


class BrNomina(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    activo = models.TextField()  # This field type is a guess.
    formula = models.CharField(max_length=255)
    periodicidad = models.CharField(max_length=9)
    periodo_fecha_final = models.DateTimeField()
    periodo_fecha_inicial = models.DateTimeField()
    tipo = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'br_nomina'


class BrNominaConceptoDeNomina(models.Model):
    br_nomina_conceptos = models.ForeignKey(BrNomina, models.DO_NOTHING, blank=True, null=True)
    concepto_de_nomina = models.ForeignKey('ConceptoDeNomina', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'br_nomina_concepto_de_nomina'


class CalculoAnual(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    isr = models.DecimalField(max_digits=19, decimal_places=2)
    aguinaldo_exento = models.DecimalField(max_digits=19, decimal_places=2)
    aguinaldo_gravable = models.DecimalField(max_digits=19, decimal_places=2)
    bono_de_productividad = models.DecimalField(max_digits=19, decimal_places=2)
    bono_por_desempeno = models.DecimalField(max_digits=19, decimal_places=2)
    calculo_anual = models.TextField()  # This field type is a guess.
    comisiones = models.DecimalField(max_digits=19, decimal_places=2)
    compensacion = models.DecimalField(max_digits=19, decimal_places=2)
    compensacionsaf = models.DecimalField(max_digits=19, decimal_places=2)
    date_created = models.DateTimeField()
    devispt = models.DecimalField(max_digits=19, decimal_places=2)
    devisptant = models.DecimalField(max_digits=19, decimal_places=2)
    ejercicio = models.IntegerField()
    empleado = models.ForeignKey('Empleado', models.DO_NOTHING)
    faltas = models.IntegerField()
    fecha_final = models.DateField()
    fecha_inicial = models.DateField()
    gratificacion = models.DecimalField(max_digits=19, decimal_places=2)
    impuesto_del_ejercicio = models.DecimalField(max_digits=19, decimal_places=2)
    incapacidades = models.IntegerField()
    incentivo = models.DecimalField(max_digits=19, decimal_places=2)
    indemnizacion_exenta = models.DecimalField(max_digits=19, decimal_places=2)
    indemnizacion_gravada = models.DecimalField(max_digits=19, decimal_places=2)
    ingreso_total = models.DecimalField(max_digits=19, decimal_places=2)
    last_updated = models.DateTimeField()
    nomina_por_empleado = models.ForeignKey('NominaPorEmpleado', models.DO_NOTHING, blank=True, null=True)
    permiso_especial = models.IntegerField()
    permiso_por_paternidad = models.DecimalField(max_digits=19, decimal_places=2)
    prima_de_antiguedad_exenta = models.DecimalField(max_digits=19, decimal_places=2)
    prima_de_antiguedad_gravada = models.DecimalField(max_digits=19, decimal_places=2)
    prima_dominical_exenta = models.DecimalField(max_digits=19, decimal_places=2)
    prima_dominical_gravada = models.DecimalField(max_digits=19, decimal_places=2)
    prima_vacacional_exenta = models.DecimalField(max_digits=19, decimal_places=2)
    prima_vacacional_gravada = models.DecimalField(max_digits=19, decimal_places=2)
    proyectado = models.DecimalField(max_digits=19, decimal_places=2)
    ptu_exenta = models.DecimalField(max_digits=19, decimal_places=2)
    ptu_gravada = models.DecimalField(max_digits=19, decimal_places=2)
    resultado = models.DecimalField(max_digits=19, decimal_places=2)
    retardos = models.DecimalField(max_digits=19, decimal_places=2)
    salario = models.DecimalField(max_digits=19, decimal_places=2)
    subs_emp_aplicado = models.DecimalField(max_digits=19, decimal_places=2)
    subs_emp_pagado = models.DecimalField(max_digits=19, decimal_places=2)
    sueldo = models.DecimalField(max_digits=19, decimal_places=2)
    tiempo_extra_doble_exento = models.DecimalField(max_digits=19, decimal_places=2)
    tiempo_extra_doble_gravado = models.DecimalField(max_digits=19, decimal_places=2)
    tiempo_extra_triple_gravado = models.DecimalField(max_digits=19, decimal_places=2)
    total = models.DecimalField(max_digits=19, decimal_places=2)
    total_exento = models.DecimalField(max_digits=19, decimal_places=2)
    total_gravado = models.DecimalField(max_digits=19, decimal_places=2)
    vacaciones = models.DecimalField(max_digits=19, decimal_places=2)
    vacaciones_pagadas = models.DecimalField(max_digits=19, decimal_places=2)
    aplicado = models.DecimalField(max_digits=19, decimal_places=2)
    bono = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    bono_antiguedad = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    bono_puntualidad_asist = models.DecimalField(max_digits=19, decimal_places=2)
    dia_descanso = models.DecimalField(max_digits=19, decimal_places=2)
    premio_puntualidad = models.DecimalField(max_digits=19, decimal_places=2)
    honorarios_al_consejo = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'calculo_anual'
        unique_together = (('ejercicio', 'empleado'), ('ejercicio', 'empleado'),)


class CalculoAnualBack20141230(models.Model):
    id = models.BigIntegerField()
    version = models.BigIntegerField()
    isr = models.DecimalField(max_digits=19, decimal_places=2)
    aguinaldo_exento = models.DecimalField(max_digits=19, decimal_places=2)
    aguinaldo_gravable = models.DecimalField(max_digits=19, decimal_places=2)
    bono_de_productividad = models.DecimalField(max_digits=19, decimal_places=2)
    bono_por_desempeno = models.DecimalField(max_digits=19, decimal_places=2)
    calculo_anual = models.TextField()  # This field type is a guess.
    comisiones = models.DecimalField(max_digits=19, decimal_places=2)
    compensacion = models.DecimalField(max_digits=19, decimal_places=2)
    compensacionsaf = models.DecimalField(max_digits=19, decimal_places=2)
    date_created = models.DateTimeField()
    devispt = models.DecimalField(max_digits=19, decimal_places=2)
    devisptant = models.DecimalField(max_digits=19, decimal_places=2)
    ejercicio = models.IntegerField()
    empleado_id = models.BigIntegerField()
    faltas = models.IntegerField()
    fecha_final = models.DateField()
    fecha_inicial = models.DateField()
    gratificacion = models.DecimalField(max_digits=19, decimal_places=2)
    impuesto_del_ejercicio = models.DecimalField(max_digits=19, decimal_places=2)
    incapacidades = models.IntegerField()
    incentivo = models.DecimalField(max_digits=19, decimal_places=2)
    indemnizacion_exenta = models.DecimalField(max_digits=19, decimal_places=2)
    indemnizacion_gravada = models.DecimalField(max_digits=19, decimal_places=2)
    ingreso_total = models.DecimalField(max_digits=19, decimal_places=2)
    last_updated = models.DateTimeField()
    nomina_por_empleado_id = models.BigIntegerField(blank=True, null=True)
    permiso_especial = models.IntegerField()
    permiso_por_paternidad = models.DecimalField(max_digits=19, decimal_places=2)
    prima_de_antiguedad_exenta = models.DecimalField(max_digits=19, decimal_places=2)
    prima_de_antiguedad_gravada = models.DecimalField(max_digits=19, decimal_places=2)
    prima_dominical_exenta = models.DecimalField(max_digits=19, decimal_places=2)
    prima_dominical_gravada = models.DecimalField(max_digits=19, decimal_places=2)
    prima_vacacional_exenta = models.DecimalField(max_digits=19, decimal_places=2)
    prima_vacacional_gravada = models.DecimalField(max_digits=19, decimal_places=2)
    proyectado = models.DecimalField(max_digits=19, decimal_places=2)
    ptu_exenta = models.DecimalField(max_digits=19, decimal_places=2)
    ptu_gravada = models.DecimalField(max_digits=19, decimal_places=2)
    resultado = models.DecimalField(max_digits=19, decimal_places=2)
    retardos = models.DecimalField(max_digits=19, decimal_places=2)
    salario = models.DecimalField(max_digits=19, decimal_places=2)
    subs_emp_aplicado = models.DecimalField(max_digits=19, decimal_places=2)
    subs_emp_pagado = models.DecimalField(max_digits=19, decimal_places=2)
    sueldo = models.DecimalField(max_digits=19, decimal_places=2)
    tiempo_extra_doble_exento = models.DecimalField(max_digits=19, decimal_places=2)
    tiempo_extra_doble_gravado = models.DecimalField(max_digits=19, decimal_places=2)
    tiempo_extra_triple_gravado = models.DecimalField(max_digits=19, decimal_places=2)
    total = models.DecimalField(max_digits=19, decimal_places=2)
    total_exento = models.DecimalField(max_digits=19, decimal_places=2)
    total_gravado = models.DecimalField(max_digits=19, decimal_places=2)
    vacaciones = models.IntegerField()
    vacaciones_pagadas = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'calculo_anual_back20141230'


class CalculoAnualRes20160210(models.Model):
    id = models.BigIntegerField()
    version = models.BigIntegerField()
    isr = models.DecimalField(max_digits=19, decimal_places=2)
    aguinaldo_exento = models.DecimalField(max_digits=19, decimal_places=2)
    aguinaldo_gravable = models.DecimalField(max_digits=19, decimal_places=2)
    bono_de_productividad = models.DecimalField(max_digits=19, decimal_places=2)
    bono_por_desempeno = models.DecimalField(max_digits=19, decimal_places=2)
    calculo_anual = models.TextField()  # This field type is a guess.
    comisiones = models.DecimalField(max_digits=19, decimal_places=2)
    compensacion = models.DecimalField(max_digits=19, decimal_places=2)
    compensacionsaf = models.DecimalField(max_digits=19, decimal_places=2)
    date_created = models.DateTimeField()
    devispt = models.DecimalField(max_digits=19, decimal_places=2)
    devisptant = models.DecimalField(max_digits=19, decimal_places=2)
    ejercicio = models.IntegerField()
    empleado_id = models.BigIntegerField()
    faltas = models.IntegerField()
    fecha_final = models.DateField()
    fecha_inicial = models.DateField()
    gratificacion = models.DecimalField(max_digits=19, decimal_places=2)
    impuesto_del_ejercicio = models.DecimalField(max_digits=19, decimal_places=2)
    incapacidades = models.IntegerField()
    incentivo = models.DecimalField(max_digits=19, decimal_places=2)
    indemnizacion_exenta = models.DecimalField(max_digits=19, decimal_places=2)
    indemnizacion_gravada = models.DecimalField(max_digits=19, decimal_places=2)
    ingreso_total = models.DecimalField(max_digits=19, decimal_places=2)
    last_updated = models.DateTimeField()
    nomina_por_empleado_id = models.BigIntegerField(blank=True, null=True)
    permiso_especial = models.IntegerField()
    permiso_por_paternidad = models.DecimalField(max_digits=19, decimal_places=2)
    prima_de_antiguedad_exenta = models.DecimalField(max_digits=19, decimal_places=2)
    prima_de_antiguedad_gravada = models.DecimalField(max_digits=19, decimal_places=2)
    prima_dominical_exenta = models.DecimalField(max_digits=19, decimal_places=2)
    prima_dominical_gravada = models.DecimalField(max_digits=19, decimal_places=2)
    prima_vacacional_exenta = models.DecimalField(max_digits=19, decimal_places=2)
    prima_vacacional_gravada = models.DecimalField(max_digits=19, decimal_places=2)
    proyectado = models.DecimalField(max_digits=19, decimal_places=2)
    ptu_exenta = models.DecimalField(max_digits=19, decimal_places=2)
    ptu_gravada = models.DecimalField(max_digits=19, decimal_places=2)
    resultado = models.DecimalField(max_digits=19, decimal_places=2)
    retardos = models.DecimalField(max_digits=19, decimal_places=2)
    salario = models.DecimalField(max_digits=19, decimal_places=2)
    subs_emp_aplicado = models.DecimalField(max_digits=19, decimal_places=2)
    subs_emp_pagado = models.DecimalField(max_digits=19, decimal_places=2)
    sueldo = models.DecimalField(max_digits=19, decimal_places=2)
    tiempo_extra_doble_exento = models.DecimalField(max_digits=19, decimal_places=2)
    tiempo_extra_doble_gravado = models.DecimalField(max_digits=19, decimal_places=2)
    tiempo_extra_triple_gravado = models.DecimalField(max_digits=19, decimal_places=2)
    total = models.DecimalField(max_digits=19, decimal_places=2)
    total_exento = models.DecimalField(max_digits=19, decimal_places=2)
    total_gravado = models.DecimalField(max_digits=19, decimal_places=2)
    vacaciones = models.IntegerField()
    vacaciones_pagadas = models.DecimalField(max_digits=19, decimal_places=2)
    aplicado = models.DecimalField(max_digits=19, decimal_places=2)
    bono = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    bono_antiguedad = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calculo_anual_res_20160210'


class CalculoSdi(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    agndo_dias = models.IntegerField()
    bimestre = models.IntegerField()
    bono_por_desemp = models.DecimalField(max_digits=19, decimal_places=2)
    comisiones = models.DecimalField(max_digits=19, decimal_places=2)
    compensacion = models.DecimalField(max_digits=19, decimal_places=2)
    dias = models.DecimalField(max_digits=19, decimal_places=2)
    dias_bim = models.DecimalField(max_digits=19, decimal_places=2)
    dias_lab_bim = models.DecimalField(max_digits=19, decimal_places=2)
    ejercicio = models.IntegerField()
    empleado = models.ForeignKey('Empleado', models.DO_NOTHING)
    factor = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    faltas = models.DecimalField(max_digits=19, decimal_places=2)
    fecha_fin = models.DateField()
    fecha_ini = models.DateField()
    hrs_extras_dobles = models.DecimalField(max_digits=19, decimal_places=2)
    hrs_extras_triples = models.DecimalField(max_digits=19, decimal_places=2)
    incapacidades = models.DecimalField(max_digits=19, decimal_places=2)
    incentivo = models.DecimalField(max_digits=19, decimal_places=2)
    prima_dom = models.DecimalField(max_digits=19, decimal_places=2)
    sdb = models.DecimalField(max_digits=19, decimal_places=2)
    sdi_anterior = models.DecimalField(max_digits=19, decimal_places=2)
    sdi_calc = models.DecimalField(max_digits=19, decimal_places=2)
    sdif = models.DecimalField(max_digits=19, decimal_places=2)
    sdi_inf = models.DecimalField(max_digits=19, decimal_places=2)
    sdi_nvo = models.DecimalField(max_digits=19, decimal_places=2)
    smg = models.DecimalField(max_digits=19, decimal_places=2)
    status = models.CharField(max_length=8)
    tipo = models.CharField(max_length=11)
    tope_smg = models.DecimalField(max_digits=19, decimal_places=2)
    vac_dias = models.IntegerField()
    vac_prima = models.DecimalField(max_digits=19, decimal_places=2)
    vacacionesp = models.DecimalField(max_digits=19, decimal_places=2)
    var_dia = models.DecimalField(max_digits=19, decimal_places=2)
    variable = models.DecimalField(max_digits=19, decimal_places=2)
    years = models.DecimalField(max_digits=19, decimal_places=2)
    sdb_anterior = models.DecimalField(max_digits=19, decimal_places=2)
    bono = models.DecimalField(max_digits=19, decimal_places=2)
    bono_por_antiguedad = models.DecimalField(max_digits=19, decimal_places=2)
    dias_prima_dominical = models.DecimalField(max_digits=19, decimal_places=2)
    dia_descanso = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'calculo_sdi'


class Calendario(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    comentario = models.CharField(max_length=200, blank=True, null=True)
    date_created = models.DateTimeField()
    ejercicio = models.IntegerField()
    last_updated = models.DateTimeField()
    tipo = models.CharField(max_length=9)

    class Meta:
        managed = False
        db_table = 'calendario'


class CalendarioDeNominas(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    comentario = models.CharField(max_length=255)
    corte = models.DateTimeField()
    folio = models.IntegerField()
    pago = models.DateTimeField()
    periodo_fecha_final = models.DateTimeField()
    periodo_fecha_inicial = models.DateTimeField()
    status = models.CharField(max_length=8)
    tipo_de_nomina = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'calendario_de_nominas'


class CalendarioDet(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    asistencia_fecha_final = models.DateTimeField(blank=True, null=True)
    asistencia_fecha_inicial = models.DateTimeField(blank=True, null=True)
    calendario = models.ForeignKey(Calendario, models.DO_NOTHING)
    fecha_de_pago = models.DateTimeField(blank=True, null=True)
    fin = models.DateField()
    folio = models.IntegerField()
    inicio = models.DateField()
    periodos_idx = models.IntegerField(blank=True, null=True)
    bimestre = models.IntegerField(blank=True, null=True)
    mes = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calendario_det'


class CancelacionDeCfdi(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    cfdi = models.ForeignKey('Cfdi', models.DO_NOTHING)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField()
    last_updated = models.DateTimeField()
    ack = models.TextField()
    cancel_status = models.CharField(max_length=255, blank=True, null=True)
    create_user = models.CharField(max_length=255, blank=True, null=True)
    is_cancelable = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255)
    status_code = models.CharField(max_length=200, blank=True, null=True)
    update_user = models.CharField(max_length=255, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'cancelacion_de_cfdi'


class Cfdi(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    emisor = models.CharField(max_length=600)
    fecha = models.DateTimeField()
    folio = models.CharField(max_length=20)
    last_updated = models.DateTimeField()
    receptor = models.CharField(max_length=600)
    receptor_rfc = models.CharField(max_length=13)
    serie = models.CharField(max_length=15)
    timbrado = models.DateTimeField(blank=True, null=True)
    total = models.DecimalField(max_digits=19, decimal_places=2)
    uuid = models.CharField(max_length=300, blank=True, null=True)
    xml = models.TextField()
    xml_name = models.CharField(max_length=200, blank=True, null=True)
    version_cfdi = models.CharField(max_length=255, blank=True, null=True)
    cancelado = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cfdi'


class CfdiCancelar(models.Model):
    id = models.BigIntegerField()
    fecha = models.DateTimeField()
    timbrado = models.DateTimeField(blank=True, null=True)
    uuid = models.CharField(max_length=300, blank=True, null=True)
    receptor = models.CharField(max_length=600)
    receptor_rfc = models.CharField(max_length=13)
    total = models.DecimalField(max_digits=19, decimal_places=2)
    status = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cfdi_cancelar'


class Checado(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    fecha = models.DateField()
    hora = models.TimeField()
    last_updated = models.DateTimeField()
    lector = models.IntegerField()
    numero_de_empleado = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'checado'


class Compensacion(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    comentario = models.CharField(max_length=255, blank=True, null=True)
    concepto = models.ForeignKey('ConceptoDeNomina', models.DO_NOTHING)
    date_created = models.DateTimeField()
    empleado = models.ForeignKey('Empleado', models.DO_NOTHING)
    fecha = models.DateTimeField()
    importe = models.DecimalField(max_digits=19, decimal_places=2)
    last_updated = models.DateTimeField()
    nomina_por_empleado = models.ForeignKey('NominaPorEmpleado', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'compensacion'


class ConceptoDeNomina(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    clase = models.CharField(max_length=30)
    clave = models.CharField(unique=True, max_length=15)
    clave_sat = models.IntegerField()
    date_created = models.DateTimeField()
    descripcion = models.CharField(max_length=100)
    general = models.TextField()  # This field type is a guess.
    last_updated = models.DateTimeField()
    tipo = models.CharField(max_length=10)
    importe_excento = models.TextField(blank=True, null=True)  # This field type is a guess.
    catalogo_sat = models.CharField(max_length=30, blank=True, null=True)
    catalogo_sat_clave = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'concepto_de_nomina'


class ControlDeVacaciones(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    acumulado_excento = models.DecimalField(max_digits=19, decimal_places=2)
    acumulado_gravado = models.DecimalField(max_digits=19, decimal_places=2)
    aniversario = models.DateField()
    antiguedad_dias = models.IntegerField()
    antiguedad_years = models.IntegerField()
    date_created = models.DateTimeField()
    dias_tomados = models.IntegerField()
    dias_trasladados = models.IntegerField()
    dias_vacaciones = models.IntegerField()
    ejercicio = models.BigIntegerField()
    empleado = models.ForeignKey('Empleado', models.DO_NOTHING)
    last_updated = models.DateTimeField()
    dias_pagados = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'control_de_vacaciones'
        unique_together = (('ejercicio', 'empleado'), ('ejercicio', 'empleado'),)


class DatosPersonales(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    conyuge = models.CharField(max_length=255, blank=True, null=True)
    direccion_calle = models.CharField(max_length=200)
    direccion_codigo_postal = models.CharField(max_length=255)
    direccion_colonia = models.CharField(max_length=255, blank=True, null=True)
    direccion_estado = models.CharField(max_length=255)
    direccion_municipio = models.CharField(max_length=255, blank=True, null=True)
    direccion_numero_exterior = models.CharField(max_length=50, blank=True, null=True)
    direccion_numero_interior = models.CharField(max_length=50, blank=True, null=True)
    direccion_pais = models.CharField(max_length=100)
    email = models.CharField(max_length=255, blank=True, null=True)
    empleado = models.OneToOneField('Empleado', models.DO_NOTHING)
    estado_civil = models.CharField(max_length=11)
    lugar_de_nacimiento = models.CharField(max_length=255, blank=True, null=True)
    nombre_de_la_madre = models.CharField(max_length=255, blank=True, null=True)
    nombre_del_pader = models.CharField(max_length=255, blank=True, null=True)
    telefono1 = models.CharField(max_length=255, blank=True, null=True)
    telefono2 = models.CharField(max_length=255, blank=True, null=True)
    tipo_de_sangre = models.CharField(max_length=255, blank=True, null=True)
    domicilio_fiscal = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'datos_personales'


class Departamento(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    clave = models.CharField(unique=True, max_length=20)
    descripcion = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'departamento'


class DiaFestivo(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    descripcion = models.CharField(max_length=255)
    ejercicio = models.IntegerField()
    fecha = models.DateField()
    parcial = models.TextField()  # This field type is a guess.
    salida = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dia_festivo'


class Empleado(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    alta = models.DateTimeField()
    apellido_materno = models.CharField(max_length=150, blank=True, null=True)
    apellido_paterno = models.CharField(max_length=150, blank=True, null=True)
    clave = models.CharField(max_length=255, blank=True, null=True)
    curp = models.CharField(unique=True, max_length=25)
    date_created = models.DateTimeField()
    fecha_de_nacimiento = models.DateTimeField()
    last_updated = models.DateTimeField()
    nombres = models.CharField(max_length=300)
    rfc = models.CharField(max_length=13)
    sexo = models.CharField(max_length=1)
    status = models.CharField(max_length=9)
    activo = models.TextField(blank=True, null=True)  # This field type is a guess.
    control_de_asistencia = models.TextField(blank=True, null=True)  # This field type is a guess.
    asimilado = models.TextField()  # This field type is a guess.
    contratado = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'empleado'


class EmpleadoContacto(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    comentario = models.CharField(max_length=255, blank=True, null=True)
    direccion_calle = models.CharField(max_length=200, blank=True, null=True)
    direccion_codigo_postal = models.CharField(max_length=255, blank=True, null=True)
    direccion_colonia = models.CharField(max_length=255, blank=True, null=True)
    direccion_estado = models.CharField(max_length=255, blank=True, null=True)
    direccion_municipio = models.CharField(max_length=255, blank=True, null=True)
    direccion_numero_exterior = models.CharField(max_length=50, blank=True, null=True)
    direccion_numero_interior = models.CharField(max_length=50, blank=True, null=True)
    direccion_pais = models.CharField(max_length=100, blank=True, null=True)
    empleado = models.OneToOneField(Empleado, models.DO_NOTHING)
    nombre = models.CharField(max_length=255)
    parentesco = models.CharField(max_length=8)
    telefono1 = models.CharField(max_length=255, blank=True, null=True)
    telefono2 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleado_contacto'


class EmpleadosPorConcepto(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    concepto = models.ForeignKey(ConceptoDeNomina, models.DO_NOTHING)
    date_created = models.DateTimeField()
    last_updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'empleados_por_concepto'


class EmpleadosPorConceptoEmpleado(models.Model):
    empleados_por_concepto_empleados = models.ForeignKey(EmpleadosPorConcepto, models.DO_NOTHING, blank=True, null=True)
    empleado = models.ForeignKey(Empleado, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empleados_por_concepto_empleado'


class Empresa(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    certificado_digital = models.TextField(blank=True, null=True)
    certificado_digital_pfx = models.TextField(blank=True, null=True)
    clave = models.CharField(unique=True, max_length=15)
    date_created = models.DateTimeField()
    direccion_calle = models.CharField(max_length=200)
    direccion_codigo_postal = models.CharField(max_length=255)
    direccion_colonia = models.CharField(max_length=255, blank=True, null=True)
    direccion_estado = models.CharField(max_length=255)
    direccion_municipio = models.CharField(max_length=255, blank=True, null=True)
    direccion_numero_exterior = models.CharField(max_length=50, blank=True, null=True)
    direccion_numero_interior = models.CharField(max_length=50, blank=True, null=True)
    direccion_pais = models.CharField(max_length=100)
    last_updated = models.DateTimeField()
    llave_privada = models.TextField(blank=True, null=True)
    nombre = models.CharField(unique=True, max_length=255)
    numero_de_certificado = models.CharField(max_length=20, blank=True, null=True)
    password_pfx = models.CharField(max_length=255, blank=True, null=True)
    regimen = models.CharField(max_length=300)
    registro_patronal = models.CharField(max_length=20)
    rfc = models.CharField(max_length=13)
    regimen_fiscal = models.CharField(max_length=30, blank=True, null=True)
    razon_social = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empresa'


class FactorDeIntegracion(models.Model):
    id = models.BigIntegerField()
    version = models.BigIntegerField()
    cob_dias = models.IntegerField()
    cob_factor = models.DecimalField(max_digits=19, decimal_places=4)
    date_created = models.DateTimeField()
    dias_de = models.IntegerField()
    dias_hasta = models.IntegerField()
    last_updated = models.DateTimeField()
    qna_dias = models.IntegerField()
    qna_factor = models.DecimalField(max_digits=19, decimal_places=4)
    sem_dias = models.IntegerField()
    sem_factor = models.DecimalField(max_digits=19, decimal_places=4)
    tipo = models.IntegerField()
    vac_dias = models.IntegerField()
    vac_prima = models.DecimalField(max_digits=19, decimal_places=2)
    year_de = models.IntegerField()
    year_hasta = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'factor_de_integracion'


class FactorDeIntegracion365(models.Model):
    id = models.BigIntegerField()
    version = models.BigIntegerField()
    cob_dias = models.IntegerField()
    cob_factor = models.DecimalField(max_digits=19, decimal_places=4)
    date_created = models.DateTimeField()
    dias_de = models.IntegerField()
    dias_hasta = models.IntegerField()
    last_updated = models.DateTimeField()
    qna_dias = models.IntegerField()
    qna_factor = models.DecimalField(max_digits=19, decimal_places=4)
    sem_dias = models.IntegerField()
    sem_factor = models.DecimalField(max_digits=19, decimal_places=4)
    tipo = models.IntegerField()
    vac_dias = models.IntegerField()
    vac_prima = models.DecimalField(max_digits=19, decimal_places=2)
    year_de = models.IntegerField()
    year_hasta = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'factor_de_integracion_365'


class FactorDeIntegracion366(models.Model):
    id = models.BigIntegerField()
    version = models.BigIntegerField()
    cob_dias = models.IntegerField()
    cob_factor = models.DecimalField(max_digits=19, decimal_places=4)
    date_created = models.DateTimeField()
    dias_de = models.IntegerField()
    dias_hasta = models.IntegerField()
    last_updated = models.DateTimeField()
    qna_dias = models.IntegerField()
    qna_factor = models.DecimalField(max_digits=19, decimal_places=4)
    sem_dias = models.IntegerField()
    sem_factor = models.DecimalField(max_digits=19, decimal_places=4)
    tipo = models.IntegerField()
    vac_dias = models.IntegerField()
    vac_prima = models.DecimalField(max_digits=19, decimal_places=2)
    year_de = models.IntegerField()
    year_hasta = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'factor_de_integracion_366'


class Finiquito(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    aguinaldo_exento = models.DecimalField(max_digits=19, decimal_places=2)
    aguinaldo_gravable = models.DecimalField(max_digits=19, decimal_places=2)
    alta = models.DateTimeField()
    anos_trabajados = models.IntegerField(blank=True, null=True)
    anticipo_de_nomina = models.DecimalField(max_digits=19, decimal_places=2)
    antiguedad = models.IntegerField()
    baja = models.ForeignKey(BajaDeEmpleado, models.DO_NOTHING)
    bono_de_productividad = models.DecimalField(max_digits=19, decimal_places=2)
    comisiones = models.DecimalField(max_digits=19, decimal_places=2)
    compensacion = models.DecimalField(max_digits=19, decimal_places=2)
    compensacionsaf = models.DecimalField(max_digits=19, decimal_places=2)
    date_created = models.DateTimeField()
    deduccion_total = models.DecimalField(max_digits=19, decimal_places=2)
    dias_aguinaldo = models.IntegerField()
    dias_del_ejercicio = models.IntegerField(blank=True, null=True)
    dias_para_aguinaldo = models.IntegerField()
    dias_por_pagar = models.IntegerField()
    dias_trabajado_ejercicio = models.IntegerField()
    dias_trabajado_para_vacaciones = models.IntegerField()
    empleado = models.OneToOneField(Empleado, models.DO_NOTHING)
    factor_liquidacion = models.DecimalField(max_digits=19, decimal_places=4)
    fonacot = models.DecimalField(max_digits=19, decimal_places=2)
    imss = models.DecimalField(max_digits=19, decimal_places=2)
    incentivo = models.DecimalField(max_digits=19, decimal_places=2)
    indemnizacion20dias_por_anio = models.DecimalField(max_digits=19, decimal_places=2)
    indemnizacion3meses_de_sueldo = models.DecimalField(max_digits=19, decimal_places=2)
    indemnizacion_exenta = models.DecimalField(max_digits=19, decimal_places=2)
    indemnizacion_gravada = models.DecimalField(max_digits=19, decimal_places=2)
    indemnizacion_intereses = models.DecimalField(max_digits=19, decimal_places=2)
    indemnizacion_prima_de_antiguedad = models.DecimalField(max_digits=19, decimal_places=2)
    infonavit = models.DecimalField(max_digits=19, decimal_places=2)
    isr = models.DecimalField(max_digits=19, decimal_places=2)
    isr_acumulado_del_mes = models.DecimalField(max_digits=19, decimal_places=2)
    last_updated = models.DateTimeField()
    liq = models.TextField()  # This field type is a guess.
    monto_intereses = models.DecimalField(max_digits=19, decimal_places=2)
    ne_finiquito = models.ForeignKey('NominaPorEmpleado', models.DO_NOTHING, blank=True, null=True)
    ne_liquidacion = models.ForeignKey('NominaPorEmpleado', models.DO_NOTHING, blank=True, null=True)
    otras_deducciones = models.DecimalField(max_digits=19, decimal_places=2)
    pension_alimenticia = models.DecimalField(max_digits=19, decimal_places=2)
    percepcion_total = models.DecimalField(max_digits=19, decimal_places=2)
    permiso_por_paternidad = models.DecimalField(max_digits=19, decimal_places=2)
    prestamo = models.DecimalField(max_digits=19, decimal_places=2)
    prima_de_antiguedad_exenta = models.DecimalField(max_digits=19, decimal_places=2)
    prima_de_antiguedad_gravada = models.DecimalField(max_digits=19, decimal_places=2)
    prima_dominical_exenta = models.DecimalField(max_digits=19, decimal_places=2)
    prima_dominical_gravada = models.DecimalField(max_digits=19, decimal_places=2)
    prima_vacacional = models.DecimalField(max_digits=19, decimal_places=2)
    prima_vacacional_exenta = models.DecimalField(max_digits=19, decimal_places=2)
    prima_vacacional_gravada = models.DecimalField(max_digits=19, decimal_places=2)
    retardos = models.DecimalField(max_digits=19, decimal_places=2)
    salario = models.DecimalField(max_digits=19, decimal_places=2)
    salario_diario_integrado = models.DecimalField(max_digits=19, decimal_places=2)
    salario_diario_integrado_liq = models.DecimalField(max_digits=19, decimal_places=2)
    salario_variable = models.DecimalField(max_digits=19, decimal_places=2)
    sdi_opcion = models.TextField()  # This field type is a guess.
    smg = models.DecimalField(max_digits=19, decimal_places=2)
    subs_emp_aplicado = models.DecimalField(max_digits=19, decimal_places=2)
    subs_emp_pagado = models.DecimalField(max_digits=19, decimal_places=2)
    subsidio_acumulado_mes = models.DecimalField(max_digits=19, decimal_places=2)
    sueldo = models.DecimalField(max_digits=19, decimal_places=2)
    tasa_interes = models.DecimalField(max_digits=19, decimal_places=2)
    total = models.DecimalField(max_digits=19, decimal_places=2)
    total_exento = models.DecimalField(max_digits=19, decimal_places=2)
    total_gravado = models.DecimalField(max_digits=19, decimal_places=2)
    vacaciones = models.DecimalField(max_digits=19, decimal_places=2)
    vacaciones_anteriores = models.IntegerField()
    vacaciones_aplicadas = models.IntegerField()
    vacaciones_ejercicio = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'finiquito'


class FiniquitoDet(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    concepto = models.ForeignKey(ConceptoDeNomina, models.DO_NOTHING)
    finiquito = models.ForeignKey(Finiquito, models.DO_NOTHING)
    importe_excento = models.DecimalField(max_digits=19, decimal_places=2)
    importe_gravado = models.DecimalField(max_digits=19, decimal_places=2)
    liquidacion = models.TextField()  # This field type is a guess.
    manual = models.TextField()  # This field type is a guess.
    tipo = models.CharField(max_length=10)
    partidas_idx = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'finiquito_det'


class Folio(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    empresa = models.ForeignKey(Empresa, models.DO_NOTHING)
    folio = models.BigIntegerField()
    serie = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'folio'


class FolioDeNomina(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'folio_de_nomina'


class Fonacot(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    activo = models.TextField()  # This field type is a guess.
    date_created = models.DateTimeField()
    empleado = models.ForeignKey(Empleado, models.DO_NOTHING)
    importe = models.DecimalField(max_digits=19, decimal_places=2)
    last_updated = models.DateTimeField()
    numero_de_credito = models.CharField(max_length=255)
    numero_de_fonacot = models.CharField(max_length=255)
    retencion_diaria = models.DecimalField(max_digits=19, decimal_places=2)
    retencion_mensual = models.DecimalField(max_digits=19, decimal_places=2)
    saldo = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'fonacot'


class FonacotAbono(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    comentario = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField()
    fecha = models.DateTimeField()
    importe = models.DecimalField(max_digits=19, decimal_places=2)
    last_updated = models.DateTimeField()
    nomina_por_empleado_det = models.ForeignKey('NominaPorEmpleadoDet', models.DO_NOTHING, blank=True, null=True)
    prestamo = models.ForeignKey(Fonacot, models.DO_NOTHING)
    abonos_idx = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fonacot_abono'


class Incapacidad(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    comentario = models.CharField(max_length=250, blank=True, null=True)
    date_created = models.DateTimeField()
    empleado = models.ForeignKey(Empleado, models.DO_NOTHING)
    fecha_final = models.DateField()
    fecha_inicial = models.DateField()
    last_updated = models.DateTimeField()
    referencia_imms = models.CharField(max_length=255)
    tipo = models.ForeignKey('SatIncapacidad', models.DO_NOTHING)
    control = models.CharField(max_length=11, blank=True, null=True)
    porcentaje = models.IntegerField(blank=True, null=True)
    secuela = models.CharField(max_length=29, blank=True, null=True)
    tipo_riesgo = models.CharField(max_length=22, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'incapacidad'


class Incentivo(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    asistencia = models.ForeignKey(Asistencia, models.DO_NOTHING, blank=True, null=True)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField()
    ejercicio = models.IntegerField()
    empleado = models.ForeignKey(Empleado, models.DO_NOTHING)
    fecha_final = models.DateField(blank=True, null=True)
    fecha_inicial = models.DateField(blank=True, null=True)
    incentivo = models.DecimalField(max_digits=19, decimal_places=2)
    ingreso_base = models.DecimalField(max_digits=19, decimal_places=2)
    last_updated = models.DateTimeField()
    mes = models.CharField(max_length=255, blank=True, null=True)
    nomina_por_empleado_det = models.ForeignKey('NominaPorEmpleadoDet', models.DO_NOTHING, blank=True, null=True)
    otorgado = models.TextField()  # This field type is a guess.
    status = models.CharField(max_length=9)
    tasa_bono1 = models.DecimalField(max_digits=19, decimal_places=6)
    tasa_bono2 = models.DecimalField(max_digits=19, decimal_places=6)
    tipo = models.CharField(max_length=9)
    calificacion = models.CharField(max_length=7)
    checadas_faltantes = models.IntegerField()
    faltas = models.IntegerField()
    minutos_no_laborados = models.IntegerField()
    manual = models.TextField(blank=True, null=True)  # This field type is a guess.
    importe_incentivo = models.DecimalField(max_digits=19, decimal_places=2)
    incentivo_inv = models.DecimalField(max_digits=19, decimal_places=6)

    class Meta:
        managed = False
        db_table = 'incentivo'


class Incidencia(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    autorizacion = models.ForeignKey(Autorizacion, models.DO_NOTHING, blank=True, null=True)
    comentario = models.CharField(max_length=250, blank=True, null=True)
    date_created = models.DateTimeField()
    empleado = models.ForeignKey(Empleado, models.DO_NOTHING)
    fecha_final = models.DateField()
    fecha_inicial = models.DateField()
    last_updated = models.DateTimeField()
    pagado = models.TextField()  # This field type is a guess.
    tipo = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'incidencia'


class Infonavit(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    activo = models.TextField()  # This field type is a guess.
    alta = models.DateField()
    comentario = models.CharField(max_length=255)
    cuota_fija = models.DecimalField(max_digits=14, decimal_places=6)
    date_created = models.DateTimeField()
    empleado = models.ForeignKey(Empleado, models.DO_NOTHING)
    last_updated = models.DateTimeField()
    numero_de_credito = models.CharField(max_length=255)
    tipo = models.CharField(max_length=10)
    bimestre_actual = models.IntegerField()
    cuota_diaria = models.DecimalField(max_digits=19, decimal_places=2)
    ultima_diferencia = models.DecimalField(max_digits=19, decimal_places=2)
    dias_del_bimestre = models.IntegerField()
    importe_bimestral = models.DecimalField(max_digits=19, decimal_places=2)
    salario_diario_integrado = models.DecimalField(max_digits=19, decimal_places=2)
    salario_minimo_general = models.DecimalField(max_digits=19, decimal_places=2)
    seguro_de_vivienda = models.DecimalField(max_digits=19, decimal_places=2)
    modificacion_numero = models.DateField(blank=True, null=True)
    modificacion_tipo = models.DateField(blank=True, null=True)
    modificacion_valor = models.DateField(blank=True, null=True)
    reinicio = models.DateField(blank=True, null=True)
    suspension = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'infonavit'


class InfonavitDet(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    acumulado = models.DecimalField(max_digits=19, decimal_places=2)
    bimestre = models.IntegerField()
    cuota = models.DecimalField(max_digits=19, decimal_places=6)
    cuota_bimestral = models.DecimalField(max_digits=19, decimal_places=2)
    cuota_diaria = models.DecimalField(max_digits=19, decimal_places=2)
    date_created = models.DateTimeField()
    dias_del_bimestre = models.IntegerField()
    ejercicio = models.IntegerField()
    faltas = models.IntegerField()
    fecha_final = models.DateField()
    fecha_inicial = models.DateField()
    importe_bimestral = models.DecimalField(max_digits=19, decimal_places=2)
    incapacidades = models.IntegerField()
    infonavit = models.ForeignKey(Infonavit, models.DO_NOTHING)
    last_updated = models.DateTimeField()
    salario_diario_integrado = models.DecimalField(max_digits=19, decimal_places=2)
    salario_minimo_general = models.DecimalField(max_digits=19, decimal_places=2)
    saldo = models.DecimalField(max_digits=19, decimal_places=2)
    seguro_de_vivienda = models.DecimalField(max_digits=19, decimal_places=2)
    suspension = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'infonavit_det'


class IsptMensual(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    base_gravable = models.DecimalField(max_digits=19, decimal_places=2)
    cuota_fija = models.DecimalField(max_digits=19, decimal_places=2)
    date_created = models.DateTimeField()
    ejercicio = models.IntegerField()
    empleado = models.ForeignKey(Empleado, models.DO_NOTHING)
    impuesto_acumulado = models.DecimalField(max_digits=19, decimal_places=2)
    impuesto_acumulado_final = models.DecimalField(max_digits=19, decimal_places=2)
    impuesto_final = models.DecimalField(max_digits=19, decimal_places=2)
    impuesto_mensual = models.DecimalField(max_digits=19, decimal_places=2)
    last_updated = models.DateTimeField()
    limite_inferior = models.DecimalField(max_digits=19, decimal_places=2)
    limite_superior = models.DecimalField(max_digits=19, decimal_places=2)
    mes = models.CharField(max_length=255)
    nomina_por_empleado = models.ForeignKey('NominaPorEmpleado', models.DO_NOTHING)
    resultado_impuesto = models.DecimalField(max_digits=19, decimal_places=2)
    resultado_subsidio = models.DecimalField(max_digits=19, decimal_places=2)
    subsidio_acumulado = models.DecimalField(max_digits=19, decimal_places=2)
    subsidio_acumulado_final = models.DecimalField(max_digits=19, decimal_places=2)
    subsidio_final = models.DecimalField(max_digits=19, decimal_places=2)
    subsidio_mensual = models.DecimalField(max_digits=19, decimal_places=2)
    tarifa = models.DecimalField(max_digits=19, decimal_places=2)
    resultado_subsidio_aplicado = models.DecimalField(max_digits=19, decimal_places=2)
    subsidio_aplicado = models.DecimalField(max_digits=19, decimal_places=2)
    permiso_retardo_acu = models.DecimalField(max_digits=19, decimal_places=2)
    impuesto_det_acu = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'ispt_mensual'


class Mes(models.Model):
    mes = models.PositiveIntegerField()
    mes_nombre = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'mes'


class ModificacionSalarial(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    comentario = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField()
    empleado = models.ForeignKey(Empleado, models.DO_NOTHING)
    fecha = models.DateField()
    last_updated = models.DateTimeField()
    salario_anterior = models.DecimalField(max_digits=19, decimal_places=2)
    salario_nuevo = models.DecimalField(max_digits=19, decimal_places=2)
    sdi_anterior = models.DecimalField(max_digits=19, decimal_places=2)
    sdi_nuevo = models.DecimalField(max_digits=19, decimal_places=2)
    tipo = models.CharField(max_length=11)
    bimestre = models.IntegerField(blank=True, null=True)
    calculo_sdi = models.ForeignKey(CalculoSdi, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modificacion_salarial'


class MotivoDeBaja(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    clave = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'motivo_de_baja'


class MotivoDeSeparacion(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    descripcion = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'motivo_de_separacion'


class Nomina(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    dia_de_pago = models.CharField(max_length=9)
    empresa = models.ForeignKey(Empresa, models.DO_NOTHING)
    folio = models.IntegerField()
    forma_de_pago = models.CharField(max_length=13)
    last_updated = models.DateTimeField()
    pago = models.DateTimeField()
    periodicidad = models.CharField(max_length=9)
    periodo_fecha_final = models.DateTimeField()
    periodo_fecha_inicial = models.DateTimeField()
    tipo = models.CharField(max_length=20, blank=True, null=True)
    total = models.DecimalField(max_digits=19, decimal_places=2)
    corte = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=9)
    calendario_det = models.ForeignKey(CalendarioDet, models.DO_NOTHING, blank=True, null=True)
    ejercicio = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nomina'


class NominaPorEmpleado(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    antiguedad_en_semanas = models.IntegerField()
    base_gravable = models.DecimalField(max_digits=19, decimal_places=2)
    cfdi = models.ForeignKey(Cfdi, models.DO_NOTHING, blank=True, null=True)
    comentario = models.CharField(max_length=200, blank=True, null=True)
    date_created = models.DateTimeField()
    empleado = models.ForeignKey(Empleado, models.DO_NOTHING)
    impuesto_subsidio = models.DecimalField(max_digits=19, decimal_places=2)
    last_updated = models.DateTimeField()
    nomina = models.ForeignKey(Nomina, models.DO_NOTHING)
    salario_diario_base = models.DecimalField(max_digits=19, decimal_places=2)
    salario_diario_integrado = models.DecimalField(max_digits=19, decimal_places=2)
    subsidio_empleo_aplicado = models.DecimalField(max_digits=19, decimal_places=2)
    total = models.DecimalField(max_digits=19, decimal_places=2)
    total_excento = models.DecimalField(max_digits=19, decimal_places=2)
    total_gravado = models.DecimalField(max_digits=19, decimal_places=2)
    ubicacion = models.ForeignKey('Ubicacion', models.DO_NOTHING)
    faltas = models.IntegerField(blank=True, null=True)
    incapacidades = models.IntegerField(blank=True, null=True)
    asistencia = models.ForeignKey(Asistencia, models.DO_NOTHING, blank=True, null=True)
    dias_del_periodo = models.IntegerField()
    dias_trabajados = models.DecimalField(max_digits=19, decimal_places=4)
    fraccion_descanso = models.FloatField()
    vacaciones = models.IntegerField()
    orden = models.IntegerField(blank=True, null=True)
    finiquito = models.TextField()  # This field type is a guess.
    recibo_firmado = models.TextField()  # This field type is a guess.
    relacionado = models.CharField(max_length=50, blank=True, null=True)
    impuesto_nomina = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nomina_por_empleado'


class NominaPorEmpleadoDet(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    comentario = models.CharField(max_length=255)
    concepto = models.ForeignKey(ConceptoDeNomina, models.DO_NOTHING)
    date_created = models.DateTimeField()
    importe_excento = models.DecimalField(max_digits=19, decimal_places=2)
    importe_gravado = models.DecimalField(max_digits=19, decimal_places=2)
    last_updated = models.DateTimeField()
    parent = models.ForeignKey(NominaPorEmpleado, models.DO_NOTHING)
    conceptos_idx = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nomina_por_empleado_det'


class NominaPorEmpleadoDetRes(models.Model):
    id = models.BigIntegerField()
    version = models.BigIntegerField()
    comentario = models.CharField(max_length=255)
    concepto_id = models.BigIntegerField()
    date_created = models.DateTimeField()
    importe_excento = models.DecimalField(max_digits=19, decimal_places=2)
    importe_gravado = models.DecimalField(max_digits=19, decimal_places=2)
    last_updated = models.DateTimeField()
    parent_id = models.BigIntegerField()
    conceptos_idx = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nomina_por_empleado_det_res'


class NominaPorEmpleadoRes(models.Model):
    id = models.BigIntegerField()
    version = models.BigIntegerField()
    antiguedad_en_semanas = models.IntegerField()
    base_gravable = models.DecimalField(max_digits=19, decimal_places=2)
    cfdi_id = models.BigIntegerField(blank=True, null=True)
    comentario = models.CharField(max_length=200, blank=True, null=True)
    date_created = models.DateTimeField()
    empleado_id = models.BigIntegerField()
    impuesto_subsidio = models.DecimalField(max_digits=19, decimal_places=2)
    last_updated = models.DateTimeField()
    nomina_id = models.BigIntegerField()
    salario_diario_base = models.DecimalField(max_digits=19, decimal_places=2)
    salario_diario_integrado = models.DecimalField(max_digits=19, decimal_places=2)
    subsidio_empleo_aplicado = models.DecimalField(max_digits=19, decimal_places=2)
    total = models.DecimalField(max_digits=19, decimal_places=2)
    total_excento = models.DecimalField(max_digits=19, decimal_places=2)
    total_gravado = models.DecimalField(max_digits=19, decimal_places=2)
    ubicacion_id = models.BigIntegerField()
    faltas = models.IntegerField(blank=True, null=True)
    incapacidades = models.IntegerField(blank=True, null=True)
    asistencia_id = models.BigIntegerField(blank=True, null=True)
    dias_del_periodo = models.IntegerField()
    dias_trabajados = models.DecimalField(max_digits=19, decimal_places=4)
    fraccion_descanso = models.FloatField()
    vacaciones = models.IntegerField()
    orden = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nomina_por_empleado_res'


class OperacionGenerica(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    calendario_det = models.ForeignKey(CalendarioDet, models.DO_NOTHING)
    comentario = models.CharField(max_length=250, blank=True, null=True)
    concepto = models.ForeignKey(ConceptoDeNomina, models.DO_NOTHING)
    date_created = models.DateTimeField()
    empleado = models.ForeignKey(Empleado, models.DO_NOTHING)
    importe_excento = models.DecimalField(max_digits=19, decimal_places=2)
    importe_gravado = models.DecimalField(max_digits=19, decimal_places=2)
    last_updated = models.DateTimeField()
    nomina_por_empleado_det = models.ForeignKey(NominaPorEmpleadoDet, models.DO_NOTHING, blank=True, null=True)
    tipo = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'operacion_generica'


class OperacionGenericaGrupo(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    calendario_det = models.ForeignKey(CalendarioDet, models.DO_NOTHING)
    comentario = models.CharField(max_length=250, blank=True, null=True)
    concepto = models.ForeignKey(ConceptoDeNomina, models.DO_NOTHING)
    date_created = models.DateTimeField()
    importe_excento = models.DecimalField(max_digits=19, decimal_places=2)
    importe_gravado = models.DecimalField(max_digits=19, decimal_places=2)
    last_updated = models.DateTimeField()
    tipo = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'operacion_generica_grupo'


class OperacionGenericaGrupoOperacionGenerica(models.Model):
    operacion_generica_grupo_partidas_id = models.BigIntegerField(blank=True, null=True)
    operacion_generica = models.ForeignKey(OperacionGenerica, models.DO_NOTHING, blank=True, null=True)
    partidas_idx = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'operacion_generica_grupo_operacion_generica'


class OtraDeduccion(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    comentario = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField()
    empleado = models.ForeignKey(Empleado, models.DO_NOTHING)
    importe = models.DecimalField(max_digits=19, decimal_places=2)
    importe_excento = models.DecimalField(max_digits=19, decimal_places=2)
    importe_gravado = models.DecimalField(max_digits=19, decimal_places=2)
    last_updated = models.DateTimeField()
    saldo = models.DecimalField(max_digits=19, decimal_places=2)
    tipo = models.CharField(max_length=21)
    calendario_det_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'otra_deduccion'


class OtraDeduccionAbono(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    comentario = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField()
    fecha = models.DateTimeField()
    importe = models.DecimalField(max_digits=19, decimal_places=2)
    last_updated = models.DateTimeField()
    nomina_por_empleado_det = models.ForeignKey(NominaPorEmpleadoDet, models.DO_NOTHING, blank=True, null=True)
    otra_deduccion = models.ForeignKey(OtraDeduccion, models.DO_NOTHING)
    abonos_idx = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'otra_deduccion_abono'


class PensionAlimenticia(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    comentario = models.CharField(max_length=255)
    date_created = models.DateTimeField()
    empleado = models.ForeignKey(Empleado, models.DO_NOTHING)
    last_updated = models.DateTimeField()
    beneficiario = models.CharField(max_length=255)
    neto = models.TextField()  # This field type is a guess.
    porcentaje = models.DecimalField(max_digits=19, decimal_places=2)
    forma_de_pago = models.CharField(max_length=13)
    tipo_de_pago = models.CharField(max_length=9)

    class Meta:
        managed = False
        db_table = 'pension_alimenticia'


class PerfilDeEmpleado(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    departamento = models.ForeignKey(Departamento, models.DO_NOTHING)
    empleado = models.OneToOneField(Empleado, models.DO_NOTHING)
    empresa = models.ForeignKey(Empresa, models.DO_NOTHING)
    jornada = models.CharField(max_length=10)
    last_updated = models.DateTimeField()
    numero_de_trabajador = models.CharField(max_length=255, blank=True, null=True)
    puesto = models.ForeignKey('Puesto', models.DO_NOTHING)
    regimen_contratacion = models.ForeignKey('SatRegimenContratacion', models.DO_NOTHING)
    riesgo_puesto = models.ForeignKey('SatRiesgoPuesto', models.DO_NOTHING)
    tipo = models.CharField(max_length=13)
    tipo_de_contrato = models.CharField(max_length=13)
    ubicacion = models.ForeignKey('Ubicacion', models.DO_NOTHING)
    turno = models.ForeignKey('Turno', models.DO_NOTHING, blank=True, null=True)
    tipo_de_incentivo = models.CharField(max_length=9, blank=True, null=True)
    declaracion_anual = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'perfil_de_empleado'


class Prestacion(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    descripcion = models.CharField(max_length=255)
    empresa = models.ForeignKey(Empresa, models.DO_NOTHING)
    formula = models.CharField(max_length=255)
    last_updated = models.DateTimeField()
    nombre = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'prestacion'


class Prestamo(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    alta = models.DateTimeField()
    autorizo = models.CharField(max_length=255)
    comentario = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField()
    empleado = models.ForeignKey(Empleado, models.DO_NOTHING)
    fecha_de_autorizacion = models.DateTimeField()
    importe = models.DecimalField(max_digits=19, decimal_places=2)
    last_updated = models.DateTimeField()
    saldo = models.DecimalField(max_digits=19, decimal_places=2)
    tasa_descuento = models.DecimalField(max_digits=19, decimal_places=2)
    tipo = models.CharField(max_length=20)
    importe_fijo = models.DecimalField(max_digits=19, decimal_places=2)
    calendario_det = models.ForeignKey(CalendarioDet, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prestamo'


class PrestamoAbono(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    comentario = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField()
    fecha = models.DateTimeField()
    importe = models.DecimalField(max_digits=19, decimal_places=2)
    last_updated = models.DateTimeField()
    nomina_por_empleado_det = models.ForeignKey(NominaPorEmpleadoDet, models.DO_NOTHING, blank=True, null=True)
    prestamo = models.ForeignKey(Prestamo, models.DO_NOTHING)
    saldo = models.DecimalField(max_digits=19, decimal_places=2)
    saldo_anterior = models.DecimalField(max_digits=19, decimal_places=2)
    abonos_idx = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prestamo_abono'


class Ptu(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    dias_ptu = models.BigIntegerField()
    ejercicio = models.IntegerField()
    factor = models.DecimalField(max_digits=19, decimal_places=2)
    factor_dias = models.DecimalField(max_digits=19, decimal_places=6)
    factor_salario = models.DecimalField(max_digits=19, decimal_places=6)
    last_updated = models.DateTimeField()
    monto = models.DecimalField(max_digits=19, decimal_places=2)
    monto_dias = models.DecimalField(max_digits=19, decimal_places=2)
    monto_salario = models.DecimalField(max_digits=19, decimal_places=2)
    remanente = models.DecimalField(max_digits=19, decimal_places=2)
    salario_minimo_general = models.DecimalField(max_digits=19, decimal_places=2)
    tope_anual_acumulado = models.DecimalField(max_digits=19, decimal_places=2)
    tope_smg = models.DecimalField(max_digits=19, decimal_places=2)
    sindicalizado_maximo = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    sindicalizado_nombre = models.CharField(max_length=255, blank=True, null=True)
    fecha_pago = models.DateField(blank=True, null=True)
    montoe = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    complemento = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'ptu'


class PtuDet(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    comisiones = models.DecimalField(max_digits=19, decimal_places=2)
    date_created = models.DateTimeField()
    dias_del_ejercicio = models.IntegerField()
    dias_ptu = models.BigIntegerField()
    empleado = models.ForeignKey(Empleado, models.DO_NOTHING)
    faltas = models.BigIntegerField()
    incapacidades = models.BigIntegerField()
    incentivo = models.DecimalField(max_digits=19, decimal_places=2)
    isr_acreditable = models.DecimalField(max_digits=19, decimal_places=2)
    isr_por_retener = models.DecimalField(max_digits=19, decimal_places=2)
    last_updated = models.DateTimeField()
    monto_dias = models.DecimalField(max_digits=19, decimal_places=6)
    monto_salario = models.DecimalField(max_digits=19, decimal_places=6)
    no_asignado = models.TextField()  # This field type is a guess.
    no_asignado_comentario = models.CharField(max_length=100, blank=True, null=True)
    no_entregar = models.TextField()  # This field type is a guess.
    nomina_por_empleado = models.ForeignKey(NominaPorEmpleado, models.DO_NOTHING, blank=True, null=True)
    otras_ded = models.DecimalField(max_digits=19, decimal_places=2)
    pensiona = models.DecimalField(max_digits=19, decimal_places=2)
    permisosp = models.BigIntegerField()
    por_pagar_bruto = models.DecimalField(max_digits=19, decimal_places=2)
    por_pagar_neto = models.DecimalField(max_digits=19, decimal_places=2)
    prestamo = models.DecimalField(max_digits=19, decimal_places=2)
    ptu = models.ForeignKey(Ptu, models.DO_NOTHING)
    ptu_excento = models.DecimalField(max_digits=19, decimal_places=2)
    ptu_gravado = models.DecimalField(max_digits=19, decimal_places=2)
    retardos = models.DecimalField(max_digits=19, decimal_places=2)
    salario = models.DecimalField(max_digits=19, decimal_places=2)
    salario_diario = models.DecimalField(max_digits=19, decimal_places=2)
    salario_mensual = models.DecimalField(max_digits=19, decimal_places=2)
    smi_isr = models.DecimalField(max_digits=19, decimal_places=2)
    smi_resultado = models.DecimalField(max_digits=19, decimal_places=2)
    smi_subsidio = models.DecimalField(max_digits=19, decimal_places=2)
    tmg_isr = models.DecimalField(max_digits=19, decimal_places=2)
    tmg_resultado = models.DecimalField(max_digits=19, decimal_places=2)
    tmg_subsidio = models.DecimalField(max_digits=19, decimal_places=2)
    tope_anual = models.DecimalField(max_digits=19, decimal_places=2)
    total = models.DecimalField(max_digits=19, decimal_places=2)
    total_mensual_gravado = models.DecimalField(max_digits=19, decimal_places=2)
    vacaciones = models.DecimalField(max_digits=19, decimal_places=2)
    calendario_det = models.ForeignKey(CalendarioDet, models.DO_NOTHING, blank=True, null=True)
    monto_ptu = models.DecimalField(max_digits=19, decimal_places=2)
    tipo = models.IntegerField(blank=True, null=True)
    alta = models.DateField(blank=True, null=True)
    baja = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    ejerciciom1 = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    ejerciciom2 = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    ejerciciom3 = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    promedio_anual = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    ptu_definido = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    ptu_excento_actual = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    ptu_gravado_actual = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    salario90 = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    apagar_actual = models.DecimalField(max_digits=19, decimal_places=2)
    apagar_previo = models.DecimalField(max_digits=19, decimal_places=2)
    excento_actual = models.DecimalField(max_digits=19, decimal_places=2)
    excento_previo = models.DecimalField(max_digits=19, decimal_places=2)
    gravado_actual = models.DecimalField(max_digits=19, decimal_places=2)
    impuesto_actual = models.DecimalField(max_digits=19, decimal_places=2)
    impuesto_previo = models.DecimalField(max_digits=19, decimal_places=2)
    gravado_previo = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'ptu_det'


class PtuDetRes20150602(models.Model):
    id = models.BigIntegerField()
    version = models.BigIntegerField()
    comisiones = models.DecimalField(max_digits=19, decimal_places=2)
    date_created = models.DateTimeField()
    dias_del_ejercicio = models.IntegerField()
    dias_ptu = models.BigIntegerField()
    empleado_id = models.BigIntegerField()
    faltas = models.BigIntegerField()
    incapacidades = models.BigIntegerField()
    incentivo = models.DecimalField(max_digits=19, decimal_places=2)
    isr_acreditable = models.DecimalField(max_digits=19, decimal_places=2)
    isr_por_retener = models.DecimalField(max_digits=19, decimal_places=2)
    last_updated = models.DateTimeField()
    monto_dias = models.DecimalField(max_digits=19, decimal_places=6)
    monto_salario = models.DecimalField(max_digits=19, decimal_places=6)
    no_asignado = models.TextField()  # This field type is a guess.
    no_asignado_comentario = models.CharField(max_length=100, blank=True, null=True)
    no_entregar = models.TextField()  # This field type is a guess.
    nomina_por_empleado_id = models.BigIntegerField(blank=True, null=True)
    otras_ded = models.DecimalField(max_digits=19, decimal_places=2)
    pensiona = models.DecimalField(max_digits=19, decimal_places=2)
    permisosp = models.BigIntegerField()
    por_pagar_bruto = models.DecimalField(max_digits=19, decimal_places=2)
    por_pagar_neto = models.DecimalField(max_digits=19, decimal_places=2)
    prestamo = models.DecimalField(max_digits=19, decimal_places=2)
    ptu_id = models.BigIntegerField()
    ptu_excento = models.DecimalField(max_digits=19, decimal_places=2)
    ptu_gravado = models.DecimalField(max_digits=19, decimal_places=2)
    retardos = models.DecimalField(max_digits=19, decimal_places=2)
    salario = models.DecimalField(max_digits=19, decimal_places=2)
    salario_diario = models.DecimalField(max_digits=19, decimal_places=2)
    salario_mensual = models.DecimalField(max_digits=19, decimal_places=2)
    smi_isr = models.DecimalField(max_digits=19, decimal_places=2)
    smi_resultado = models.DecimalField(max_digits=19, decimal_places=2)
    smi_subsidio = models.DecimalField(max_digits=19, decimal_places=2)
    tmg_isr = models.DecimalField(max_digits=19, decimal_places=2)
    tmg_resultado = models.DecimalField(max_digits=19, decimal_places=2)
    tmg_subsidio = models.DecimalField(max_digits=19, decimal_places=2)
    tope_anual = models.DecimalField(max_digits=19, decimal_places=2)
    total = models.DecimalField(max_digits=19, decimal_places=2)
    total_mensual_gravado = models.DecimalField(max_digits=19, decimal_places=2)
    vacaciones = models.DecimalField(max_digits=19, decimal_places=2)
    calendario_det_id = models.BigIntegerField(blank=True, null=True)
    monto_ptu = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'ptu_det_res_20150602'


class PtuDetRes20160610(models.Model):
    id = models.BigIntegerField()
    version = models.BigIntegerField()
    comisiones = models.DecimalField(max_digits=19, decimal_places=2)
    date_created = models.DateTimeField()
    dias_del_ejercicio = models.IntegerField()
    dias_ptu = models.BigIntegerField()
    empleado_id = models.BigIntegerField()
    faltas = models.BigIntegerField()
    incapacidades = models.BigIntegerField()
    incentivo = models.DecimalField(max_digits=19, decimal_places=2)
    isr_acreditable = models.DecimalField(max_digits=19, decimal_places=2)
    isr_por_retener = models.DecimalField(max_digits=19, decimal_places=2)
    last_updated = models.DateTimeField()
    monto_dias = models.DecimalField(max_digits=19, decimal_places=6)
    monto_salario = models.DecimalField(max_digits=19, decimal_places=6)
    no_asignado = models.TextField()  # This field type is a guess.
    no_asignado_comentario = models.CharField(max_length=100, blank=True, null=True)
    no_entregar = models.TextField()  # This field type is a guess.
    nomina_por_empleado_id = models.BigIntegerField(blank=True, null=True)
    otras_ded = models.DecimalField(max_digits=19, decimal_places=2)
    pensiona = models.DecimalField(max_digits=19, decimal_places=2)
    permisosp = models.BigIntegerField()
    por_pagar_bruto = models.DecimalField(max_digits=19, decimal_places=2)
    por_pagar_neto = models.DecimalField(max_digits=19, decimal_places=2)
    prestamo = models.DecimalField(max_digits=19, decimal_places=2)
    ptu_id = models.BigIntegerField()
    ptu_excento = models.DecimalField(max_digits=19, decimal_places=2)
    ptu_gravado = models.DecimalField(max_digits=19, decimal_places=2)
    retardos = models.DecimalField(max_digits=19, decimal_places=2)
    salario = models.DecimalField(max_digits=19, decimal_places=2)
    salario_diario = models.DecimalField(max_digits=19, decimal_places=2)
    salario_mensual = models.DecimalField(max_digits=19, decimal_places=2)
    smi_isr = models.DecimalField(max_digits=19, decimal_places=2)
    smi_resultado = models.DecimalField(max_digits=19, decimal_places=2)
    smi_subsidio = models.DecimalField(max_digits=19, decimal_places=2)
    tmg_isr = models.DecimalField(max_digits=19, decimal_places=2)
    tmg_resultado = models.DecimalField(max_digits=19, decimal_places=2)
    tmg_subsidio = models.DecimalField(max_digits=19, decimal_places=2)
    tope_anual = models.DecimalField(max_digits=19, decimal_places=2)
    total = models.DecimalField(max_digits=19, decimal_places=2)
    total_mensual_gravado = models.DecimalField(max_digits=19, decimal_places=2)
    vacaciones = models.DecimalField(max_digits=19, decimal_places=2)
    calendario_det_id = models.BigIntegerField(blank=True, null=True)
    monto_ptu = models.DecimalField(max_digits=19, decimal_places=2)
    tipo = models.IntegerField(blank=True, null=True)
    alta = models.DateField(blank=True, null=True)
    baja = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ptu_det_res_20160610'


class PtuDetRes20160706Todo(models.Model):
    id = models.BigIntegerField()
    version = models.BigIntegerField()
    comisiones = models.DecimalField(max_digits=19, decimal_places=2)
    date_created = models.DateTimeField()
    dias_del_ejercicio = models.IntegerField()
    dias_ptu = models.BigIntegerField()
    empleado_id = models.BigIntegerField()
    faltas = models.BigIntegerField()
    incapacidades = models.BigIntegerField()
    incentivo = models.DecimalField(max_digits=19, decimal_places=2)
    isr_acreditable = models.DecimalField(max_digits=19, decimal_places=2)
    isr_por_retener = models.DecimalField(max_digits=19, decimal_places=2)
    last_updated = models.DateTimeField()
    monto_dias = models.DecimalField(max_digits=19, decimal_places=6)
    monto_salario = models.DecimalField(max_digits=19, decimal_places=6)
    no_asignado = models.TextField()  # This field type is a guess.
    no_asignado_comentario = models.CharField(max_length=100, blank=True, null=True)
    no_entregar = models.TextField()  # This field type is a guess.
    nomina_por_empleado_id = models.BigIntegerField(blank=True, null=True)
    otras_ded = models.DecimalField(max_digits=19, decimal_places=2)
    pensiona = models.DecimalField(max_digits=19, decimal_places=2)
    permisosp = models.BigIntegerField()
    por_pagar_bruto = models.DecimalField(max_digits=19, decimal_places=2)
    por_pagar_neto = models.DecimalField(max_digits=19, decimal_places=2)
    prestamo = models.DecimalField(max_digits=19, decimal_places=2)
    ptu_id = models.BigIntegerField()
    ptu_excento = models.DecimalField(max_digits=19, decimal_places=2)
    ptu_gravado = models.DecimalField(max_digits=19, decimal_places=2)
    retardos = models.DecimalField(max_digits=19, decimal_places=2)
    salario = models.DecimalField(max_digits=19, decimal_places=2)
    salario_diario = models.DecimalField(max_digits=19, decimal_places=2)
    salario_mensual = models.DecimalField(max_digits=19, decimal_places=2)
    smi_isr = models.DecimalField(max_digits=19, decimal_places=2)
    smi_resultado = models.DecimalField(max_digits=19, decimal_places=2)
    smi_subsidio = models.DecimalField(max_digits=19, decimal_places=2)
    tmg_isr = models.DecimalField(max_digits=19, decimal_places=2)
    tmg_resultado = models.DecimalField(max_digits=19, decimal_places=2)
    tmg_subsidio = models.DecimalField(max_digits=19, decimal_places=2)
    tope_anual = models.DecimalField(max_digits=19, decimal_places=2)
    total = models.DecimalField(max_digits=19, decimal_places=2)
    total_mensual_gravado = models.DecimalField(max_digits=19, decimal_places=2)
    vacaciones = models.DecimalField(max_digits=19, decimal_places=2)
    calendario_det_id = models.BigIntegerField(blank=True, null=True)
    monto_ptu = models.DecimalField(max_digits=19, decimal_places=2)
    tipo = models.IntegerField(blank=True, null=True)
    alta = models.DateField(blank=True, null=True)
    baja = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ptu_det_res_20160706todo'


class Puesto(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    clave = models.CharField(unique=True, max_length=100, blank=True, null=True)
    date_created = models.DateTimeField()
    descripcion = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'puesto'


class ReciboDeNomina(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    cfdi = models.ForeignKey(Cfdi, models.DO_NOTHING)
    date_created = models.DateTimeField()
    empleado = models.ForeignKey(Empleado, models.DO_NOTHING)
    last_updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'recibo_de_nomina'


class RegistrationCode(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_created = models.DateTimeField()
    token = models.CharField(max_length=255)
    username = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'registration_code'


class RegistroDeComisiones(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    calendario_det = models.ForeignKey(CalendarioDet, models.DO_NOTHING)
    comentario = models.CharField(max_length=255)
    date_created = models.DateTimeField()
    empleado = models.ForeignKey(Empleado, models.DO_NOTHING)
    importe = models.DecimalField(max_digits=19, decimal_places=2)
    last_updated = models.DateTimeField()
    nomina_por_empleado_det = models.ForeignKey(NominaPorEmpleadoDet, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'registro_de_comisiones'


class ReglaBono(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    ejercicio = models.IntegerField()
    last_updated = models.DateTimeField()
    regla = models.CharField(max_length=700, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'regla_bono'


class Reporte(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    grupo = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'reporte'


class Role(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    authority = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'role'


class Salario(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    banco = models.ForeignKey('SatBanco', models.DO_NOTHING, blank=True, null=True)
    base_cotizacion = models.CharField(max_length=50, blank=True, null=True)
    clabe = models.CharField(max_length=255, blank=True, null=True)
    empleado = models.OneToOneField(Empleado, models.DO_NOTHING)
    forma_de_pago = models.CharField(max_length=13)
    periodicidad = models.CharField(max_length=14)
    salario_diario = models.DecimalField(max_digits=19, decimal_places=2)
    salario_diario_integrado = models.DecimalField(max_digits=19, decimal_places=2)
    salario_variable = models.DecimalField(max_digits=19, decimal_places=2)
    numero_de_cuenta = models.CharField(max_length=255, blank=True, null=True)
    prima_dominical_fija = models.TextField(blank=True, null=True)  # This field type is a guess.
    sucursal_banco = models.CharField(max_length=255, blank=True, null=True)
    tipo_cuenta = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'salario'


class SatBanco(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    clave = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=300)
    nombre_corto = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'sat_banco'


class SatDeduccion(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    clave = models.IntegerField(unique=True)
    descripcion = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'sat_deduccion'


class SatIncapacidad(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    clave = models.IntegerField(unique=True)
    descripcion = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'sat_incapacidad'


class SatPercepcion(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    clave = models.IntegerField(unique=True)
    descripcion = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'sat_percepcion'


class SatRegimenContratacion(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    clave = models.IntegerField(unique=True)
    descripcion = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'sat_regimen_contratacion'


class SatRiesgoPuesto(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    clave = models.IntegerField(unique=True)
    descripcion = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'sat_riesgo_puesto'


class SeguridadSocial(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    alta = models.DateTimeField(blank=True, null=True)
    comentario = models.CharField(max_length=300, blank=True, null=True)
    empleado = models.OneToOneField(Empleado, models.DO_NOTHING)
    numero = models.CharField(max_length=15)
    turno = models.CharField(max_length=8)
    unidad_medica = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seguridad_social'


class SubsidioEmpleo(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    desde = models.DecimalField(max_digits=19, decimal_places=2)
    hasta = models.DecimalField(max_digits=19, decimal_places=2)
    last_updated = models.DateTimeField()
    subsidio = models.DecimalField(max_digits=19, decimal_places=2)
    ejercicio = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'subsidio_empleo'


class SubsidioEmpleo2014(models.Model):
    id = models.BigIntegerField()
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    desde = models.DecimalField(max_digits=19, decimal_places=2)
    hasta = models.DecimalField(max_digits=19, decimal_places=2)
    last_updated = models.DateTimeField()
    subsidio = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'subsidio_empleo_2014'


class TarifaIsr(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    cuota_fija = models.DecimalField(max_digits=19, decimal_places=2)
    limite_inferior = models.DecimalField(max_digits=19, decimal_places=2)
    limite_superior = models.DecimalField(max_digits=19, decimal_places=2)
    porcentaje = models.DecimalField(max_digits=19, decimal_places=2)
    ejercicio = models.IntegerField()
    tipo = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'tarifa_isr'


class TiempoExtra(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    asistencia = models.OneToOneField(Asistencia, models.DO_NOTHING)
    date_created = models.DateTimeField()
    ejercicio = models.IntegerField()
    empleado = models.ForeignKey(Empleado, models.DO_NOTHING)
    folio = models.IntegerField()
    last_updated = models.DateTimeField()
    nomina_por_empleado = models.ForeignKey(NominaPorEmpleado, models.DO_NOTHING, blank=True, null=True)
    tipo = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tiempo_extra'


class TiempoExtraDet(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    domingo = models.IntegerField()
    importe_dobles_excentos = models.DecimalField(max_digits=19, decimal_places=2)
    importe_dobles_gravados = models.DecimalField(max_digits=19, decimal_places=2)
    importe_triples_gravados = models.DecimalField(max_digits=19, decimal_places=2)
    jueves = models.IntegerField()
    lunes = models.IntegerField()
    martes = models.IntegerField()
    miercoles = models.IntegerField()
    minutos_dobles = models.IntegerField()
    minutos_triples = models.IntegerField()
    sabado = models.IntegerField()
    salario_diario = models.DecimalField(max_digits=19, decimal_places=2)
    semana = models.IntegerField()
    tiempo_extra = models.ForeignKey(TiempoExtra, models.DO_NOTHING)
    total_minutos = models.IntegerField()
    viernes = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tiempo_extra_det'


class TiempoExtraImss(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    domingo = models.DecimalField(max_digits=19, decimal_places=2)
    integra = models.DecimalField(max_digits=19, decimal_places=2)
    jueves = models.DecimalField(max_digits=19, decimal_places=2)
    lunes = models.DecimalField(max_digits=19, decimal_places=2)
    martes = models.DecimalField(max_digits=19, decimal_places=2)
    miercoles = models.DecimalField(max_digits=19, decimal_places=2)
    sabado = models.DecimalField(max_digits=19, decimal_places=2)
    semana = models.IntegerField()
    tiempo_extra_det = models.OneToOneField(TiempoExtraDet, models.DO_NOTHING)
    total = models.DecimalField(max_digits=19, decimal_places=2)
    viernes = models.DecimalField(max_digits=19, decimal_places=2)
    integra_triples = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'tiempo_extra_imss'


class Turno(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    descripcion = models.CharField(max_length=255)
    hora_limite_de_trabajo = models.TimeField()
    hora_limite_siguiente_dia = models.TextField()  # This field type is a guess.
    inicio_de_dia = models.TimeField()
    inicio_de_tiempo_extra = models.TimeField(blank=True, null=True)
    last_updated = models.DateTimeField()
    tiempo_de_comida = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'turno'


class TurnoDet(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    dia = models.CharField(max_length=255)
    entrada1 = models.TimeField(blank=True, null=True)
    entrada2 = models.TimeField(blank=True, null=True)
    salida1 = models.TimeField(blank=True, null=True)
    salida2 = models.TimeField(blank=True, null=True)
    turno = models.ForeignKey(Turno, models.DO_NOTHING)
    dias_idx = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'turno_det'


class Ubicacion(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    clave = models.CharField(unique=True, max_length=20)
    descripcion = models.CharField(max_length=300)
    direccion_calle = models.CharField(max_length=200, blank=True, null=True)
    direccion_codigo_postal = models.CharField(max_length=255, blank=True, null=True)
    direccion_colonia = models.CharField(max_length=255, blank=True, null=True)
    direccion_estado = models.CharField(max_length=255, blank=True, null=True)
    direccion_municipio = models.CharField(max_length=255, blank=True, null=True)
    direccion_numero_exterior = models.CharField(max_length=50, blank=True, null=True)
    direccion_numero_interior = models.CharField(max_length=50, blank=True, null=True)
    direccion_pais = models.CharField(max_length=100, blank=True, null=True)
    empresa = models.ForeignKey(Empresa, models.DO_NOTHING)
    numero = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ubicacion'


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    account_expired = models.TextField()  # This field type is a guess.
    account_locked = models.TextField()  # This field type is a guess.
    enabled = models.TextField()  # This field type is a guess.
    password = models.CharField(max_length=255)
    password_expired = models.TextField()  # This field type is a guess.
    username = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'user'


class UserRole(models.Model):
    role = models.OneToOneField(Role, models.DO_NOTHING, primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_role'
        unique_together = (('role', 'user'),)


class Uuidparacancelar20190131(models.Model):
    rfc = models.CharField(max_length=12)
    receptor_rfc = models.CharField(max_length=13)
    uuid = models.CharField(max_length=300, blank=True, null=True)
    total = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'uuidparacancelar20190131'


class Uuidparacancelar201901312(models.Model):
    rfc = models.CharField(max_length=12)
    receptor_rfc = models.CharField(max_length=13)
    uuid = models.CharField(max_length=300, blank=True, null=True)
    total = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'uuidparacancelar20190131_2'


class Vacaciones(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    autorizacion = models.ForeignKey(Autorizacion, models.DO_NOTHING, blank=True, null=True)
    comentario = models.CharField(max_length=250, blank=True, null=True)
    date_created = models.DateTimeField()
    empleado = models.ForeignKey(Empleado, models.DO_NOTHING)
    last_updated = models.DateTimeField()
    solicitud = models.DateField()
    pg = models.TextField()  # This field type is a guess.
    acreditada = models.TextField()  # This field type is a guess.
    control = models.ForeignKey(ControlDeVacaciones, models.DO_NOTHING, blank=True, null=True)
    dias_pagados = models.IntegerField()
    calendario_det = models.ForeignKey(CalendarioDet, models.DO_NOTHING, blank=True, null=True)
    cierre_anual = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'vacaciones'


class VacacionesDias(models.Model):
    vacaciones = models.ForeignKey(Vacaciones, models.DO_NOTHING, blank=True, null=True)
    dias_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vacaciones_dias'


class VacacionesGrupo(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    calendario_det = models.ForeignKey(CalendarioDet, models.DO_NOTHING, blank=True, null=True)
    comentario = models.CharField(max_length=250)
    date_created = models.DateTimeField()
    fecha_final = models.DateField()
    fecha_inicial = models.DateField()
    last_updated = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'vacaciones_grupo'


class VacacionesGrupoVacaciones(models.Model):
    vacaciones_grupo_partidas = models.ForeignKey(VacacionesGrupo, models.DO_NOTHING, blank=True, null=True)
    vacaciones = models.ForeignKey(Vacaciones, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vacaciones_grupo_vacaciones'


class ZonaEconomica(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    clave = models.CharField(max_length=255)
    salario = models.DecimalField(max_digits=19, decimal_places=2)
    ejercicio = models.IntegerField()
    uma = models.DecimalField(max_digits=19, decimal_places=2)
    factor_infonavit = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'zona_economica'
