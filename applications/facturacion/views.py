from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .helpers.cfdi_services import CfdiServices



# Create your views here.

class Facturacion(APIView):

    def __init__(self)  :
       pass

    def get(self, request):
        print("Ejecutando el metodo de facturacion !!!") 
        service = CfdiServices()
        #service.create_ingreso()
        #service.create_egreso()
        #service.create_traslado()
        service.create_nomina()

        return Response({"message": "request exitoso1!!!"})


