from .entity_sat import EntitySat



class Egreso(EntitySat):

    def __init__(self):
        self.tipo = "E"
        super().__init__(self.tipo)