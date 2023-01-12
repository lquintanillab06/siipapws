
class CfdiConcepto():

    def __init__(self):
        self.clav_prod_serv = None
        self.cantidad = 0
        self.clave_unidad = None
        self.unidad = None
        self.descripcion = None
        self.valor_unitario = None
        self.descuento = None
        self.importe = None
        self.objeto_imp = None
        self.concepto_impuestos = {
            'traslados':[],
            'retenciones':[]
        }

    def add_traslado(self):
        pass

    def add_retencion(self):
        pass