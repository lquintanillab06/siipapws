from .comprobante import Comprobante
from .emisor import Emisor
from .receptor import Receptor
from .conceptos import Conceptos
from .concepto import Concepto
from .impuestos import Impuestos
from .traslados import Traslados
from .traslado import Traslado
from .retencion import Retencion
from .retenciones import Retenciones
from .complemento import Complemento
from .impuestos10 import Impuestos10
from .traslados10 import Traslados10
from .traslado10 import Traslado10
from .retenciones10 import Retenciones10 
from .retencion10 import Retencion10
from .informacionGlobal import InformacionGlobal
from .cfdiRelacionados import CfdiRelacionados
from .cfdiRelacionado import CfdiRelacionado
from .aCuentaTerceros import ACuentaTerceros
from .informacionAduanera import InformacionAduanera
from .cuentaPredial import CuentaPredial


class ObjectComprobanteFactory():

    @staticmethod
    def create_comprobante():
        return Comprobante()

    @staticmethod
    def create_emisor():
        return Emisor()

    @staticmethod
    def create_receptor():
        return Receptor()

    @staticmethod
    def create_conceptos():
        return Conceptos()

    @staticmethod
    def create_concepto():
        return Concepto()

    @staticmethod
    def create_impuestos():
        return Impuestos()

    @staticmethod
    def create_traslados():
        return Traslados()

    @staticmethod
    def create_traslado():
        return Traslado()

    @staticmethod
    def create_retencion():
        return Retencion()

    @staticmethod
    def create_retenciones():
        return Retenciones()

    @staticmethod
    def create_complemento():
        return Complemento()

    @staticmethod
    def create_impuestos10():
        return Impuestos10()

    @staticmethod
    def create_traslados10():
        return Traslados10()
    
    @staticmethod
    def create_traslado10():
        return Traslado10()

    @staticmethod
    def create_retenciones10():
        return Retenciones10()

    @staticmethod
    def create_retencion10():
        return Retencion10()

    @staticmethod
    def create_informacion_global():
        return InformacionGlobal()

    @staticmethod
    def create_cfdi_relacionados():
        return CfdiRelacionados()

    @staticmethod
    def create_cfdi_relacionado():
        return CfdiRelacionado()

    @staticmethod
    def create_acuenta_terceros():
        return ACuentaTerceros()

    @staticmethod
    def create_informacion_aduanera():
        return InformacionAduanera()

    @staticmethod
    def create_cuenta_predial():
        return CuentaPredial()

    
    