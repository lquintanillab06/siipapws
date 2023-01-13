from .entity_sat import EntitySat



class EntitySatIngreso(EntitySat):

    def __init__(self):
        self.tipo = "I"
        super().__init__(self.tipo)