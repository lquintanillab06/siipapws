from applications.cfdi.cfdi_sat.cfdi_models.ingreso import Ingreso

class CfdiServices():

    def __init__(self):
        self.ingreso  = Ingreso()

    def create_ingreso(self):
        print("Creando el ingreso")
