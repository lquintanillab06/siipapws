from applications.cfdi.cfdi_sat.cfdi_models import ObjectCfdiEntityFactory
from applications.cfdi.cfdi_sat.builders.comprobante_builder_director import ComprobanteBuilderDirector
from datetime import datetime,date


class CfdiEgresoFacade():

    def create_cfdi_egreso(self):
        egreso = ObjectCfdiEntityFactory.create_entity_sat_egreso()
        egreso.serie = "FAC"
        egreso.folio = "1000"
        egreso.forma_pago = "efectivo"
        egreso.tipo_cambio = 1.00
        egreso.subtotal = 84.00
        egreso.total = 100.00
        egreso.descuento = 1
        egreso.condiciones_de_pago = "PUE"
        egreso.exportacion = "02"
        egreso.metodo_pago = "PUE"
        egreso.lugar_de_expedicion = "02870"
        egreso.moneda = 'MXN'
        egreso.fecha = date(2023,1,13)

        emisor = ObjectCfdiEntityFactory.create_cfdi_emisor()
        emisor.nombre = "LUIS QUINTANILLA BAUTISTA"
        emisor.rfc = "LQB790930A69"
        emisor.regimen_fiscal = "605"
       
        egreso.add_emisor(emisor)

        receptor = ObjectCfdiEntityFactory.create_cfdi_receptor()
        receptor.nombre = "PAPEL"
        receptor.rfc = "PAP830101CR3"
        receptor.regimen_fiscal = "601"
        receptor.domicilio_fiscal = "03200"
        receptor.uso_cfdi = "G01"
        
        egreso.add_receptor(receptor)

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

        egreso.add_concepto(concepto1)

        cfdi_traslado = ObjectCfdiEntityFactory.create_cfdi_traslado()
        cfdi_traslado.base = 84.00
        cfdi_traslado.importe = 16.00
        cfdi_traslado.impuesto = '02'
        cfdi_traslado.tasa_cuota = 'TASA'
        cfdi_traslado.tipo_factor = 'IVA'
        
        egreso.add_cfdi_impuestos(16,16)
        egreso.add_cfdi_traslado(cfdi_traslado)

        cfdi_retencion = ObjectCfdiEntityFactory.create_cfdi_retencion()
        cfdi_retencion.impuesto = '02'
        cfdi_retencion.importe = 16.00

        egreso.add_cfdi_retencion(cfdi_retencion)



        egreso.tipo_relacion = '02'

        egreso.add_relacionado('DSKAFKJLDLJFJKASKFDLJASÑFDLSDSFA')
        egreso.add_relacionado('POPYUTPRIUPIOYRTPUYPKRKKTÑYRKHÑL')
        


        comprobante = ComprobanteBuilderDirector().build(egreso)

        print('*'*100)
        print(egreso.__dict__)
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
        print(comprobante.CfdiRelacionados.TipoRelacion)
        for relacionado in comprobante.CfdiRelacionados.CfdiRelacionado:
            print(relacionado.UUID)

        print('*'*100)
        