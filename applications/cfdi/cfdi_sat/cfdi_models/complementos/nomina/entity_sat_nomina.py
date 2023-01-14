from ....cfdi_models.entity_sat import EntitySat


class EntitySatNomina(EntitySat):
    
    def __init__(self):
        self.tipo = 'N'
        super().__init__(self.tipo)