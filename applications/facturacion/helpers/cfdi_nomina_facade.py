from applications.cfdi.cfdi_sat.cfdi_models.complementos.nomina.entity_sat_nomina import EntitySatNomina
from applications.cfdi.cfdi_sat.cfdi_models import ObjectCfdiEntityFactory
from applications.cfdi.cfdi_sat.builders.comprobante_builder_director import ComprobanteBuilderDirector
from datetime import datetime,date


class CfdiNominaFacade():

    def create_cfdi_nomina(self):
        nomina = EntitySatNomina()
        nomina.serie = "FAC"
        nomina.folio = "1000"
        nomina.forma_pago = "efectivo"
        nomina.tipo_cambio = 1.00
        nomina.subtotal = 84.00
        nomina.total = 100.00
        nomina.descuento = 1
        nomina.condiciones_de_pago = "PUE"
        nomina.exportacion = "02"
        nomina.metodo_pago = "PUE"
        nomina.lugar_de_expedicion = "02870"
        nomina.moneda = 'MXN'
        nomina.fecha = date(2023,1,13)

        emisor = ObjectCfdiEntityFactory.create_cfdi_emisor()
        emisor.nombre = "LUIS QUINTANILLA BAUTISTA"
        emisor.rfc = "LQB790930A69"
        emisor.regimen_fiscal = "605"
       
        nomina.add_emisor(emisor)

        receptor = ObjectCfdiEntityFactory.create_cfdi_receptor()
        receptor.nombre = "PAPEL"
        receptor.rfc = "PAP830101CR3"
        receptor.regimen_fiscal = "601"
        receptor.domicilio_fiscal = "03200"
        receptor.uso_cfdi = "G01"
        
        nomina.add_receptor(receptor)

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

        nomina.add_concepto(concepto1)

        comprobante = ComprobanteBuilderDirector().build(nomina)


        print('*'*100)
        print(nomina.__dict__)
        print('*'*100)
        print(comprobante.__dict__)
        print(comprobante.Emisor.__dict__)
        print(comprobante.Receptor.__dict__)
        print(comprobante.Conceptos.__dict__)
        print('*'*100)
        print(comprobante.Conceptos.Concepto[0].__dict__)
        print('*'*100)

        print('*'*100)
        
        