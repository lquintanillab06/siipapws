
class CfdiEmisor():
    
    def __init__(self,rfc,nombre,regimen_fiscal,domicilio_fiscal, uso_cfdi):
        self.nombre = nombre
        self.rfc = rfc
        self.regimen_fiscal = regimen_fiscal
        self.domicilio_fiscal = domicilio_fiscal
        self.uso_cfdi = uso_cfdi