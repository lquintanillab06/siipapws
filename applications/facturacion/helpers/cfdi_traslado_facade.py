from applications.cfdi.cfdi_sat.cfdi_models import ObjectCfdiEntityFactory
from applications.cfdi.cfdi_sat.builders.comprobante_builder_director import ComprobanteBuilderDirector
from datetime import datetime,date


class CfdiTrasladoFacade():

    def create_cfdi_traslado(self):
        traslado = ObjectCfdiEntityFactory.create_entity_sat_traslado()
        traslado.serie = "FAC"
        traslado.folio = "1000"
        traslado.forma_pago = "efectivo"
        traslado.tipo_cambio = 1.00
        traslado.subtotal = 84.00
        traslado.total = 100.00
        traslado.descuento = 1
        traslado.condiciones_de_pago = "PUE"
        traslado.exportacion = "02"
        traslado.metodo_pago = "PUE"
        traslado.lugar_de_expedicion = "02870"
        traslado.moneda = 'MXN'
        traslado.fecha = date(2023,1,13)

        emisor = ObjectCfdiEntityFactory.create_cfdi_emisor()
        emisor.nombre = "LUIS QUINTANILLA BAUTISTA"
        emisor.rfc = "LQB790930A69"
        emisor.regimen_fiscal = "605"
       
        traslado.add_emisor(emisor)

        receptor = ObjectCfdiEntityFactory.create_cfdi_receptor()
        receptor.nombre = "PAPEL"
        receptor.rfc = "PAP830101CR3"
        receptor.regimen_fiscal = "601"
        receptor.domicilio_fiscal = "03200"
        receptor.uso_cfdi = "G01"
        
        traslado.add_receptor(receptor)

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

        traslado.add_concepto(concepto1)

        comprobante = ComprobanteBuilderDirector().build(traslado)


        print('*'*100)
        print(traslado.__dict__)
        print('*'*100)
        print(comprobante.__dict__)
        print(comprobante.Emisor.__dict__)
        print(comprobante.Receptor.__dict__)
        print(comprobante.Conceptos.__dict__)
        print('*'*100)
        print(comprobante.Conceptos.Concepto[0].__dict__)
        print('*'*100)

        print('*'*100)
        
        