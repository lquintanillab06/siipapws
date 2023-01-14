from .entity_sat import EntitySat



class EntitySatIngreso(EntitySat):

    def __init__(self):
        self.tipo = "I"
        self.cuenta_predial = None
        self.informacion_aduanera = None
        super().__init__(self.tipo)

    def add_cuenta_predial(self):
        pass

    def add_informacion_aduanera(self):
        pass

