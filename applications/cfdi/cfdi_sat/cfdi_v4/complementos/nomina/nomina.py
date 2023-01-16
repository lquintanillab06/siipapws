


class Nomina():


    def __init__(self):

        #Emisor type Emisor - required
        self.Emisor = None
        #Receptor type Receptor - required
        self.Receptor = None
        #Percepciones type Percepciones 
        self.Percepciones = None
        #Deducciones type Deducciones
        self.Deducciones = None
        #OtrosPagos type OtrosPagos
        self.OtrosPagos = None
        #Incapacidades type Incapacidades
        self.Incapacidades = None
        #Version type String - required
        self.Version = None
        #TipoNomina type CTipoNomina - required
        self.TipoNomina = None
        #FechaPago type String - required
        self.FechaPago = None
        #FechaInicilaPago type String - required
        self.FechaInicialPago = None
        #FechaFinalPago type String - required
        self.FechaFinalPago = None
        #NumDiasPagados type Decimal - required
        self.NumDiasPagados = None
        #TotalPercepciones type Decimal
        self.TotalPercepciones = None
        #TotalDeducciones type - Decimal
        self.TotalDeducciones = None
        #TotalOtrosPagos type Decimal
        self.TotalOtrosPagos = None
