from ..cfdi_v4.comprobante import ObjectComprobanteFactory
from applications.commons.utils.dateUtils import DateUtils
from ..cfdi_utils.cfdi_moneda_utils import MonedaUtils


class ComprobanteBuilder():

    def __init__(self,cfdi_entity):
        self.comprobante = ObjectComprobanteFactory.create_comprobante()
        self.entity = cfdi_entity

    def get_comprobante(self):
        return self.comprobante

    def build_comprobante(self):
        self.comprobante.Version = self.entity.version_cfdi
        self.comprobante.TipoDeComprobante = self.entity.tipo
        self.comprobante.Fecha = DateUtils.getNowFormatted()
        self.comprobante.SubTotal = 0.00
        self.comprobante.Moneda = MonedaUtils.monedaResolve(self.entity.moneda)
        self.comprobante.Total = 0.00
        self.comprobante.Exportacion = self.entity.exportacion
        self.comprobante.LugarExpedicion = self.entity.lugar_de_expedicion
        self.comprobante.NoCertificado = self.entity.no_certificado
        self.comprobante.Certificado = self.entity.certificado  
        if self.entity.serie:
            self.comprobante.Serie = self.entity.serie
        if self.entity.folio:
            self.comprobante.Folio = self.entity.folio       
        if self.entity.forma_pago:
            self.comprobante.FormaPago = self.entity.forma_pago
        if self.entity.descuento:
            self.comprobante.Descuento = self.entity.descuento
        if self.entity.tipo_cambio:
            self.comprobante.TipoCambio = self.entity.tipo_cambio
        if self.entity.metodo_pago:
             self.comprobante.MetodoPago = self.entity.metodo_pago
        if self.entity.condiciones_de_pago:
            self.comprobante.CondicionesDePago = self.entity.condiciones_de_pago
        if self.entity.confirmacion:
            self.comprobante.Confirmacion = self.entity.confirmacion
        
        return self

    def build_emisor(self):
        emisor = ObjectComprobanteFactory.create_emisor()
        emisor.Rfc = self.entity.emisor.rfc
        emisor.Nombre = self.entity.emisor.nombre
        emisor.RegimenFiscal = self.entity.emisor.regimen_fiscal
        if self.entity.emisor.fact_atr_adquiriente :
            emisor.FacAtrAdquirente = self.entity.emisor.fact_atr_adquiriente
        self.comprobante.Emisor = emisor
        return self

    def build_receptor(self):
        receptor = ObjectComprobanteFactory.create_receptor()
        receptor.Nombre = self.entity.receptor.nombre
        receptor.Rfc = self.entity.receptor.rfc
        receptor.RegimenFiscalReceptor = self.entity.receptor.regimen_fiscal
        receptor.DomicilioFiscalReceptor = self.entity.receptor.domicilio_fiscal
        receptor.UsoDeCfdi = self.entity.receptor.uso_cfdi

        if self.entity.receptor.residencia_fiscal:
            receptor.ResidenciaFiscal = self.entity.receptor.residencia_fiscal

        if self.entity.receptor.num_reg_id_trib:
            receptor.NumRegIdTrib = self.entity.receptor.num_reg_id_trib

        self.comprobante.Receptor = receptor

        return self

    def build_informacion_global(self):
        informacion_global = ObjectComprobanteFactory.create_informacion_global()
        informacion_global.Periodicidad = self.entity.periodicidad
        informacion_global.Meses = self.entity.meses
        informacion_global.Año = self.entity.año
        self.comprobante.InformacionGlobal =  informacion_global
        return self

    def build_relacionados(self):

        if self.entity.cfdi_relacionados:
            relacionados = ObjectComprobanteFactory.create_cfdi_relacionados()
            relacionados.TipoRelacion = self.entity.tipo_relacion

            for cfdi_relacionado in self.entity.cfdi_relacionados:
                relacionado = ObjectComprobanteFactory.create_cfdi_relacionado()
                relacionado.UUID = cfdi_relacionado
                relacionados.CfdiRelacionado.append(relacionado)
            
            self.comprobante.CfdiRelacionados = relacionados

            return self

    def build_conceptos(self):
    
        conceptos = ObjectComprobanteFactory.create_conceptos()

        for cfdi_concepto in self.entity.conceptos:
            concepto = ObjectComprobanteFactory.create_concepto()
            concepto.ClaveProdServ = cfdi_concepto.clav_prod_serv
            concepto.NoIdentificacion = cfdi_concepto.no_identificacion
            concepto.Cantidad = cfdi_concepto.cantidad
            concepto.ClaveUnidad = cfdi_concepto.clave_unidad
            concepto.Descripcion = cfdi_concepto.descripcion
            concepto.ValorUnitario = cfdi_concepto.valor_unitario
            concepto.Importe = cfdi_concepto.importe
            concepto.ObjetoImp = cfdi_concepto.objeto_imp

            if cfdi_concepto.unidad:   
                concepto.Unidad = cfdi_concepto.unidad

            if cfdi_concepto.descuento:
                concepto.Descuento = cfdi_concepto.descuento

            if cfdi_concepto.concepto_impuestos:
                concepto.Impuestos = self.build_concepto_impuestos(cfdi_concepto.concepto_impuestos)

            if cfdi_concepto.a_cuenta_terceros:
                concepto.ACuentaTerceros = self.build_a_cuenta_terceros(cfdi_concepto.a_cuenta_terceros)

            if cfdi_concepto.informacion_aduanera:
                concepto.InformacionAduanera = self.build_informacion_aduanera(cfdi_concepto.informacion_aduanera)

            if cfdi_concepto.cuenta_predial:
                concepto.CuentaPredial = self.build_cuenta_predial(cfdi_concepto.cuenta_predial)

            conceptos.Concepto.append(concepto)
      
        self.comprobante.Conceptos = conceptos
        return self

    def  build_concepto_impuestos(self,concepto_impuestos):
      
        impuestos = ObjectComprobanteFactory.create_impuestos()
        
        if concepto_impuestos['traslados']:
            traslados = ObjectComprobanteFactory.create_traslados()
            for concepto_traslado in concepto_impuestos['traslados']:
                traslado = ObjectComprobanteFactory.create_traslado()
                traslado.Base = concepto_traslado.base
                traslado.Impuesto = concepto_traslado.impuesto
                traslado.TipoFactor = concepto_traslado.tipo_factor
                traslado.TasaOCuota = concepto_traslado.tasa_cuota
                traslado.Importe = concepto_traslado.importe
                traslados.Traslado.append(traslado)
            impuestos.Traslados = traslados

        if concepto_impuestos['retenciones']:
            retenciones = ObjectComprobanteFactory.create_retenciones()
            for concepto_retencion in concepto_impuestos['retenciones']:
                retencion = ObjectComprobanteFactory.create_retencion()
                retencion.Base = concepto_retencion.base
                retencion.Impuesto = concepto_retencion.impuesto
                retencion.TipoFactor = concepto_retencion.tipo_factor
                retencion.TasaOCuota = concepto_retencion.tasa_cuota
                retencion.Importe = concepto_retencion.importe
                retenciones.Retencion.append(retencion)
            impuestos.Retenciones = retenciones

        return impuestos                

    def build_a_cuenta_terceros(self,acuenta):
        acuenta_terceros = ObjectComprobanteFactory.create_acuenta_terceros()
        acuenta_terceros.RfcACuentaTerceros = acuenta.rfc
        acuenta_terceros.NombreAcuentaTerceros = acuenta.nombre
        acuenta_terceros.RegimenFiscalACuentaTerceros = acuenta.regimen_fiscal
        acuenta_terceros.DomiciliioFiscalACuentaTerceros = acuenta.domicilio_fiscal
        return acuenta_terceros

    def build_informacion_aduanera(self,informacion):
        informacion_aduanera = ObjectComprobanteFactory.create_informacion_aduanera()
        informacion_aduanera.NumeroPedimento = informacion
        return informacion_aduanera

    def build_cuenta_predial(self,cuenta):
        cuenta_predial = ObjectComprobanteFactory.create_cuenta_predial()
        cuenta_predial.Numero = cuenta.numero

        return cuenta_predial


    def build_impuestos(self):

        impuestos = ObjectComprobanteFactory.create_impuestos10()
        impuestos.TotalImpuestosRetenidos = self.entity.impuestos['total_impuestos_retenidos']
        impuestos.TotalImpuestosTrasladados = self.entity.impuestos['total_impuestos_trasladados']
        if self.entity.impuestos['retenciones']:
            retenciones = ObjectComprobanteFactory.create_retenciones10()
            for cfdi_retencion in self.entity.impuestos['retenciones']:
                retencion = ObjectComprobanteFactory.create_retencion10()
                retencion.Impuesto = cfdi_retencion.impuesto
                retencion.Importe = cfdi_retencion.importe
                
                retenciones.Retencion.append(retencion)

            impuestos.Retenciones = retenciones
        if self.entity.impuestos['traslados']:
            traslados = ObjectComprobanteFactory.create_traslados10()
            for cfdi_traslado in self.entity.impuestos['traslados']:
                traslado = ObjectComprobanteFactory.create_traslado10()
                traslado.Base = cfdi_traslado.base
                traslado.Impuesto = cfdi_traslado.impuesto
                traslado.TipoFactor = cfdi_traslado.tipo_factor
                traslado.TasaOCuota = cfdi_traslado.tasa_cuota
                traslado.Importe = cfdi_traslado.importe

                traslados.Traslado.append(traslado)
            impuestos.Traslados = traslados
        self.comprobante.Impuestos = impuestos
        return self

    def build_complemento(self,complemento):
        self.comprobante.Complemento = complemento

    def build_adenda(self,adenda):
        self.comprobante.Adenda = adenda

    



            










    

        

        



        


        