from applications.cfdi.cfdi_sat.cfdi_models.entity_sat_ingreso import EntitySatIngreso

class CfdiServices():

    def __init__(self):
        self.ingreso  = EntitySatIngreso()

    def create_ingreso(self):
        print("Creando el ingreso")
