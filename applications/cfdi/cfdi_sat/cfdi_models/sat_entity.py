from abc import ABC, abstractmethod

class SatEntity(ABC):
    def __init__(self,tipo):
        self.tipo= tipo
        self.conceptos = []
        self.emisor = None
        self.receptor = None

  
    def create_emisor(self):
        pass

    def create_receptor(self):
        pass