from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter(trailing_slash = False)
#router.register(r'marcas',views.MarcaPruebaViewSet,basename="marcas")
#router.register(r'marcas',views.MarcaPruebaViewSet)
#router.register(r'marcas_test',views.MarcaTestViewSet)
router.register(r'marca_model',views.MarcaModelViewSet)

urlpatterns = [
    path('api/prueba', views.Prueba1.as_view(), name='prueba'),
    path('api/prueba_func', views.prueba_function, name='prueba_func'),
    path('api/lista', views.Listar.as_view(),name= "lista"),
    path('api/banco/<pk>', views.BancoRetrieve.as_view(),name= "banco"),
    path('api/banco1/<int:year>/<pk>', views.BancoRetrieve2.as_view(),name= "banco1"),
    path('api/banco2/<int:year>/<pk>', views.prueba_banco,name= "banco2"),
    path('api/listar_marcas', views.ListarMarcas.as_view(),name= "lista marcas"),
    path('api/', include(router.urls)), 
    path('api/test_parser/<filename>', views.ViewParser.as_view(),name= "parser"),
    path('api/test_ser', views.TestSerializer.as_view(),name= "serializer"),
]
