


class CfdiEmisor():
    
    def __init__(self,rfc,nombre,regimen_fiscal):
        self.nombre = nombre
        self.rfc = rfc
        self.regimen_fiscal = regimen_fiscal
        self.fact_atr_adquiriente = None
        