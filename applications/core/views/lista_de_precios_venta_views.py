
from django.shortcuts import render

from rest_framework.generics import (ListAPIView, 
                                    CreateAPIView, 
                                    RetrieveAPIView, 
                                    DestroyAPIView, 
                                    UpdateAPIView,
                                    RetrieveUpdateAPIView,
                                    RetrieveUpdateDestroyAPIView)

from rest_framework.decorators import api_view

from ..models import (ListaDePreciosVenta,)
from ..serializers import (ListaDePreciosVentaSerializer,)



class ListaDePreciosVentaList(ListAPIView):
    queryset = ListaDePreciosVenta.objects.all()
    serializer_class = ListaDePreciosVentaSerializer

class ListaDePreciosVentaCreate(CreateAPIView):
    serializer_class = ListaDePreciosVentaSerializer

class ListaDePreciosVentaRetrieve(RetrieveAPIView):
    serializer_class = ListaDePreciosVentaSerializer
    queryset = ListaDePreciosVenta.objects.filter()

class ListaDePreciosVentaDelete(DestroyAPIView):
    serializer_class = ListaDePreciosVentaSerializer
    queryset = ListaDePreciosVenta.objects.filter()

class ListaDePreciosVentaUpdate(UpdateAPIView):
    serializer_class = ListaDePreciosVentaSerializer
    queryset = ListaDePreciosVenta.objects.filter()

class ListaDePreciosVentaGetUpdate(RetrieveUpdateAPIView):
    serializer_class = ListaDePreciosVentaSerializer
    queryset = ListaDePreciosVenta.objects.filter()

class ListaDePreciosVentaGetUpdateDelete(RetrieveUpdateDestroyAPIView):
    serializer_class = ListaDePreciosVentaSerializer
    queryset = ListaDePreciosVenta.objects.filter()







