from .sat_entity import SatEntity



class Ingreso(SatEntity):

    def __init__(self):
        self.tipo = "Ingreso"
        super().__init__(self.tipo)