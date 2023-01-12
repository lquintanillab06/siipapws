from abc import ABC, abstractmethod

class CfdiEntity(ABC):
    def __init__(self,tipo):
        self.tipo= tipo
        self.conceptos = []
        self.emisor = None
        self.receptor = None
        self.impuestos = {
            'total_impuestos_retenidos': None,
            'total_impuestos_traslados': None,
            'retenciones': [],
            'traslados': [],

        }

  
    def create_emisor(self):
        pass

    def create_receptor(self):
        pass

    def add_concepto(self):
        pass

    def add_retencion(self):
        pass

    def add_traslado(self):
        pass 

