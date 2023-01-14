
class CfdiConcepto():

    def __init__(self):
        self.clav_prod_serv = None
        self.no_identificacion = None
        self.cantidad = 0
        self.clave_unidad = None
        self.unidad = None
        self.descripcion = None
        self.valor_unitario = None
        self.descuento = None
        self.importe = None
        self.objeto_imp = None
        self.a_cuenta_terceros = None
        self.informacion_aduanera = None
        self.cuenta_predial = None
        self.concepto_impuestos = None


    def add_concepto_impuestos(self):
        self.concepto_impuestos = {
            'traslados':[],
            'retenciones':[]
        }

    def add_concepto_traslado(self,traslado):
        self.concepto_impuestos['traslados'].append(traslado)

    def add_concepto_retencion(self,retencion):
        self.concepto_impuestos['retenciones'].append(retencion)