from .comprobante_builder import ComprobanteBuilder
from .nomina_builder import NominaBuilder

class ComprobanteBuilderDirector():

    
    def build(self, entity):

        if entity.tipo == 'I':
            return self.build_ingreso(entity)

        if entity.tipo == 'E':
            return self.build_egreso(entity)
        
        if entity.tipo == 'T':
            return self.build_traslado(entity)

        if entity.tipo == 'N':
            return self.build_nomina(entity)

       

    def build_ingreso(self,entity):
        builder = (ComprobanteBuilder(entity)
        .build_comprobante()
        .build_emisor()
        .build_receptor()
        .build_conceptos()   
        )
        if entity.impuestos:
            builder.build_impuestos()

        comprobante = builder.get_comprobante()
        return comprobante

    def build_egreso(self,entity):
        builder = ComprobanteBuilder(entity)
        comprobante = (
        builder
        .build_comprobante()
        .build_emisor()
        .build_receptor()
        .build_conceptos()
        .build_impuestos()
        .build_relacionados()
        .get_comprobante()
        )

        return comprobante

    def build_traslado(self,entity):
        
        builder = ComprobanteBuilder(entity)
        comprobante = (
        builder
        .build_comprobante()
        .build_emisor()
        .build_receptor()
        .build_conceptos()
        .get_comprobante()
        )
        
        return comprobante


    def build_nomina(self,entity):

        builder = (ComprobanteBuilder(entity)
                    .build_comprobante()
                    .build_emisor()
                    .build_receptor()
                    .build_conceptos()
                    )

        nomina_builder = NominaBuilder('nomina')
        nomina_builder.get_nomina()
        comprobante = builder.get_comprobante()
        
        
        return comprobante


