from .cfdi_ingreso_facade import CfdiIngresoFacade
from .cfdi_egreso_facade import CfdiEgresoFacade
from .cfdi_traslado_facade import CfdiTrasladoFacade
from .cfdi_nomina_facade import CfdiNominaFacade

class CfdiServices():

    def create_ingreso(self):
        print("Creando el Ingreso")
        facade = CfdiIngresoFacade()
        facade.create_cfdi_ingreso()
        
    def create_egreso(self):
            print("Creando el Egreso")
            facade = CfdiEgresoFacade()
            facade.create_cfdi_egreso()
 
    def create_traslado(self):
            print("Creando el Traslado")
            facade = CfdiTrasladoFacade()
            facade.create_cfdi_traslado()

    def create_nomina(self):
            print("Creando la Nomina")
            facade = CfdiNominaFacade()
            facade.create_cfdi_nomina()
 