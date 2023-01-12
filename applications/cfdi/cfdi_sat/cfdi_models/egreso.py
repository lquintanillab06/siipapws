from .cfdi_entity import CfdiEntity



class Egreso(CfdiEntity):

    def __init__(self):
        self.tipo = "Egreso"
        super().__init__(self.tipo)