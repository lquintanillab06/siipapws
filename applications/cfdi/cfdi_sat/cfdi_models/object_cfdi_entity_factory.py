from .entity_sat_ingreso import EntitySatIngreso
from .entity_sat_egreso import EntitySatEgreso
from .entity_sat_traslado import EntitySatTraslado
from .cfdi_emisor import CfdiEmisor
from .cfdi_receptor import CfdiReceptor
from .cfdi_concepto import CfdiConcepto
from .cfdi_concepto_retencion import CfdiConceptoRetencion
from .cfdi_concepto_traslado import CfdiConceptoTraslado
from .cfdi_retencion import CfdiRetencion
from .cfdi_traslado import CfdiTraslado


class ObjectCfdiEntityFactory():

    @staticmethod
    def create_entity_sat_ingreso():
        return EntitySatIngreso()

    @staticmethod
    def create_entity_sat_egreso():
        return EntitySatEgreso()

    @staticmethod
    def create_entity_sat_traslado():
        return EntitySatTraslado()

    @staticmethod
    def create_cfdi_emisor():
        return CfdiEmisor()

    @staticmethod
    def create_cfdi_receptor():
        return CfdiReceptor()
    
    @staticmethod
    def create_cfdi_concepto():
        return CfdiConcepto()
    
    @staticmethod
    def create_cfdi_concepto_retencion():
        return CfdiConceptoRetencion()
    
    @staticmethod
    def create_cfdi_concepto_traslado():
        return CfdiConceptoTraslado()

    @staticmethod
    def create_cfdi_retencion():
        return CfdiRetencion()
    
    @staticmethod
    def create_cfdi_traslado():
        return CfdiTraslado()