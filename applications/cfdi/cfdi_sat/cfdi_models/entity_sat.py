from abc import ABC, abstractmethod

from .cfdi_emisor import CfdiEmisor

class EntitySat(ABC):
    def __init__(self,tipo):

        self.tipo= tipo
        self.version_cfdi = '4.0'
        self.serie = None
        self.folio = None
        self.fecha = None
        self.forma_pago = None
        self.no_certificado = None
        self.certificado = None
        self.subtotal = None
        self.descuento = None
        self.condiciones_de_pago = None
        self.exportacion = None
        self.metodo_pago = None
        self.lugar_de_expedicion = None
        self.emisor = None
        self.receptor = None
        self.conceptos = []
        self.impuestos = {
            'total_impuestos_retenidos': None,
            'total_impuestos_trasladados': None,
            'retenciones': [],
            'traslados': [],
        }
  
    def add_emisor(self,emisor):
       self.emisor = emisor

    def add_receptor(self, receptor):
        self.receptor = receptor

    def add_concepto(self,concepto):
        self.conceptos.append(concepto)

    def add_impuestos(self,total_impuestos_retenidos = 0, total_impuestos_trasladados = 0):

        self.impuestos['total_impuestos_retenidos'] = total_impuestos_retenidos
        self.impuestos['total_impuestos_trasladados'] = total_impuestos_trasladados


    def add_retencion(self, retencion):
        self.impuestos['retenciones'].append(retencion)

    def add_traslado(self, traslado):
        self.impuestos['traslados'].append(traslado) 

