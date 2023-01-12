from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .services.cfdi_services import CfdiServices

# Create your views here.

class Facturacion(APIView):

    def get(self, request):
        print("Ejecutando el metodo de facturacion !!!")

        service = CfdiServices()
        service.create_ingreso()
        return Response({"message": "request exitoso!!!"})


