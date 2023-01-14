
from .entity_sat import EntitySat



class EntitySatTraslado(EntitySat):

    def __init__(self):
        self.tipo = "T"
        super().__init__(self.tipo)