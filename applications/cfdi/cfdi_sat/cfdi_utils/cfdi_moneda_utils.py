from ..cfdi_v4.catalogos.c_moneda import CMoneda

class MonedaUtils():
    
    @classmethod
    def monedaResolve(self, monedaCode):
        if monedaCode == 'MXN':
            return CMoneda.MXN
        if monedaCode == 'USD':
            return CMoneda.USD