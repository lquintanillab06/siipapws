from applications.cfdi.cfdi_sat.cfdi_models import ObjectCfdiEntityFactory
from applications.cfdi.cfdi_sat.builders.comprobante_builder_director import ComprobanteBuilderDirector
from datetime import datetime,date

class CfdiIngresoFacade():

    def create_cfdi_ingreso(self):
        ingreso  = ObjectCfdiEntityFactory.create_entity_sat_ingreso()
        print("Creando el ingreso")
        ingreso.serie = "FAC"
        ingreso.folio = "1000"
        ingreso.forma_pago = "efectivo"
        ingreso.tipo_cambio = 1.00
        ingreso.subtotal = 84.00
        ingreso.total = 100.00
        ingreso.descuento = 1
        ingreso.condiciones_de_pago = "PUE"
        ingreso.exportacion = "02"
        ingreso.metodo_pago = "PUE"
        ingreso.lugar_de_expedicion = "02870"
        ingreso.moneda = 'MXN'
        ingreso.fecha = date(2023,1,13)

        emisor = ObjectCfdiEntityFactory.create_cfdi_emisor()
        emisor.nombre = "LUIS QUINTANILLA BAUTISTA"
        emisor.rfc = "LQB790930A69"
        emisor.regimen_fiscal = "605"
       
        ingreso.add_emisor(emisor)

        receptor = ObjectCfdiEntityFactory.create_cfdi_receptor()
        receptor.nombre = "PAPEL"
        receptor.rfc = "PAP830101CR3"
        receptor.regimen_fiscal = "601"
        receptor.domicilio_fiscal = "03200"
        receptor.uso_cfdi = "G01"
        
        ingreso.add_receptor(receptor)

        concepto1 = ObjectCfdiEntityFactory.create_cfdi_concepto()
        concepto1.clav_prod_serv = 'POL100'
        concepto1.no_identificacion = '15000'
        concepto1.cantidad = 100
        concepto1.clave_unidad = 'MIL'
        concepto1.unidad = 'MILLAR'
        concepto1.descripcion = 'POLYPAP'
        concepto1.valor_unitario = 1
        concepto1.descuento = 1
        concepto1.importe = 100
        concepto1.objeto_imp = '02'

        concepto_traslado = ObjectCfdiEntityFactory.create_cfdi_concepto_traslado()
        concepto_traslado.base = 84.00
        concepto_traslado.importe = 16.00
        concepto_traslado.impuesto = '01'
        concepto_traslado.tasa_cuota = 'TASA'
        concepto_traslado.tipo_factor = 'IVA'
        
        concepto1.add_concepto_impuestos()
        concepto1.add_concepto_traslado(concepto_traslado)

        concepto_retencion = ObjectCfdiEntityFactory.create_cfdi_concepto_retencion()
        concepto_retencion.base = 84.00
        concepto_retencion.importe = 16.00
        concepto_retencion.impuesto = '01'
        concepto_retencion.tasa_cuota = 'TASA'
        concepto_retencion.tipo_factor = 'IVA'
        concepto1.add_concepto_retencion(concepto_retencion)

        ingreso.add_concepto(concepto1)

        cfdi_traslado = ObjectCfdiEntityFactory.create_cfdi_traslado()
        cfdi_traslado.base = 84.00
        cfdi_traslado.importe = 16.00
        cfdi_traslado.impuesto = '02'
        cfdi_traslado.tasa_cuota = 'TASA'
        cfdi_traslado.tipo_factor = 'IVA'
        
        ingreso.add_cfdi_impuestos(16,16)
        ingreso.add_cfdi_traslado(cfdi_traslado)

        cfdi_retencion = ObjectCfdiEntityFactory.create_cfdi_retencion()
        cfdi_retencion.impuesto = '02'
        cfdi_retencion.importe = 16.00

        ingreso.add_cfdi_retencion(cfdi_retencion)

        comprobante = ComprobanteBuilderDirector().build(ingreso)

        print('*'*100)
        print(ingreso.__dict__)
        print('*'*100)
        print(comprobante.__dict__)
        print(comprobante.Emisor.__dict__)
        print(comprobante.Receptor.__dict__)
        print(comprobante.Conceptos.__dict__)
        print('*'*100)
        print(comprobante.Conceptos.Concepto[0].__dict__)
        print(comprobante.Conceptos.Concepto[0].Impuestos.Traslados.Traslado[0].__dict__)
        print(comprobante.Conceptos.Concepto[0].Impuestos.Retenciones.Retencion[0].__dict__)
        print('*'*100)
        print(comprobante.Impuestos.__dict__)
        print(comprobante.Impuestos.Retenciones.Retencion[0].__dict__)
        print(comprobante.Impuestos.Traslados.Traslado[0].__dict__)
        print('*'*100)


