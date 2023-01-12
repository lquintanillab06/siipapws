from .cfdi_entity import CfdiEntity



class Ingreso(CfdiEntity):

    def __init__(self):
        self.tipo = "Ingreso"
        super().__init__(self.tipo)