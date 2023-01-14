from .entity_sat import EntitySat



class EntitySatEgreso(EntitySat):

    def __init__(self):
        self.tipo = "E"
        self.tipo_relacion = None
        self.cfdi_relacionados = []

        super().__init__(self.tipo)


    def add_relacionado(self, uuid):
        self.cfdi_relacionados.append(uuid)