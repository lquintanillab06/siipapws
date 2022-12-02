from django.urls import path

from . import views

urlProductos =[ 
        # Rutas para Productos
        path('productos', views.ProductoList.as_view(), name= 'productos_list'),
        path('producto_create', views.ProductoCreate.as_view(), name= 'producto_create'),
        path('producto_retrieve/<pk>/', views.ProductoRetrieve.as_view(), name= 'producto_retrieve'),
        path('producto_delete/<pk>/', views.ProductoDelete.as_view(), name= 'producto_delete'),
        path('producto_update/<pk>/', views.ProductoUpdate.as_view(), name= 'producto_update'),
        path('producto_get_update/<pk>/', views.ProductoGetUpdate.as_view(), name= 'producto_get_update'),
        path('producto_get_update_delete/<pk>/', views.ProductoGetUpdateDelete.as_view(), name= 'producto_get_update_delete'),
    ]

urlClientes =[ 
        # Rutas para Clientes
        path('clientes', views.ClienteList.as_view(), name= 'clientes_list'),
        path('cliente_create', views.ClienteCreate.as_view(), name= 'cliente_create'),
        path('cliente_retrieve/<pk>/', views.ClienteRetrieve.as_view(), name= 'cliente_retrieve'),
        path('cliente_delete/<pk>/', views.ClienteDelete.as_view(), name= 'cliente_delete'),
        path('cliente_update/<pk>/', views.ClienteUpdate.as_view(), name= 'cliente_update'),
        path('cliente_get_update/<pk>/', views.ClienteGetUpdate.as_view(), name= 'cliente_get_update'),
        path('cliente_get_update_delete/<pk>/', views.ClienteGetUpdateDelete.as_view(), name= 'cliente_get_update_delete'),
        path('add_to_cliente_cliente_credito/<cliente>/', views.add_to_cliente_cliente_credito, name="add_to_cliente_cliente_credito")
    ]

urlClienteContactos = [
        path('cliente_contactos', views.ClienteContactosList.as_view(), name= 'cliente_contactoss_list'),
        path('cliente_contactos_create', views.ClienteContactosCreate.as_view(), name= 'cliente_contactos_create'),
        path('cliente_contactos_retrieve/<pk>/', views.ClienteContactosRetrieve.as_view(), name= 'cliente_contactos_retrieve'),
        path('cliente_contactos_delete/<pk>/', views.ClienteContactosDelete.as_view(), name= 'cliente_contactos_delete'),
        path('cliente_contactos_update/<pk>/', views.ClienteContactosUpdate.as_view(), name= 'cliente_contactos_update'),
        path('cliente_contactos_get_update/<pk>/', views.ClienteContactosGetUpdate.as_view(), name= 'cliente_contactos_get_update'),
        path('cliente_contactos_get_update_delete/<pk>/', views.ClienteContactosGetUpdateDelete.as_view(), name= 'cliente_contactos_get_update_delete'),
]

urlComunicacionEmpresa = [
        path('comunicacion_empresa', views.ComunicacionEmpresaList.as_view(), name= 'comunicacion_empresa_list'),
        path('comunicacion_empresa_create', views.ComunicacionEmpresaCreate.as_view(), name= 'comunicacion_empresa_create'),
        path('comunicacion_empresa_retrieve/<pk>/', views.ComunicacionEmpresaRetrieve.as_view(), name= 'comunicacion_empresa_retrieve'),
        path('comunicacion_empresa_delete/<pk>/', views.ComunicacionEmpresaDelete.as_view(), name= 'comunicacion_empresa_delete'),
        path('comunicacion_empresa_update/<pk>/', views.ComunicacionEmpresaUpdate.as_view(), name= 'comunicacion_empresa_update'),
        path('comunicacion_empresa_get_update/<pk>/', views.ComunicacionEmpresaGetUpdate.as_view(), name= 'comunicacion_empresa_get_update'),
        path('comunicacion_empresa_get_update_delete/<pk>/', views.ComunicacionEmpresaGetUpdateDelete.as_view(), name= 'comunicacion_empresa_get_update_delete'),
]


urlProveedor = [
        path('proveedores', views.ProveedorList.as_view(), name= 'proveedores_list'),
        path('proveedor_create', views.ProveedorCreate.as_view(), name= 'proveedor_create'),
        path('proveedor_retrieve/<pk>/', views.ProveedorRetrieve.as_view(), name= 'proveedor_retrieve'),
        path('proveedor_delete/<pk>/', views.ProveedorDelete.as_view(), name= 'proveedor_delete'),
        path('proveedor_update/<pk>/', views.ProveedorUpdate.as_view(), name= 'proveedor_update'),
        path('proveedor_get_update/<pk>/', views.ProveedorGetUpdate.as_view(), name= 'proveedor_get_update'),
        path('proveedor_get_update_delete/<pk>/', views.ProveedorGetUpdateDelete.as_view(), name= 'proveedor_get_update_delete'),
]

urlClienteCredito = [
        path('clientes_credito', views.ClienteCreditoList.as_view(), name= 'clientes_credito_list'),
        path('cliente_credito_create', views.ClienteCreditoCreate.as_view(), name= 'cliente_credito_create'),
        path('cliente_credito_retrieve/<pk>/', views.ClienteCreditoRetrieve.as_view(), name= 'cliente_credito_retrieve'),
        path('cliente_credito_delete/<pk>/', views.ClienteCreditoDelete.as_view(), name= 'cliente_credito_delete'),
        path('cliente_credito_update/<pk>/', views.ClienteCreditoUpdate.as_view(), name= 'cliente_credito_update'),
        path('cliente_credito_get_update/<pk>/', views.ClienteCreditoGetUpdate.as_view(), name= 'cliente_credito_get_update'),
        path('cliente_credito_get_update_delete/<pk>/', views.ClienteCreditoGetUpdateDelete.as_view(), name= 'cliente_credito_get_update_delete'),
]

urlClase = [
        path('clases', views.ClaseList.as_view(), name= 'clases_list'),
        path('clase_create', views.ClaseCreate.as_view(), name= 'clase_create'),
        path('clase_retrieve/<pk>/', views.ClaseRetrieve.as_view(), name= 'clase_retrieve'),
        path('clase_delete/<pk>/', views.ClaseDelete.as_view(), name= 'clase_delete'),
        path('clase_update/<pk>/', views.ClaseUpdate.as_view(), name= 'clase_update'),
        path('clase_get_update/<pk>/', views.ClaseGetUpdate.as_view(), name= 'clase_get_update'),
        path('clase_get_update_delete/<pk>/', views.ClaseGetUpdateDelete.as_view(), name= 'clase_get_update_delete'),
]

urlLinea = [
        path('lineas', views.LineaList.as_view(), name= 'lineas_list'),
        path('linea_create', views.LineaCreate.as_view(), name= 'linea_create'),
        path('linea_retrieve/<pk>/', views.LineaRetrieve.as_view(), name= 'linea_retrieve'),
        path('linea_delete/<pk>/', views.LineaDelete.as_view(), name= 'linea_delete'),
        path('linea_update/<pk>/', views.LineaUpdate.as_view(), name= 'linea_update'),
        path('linea_get_update/<pk>/', views.LineaGetUpdate.as_view(), name= 'linea_get_update'),
        path('linea_get_update_delete/<pk>/', views.LineaGetUpdateDelete.as_view(), name= 'linea_get_update_delete'),
]

urlMarca = [
        path('marcas', views.MarcaList.as_view(), name= 'marcas_list'),
        path('marca_create', views.MarcaCreate.as_view(), name= 'marca_create'),
        path('marca_retrieve/<pk>/', views.MarcaRetrieve.as_view(), name= 'marca_retrieve'),
        path('marca_delete/<pk>/', views.MarcaDelete.as_view(), name= 'marca_delete'),
        path('marca_update/<pk>/', views.MarcaUpdate.as_view(), name= 'marca_update'),
        path('marca_get_update/<pk>/', views.MarcaGetUpdate.as_view(), name= 'marca_get_update'),
        path('marca_get_update_delete/<pk>/', views.MarcaGetUpdateDelete.as_view(), name= 'marca_get_update_delete'),
]

urlBanco = [
        path('bancos', views.BancoList.as_view(), name= 'bancos_list'),
        path('banco_create', views.BancoCreate.as_view(), name= 'banco_create'),
        path('banco_retrieve/<pk>/', views.BancoRetrieve.as_view(), name= 'banco_retrieve'),
        path('banco_delete/<pk>/', views.BancoDelete.as_view(), name= 'banco_delete'),
        path('banco_update/<pk>/', views.BancoUpdate.as_view(), name= 'banco_update'),
        path('banco_get_update/<pk>/', views.BancoGetUpdate.as_view(), name= 'banco_get_update'),
        path('banco_get_update_delete/<pk>/', views.BancoGetUpdateDelete.as_view(), name= 'banco_get_update_delete'),
]

urlCuentaDeBanco = [
        path('cuentas_de_banco', views.CuentaDeBancoList.as_view(), name= 'cuentas_de_banco_list'),
        path('cuenta_de_banco_create', views.CuentaDeBancoCreate.as_view(), name= 'cuenta_de_banco_create'),
        path('cuenta_de_banco_retrieve/<pk>/', views.CuentaDeBancoRetrieve.as_view(), name= 'cuenta_de_banco_retrieve'),
        path('cuenta_de_banco_delete/<pk>/', views.CuentaDeBancoDelete.as_view(), name= 'cuenta_de_banco_delete'),
        path('cuenta_de_banco_update/<pk>/', views.CuentaDeBancoUpdate.as_view(), name= 'cuenta_de_banco_update'),
        path('cuenta_de_banco_get_update/<pk>/', views.CuentaDeBancoGetUpdate.as_view(), name= 'cuenta_de_banco_get_update'),
        path('cuenta_de_banco_get_update_delete/<pk>/', views.CuentaDeBancoGetUpdateDelete.as_view(), name= 'cuenta_de_banco_get_update_delete'),
]

urlProductoServicio = [
        path('productos_servicio', views.ProductoServicioList.as_view(), name= 'productos_servicio_list'),
        path('producto_servcio_create', views.ProductoServicioCreate.as_view(), name= 'producto_servcio_create'),
        path('producto_servcio_retrieve/<pk>/', views.ProductoServicioRetrieve.as_view(), name= 'producto_servcio_retrieve'),
        path('producto_servcio_delete/<pk>/', views.ProductoServicioDelete.as_view(), name= 'producto_servcio_delete'),
        path('producto_servcio_update/<pk>/', views.ProductoServicioUpdate.as_view(), name= 'producto_servcio_update'),
        path('producto_servcio_get_update/<pk>/', views.ProductoServicioGetUpdate.as_view(), name= 'producto_servcio_get_update'),
        path('producto_servcio_get_update_delete/<pk>/', views.ProductoServicioGetUpdateDelete.as_view(), name= 'producto_servcio_get_update_delete'),
]

urlDescuentoPorVolumen = [
        path('descuentos_por_volumen', views.DescuentoPorVolumenList.as_view(), name= 'descuentos_por_volumen_list'),
        path('descuento_por_volumens_create', views.DescuentoPorVolumenCreate.as_view(), name= 'descuento_por_volumens_create'),
        path('descuento_por_volumens_retrieve/<pk>/', views.DescuentoPorVolumenRetrieve.as_view(), name= 'descuento_por_volumens_retrieve'),
        path('descuento_por_volumens_delete/<pk>/', views.DescuentoPorVolumenDelete.as_view(), name= 'descuento_por_volumens_delete'),
        path('descuento_por_volumens_update/<pk>/', views.DescuentoPorVolumenUpdate.as_view(), name= 'descuento_por_volumens_update'),
        path('descuento_por_volumens_get_update/<pk>/', views.DescuentoPorVolumenGetUpdate.as_view(), name= 'descuento_por_volumens_get_update'),
        path('descuento_por_volumens_get_update_delete/<pk>/', views.DescuentoPorVolumenGetUpdateDelete.as_view(), name= 'descuento_por_volumens_get_update_delete'),
]

urlListaDePreciosVenta = [
        path('listas_de_precios_venta', views.ListaDePreciosVentaList.as_view(), name= 'listas_de_precios_venta_list'),
        path('lista_de_precios_venta_create', views.ListaDePreciosVentaCreate.as_view(), name= 'lista_de_precios_venta_create'),
        path('lista_de_precios_venta_retrieve/<pk>/', views.ListaDePreciosVentaRetrieve.as_view(), name= 'lista_de_precios_venta_retrieve'),
        path('lista_de_precios_venta_delete/<pk>/', views.ListaDePreciosVentaDelete.as_view(), name= 'lista_de_precios_venta_delete'),
        path('lista_de_precios_venta_update/<pk>/', views.ListaDePreciosVentaUpdate.as_view(), name= 'lista_de_precios_venta_update'),
        path('lista_de_precios_venta_get_update/<pk>/', views.ListaDePreciosVentaGetUpdate.as_view(), name= 'lista_de_precios_venta_get_update'),
        path('lista_de_precios_venta_get_update_delete/<pk>/', views.ListaDePreciosVentaGetUpdateDelete.as_view(), name= 'lista_de_precios_venta_get_update_delete'),
]

urlListaDePreciosVentaDet = [
        path('listas_de_precios_venta_det', views.ListaDePreciosVentaDetList.as_view(), name= 'listas_de_precios_venta_det_list'),
        path('lista_de_precios_venta_det_create', views.ListaDePreciosVentaDetCreate.as_view(), name= 'lista_de_precios_venta_det_create'),
        path('lista_de_precios_venta_det_retrieve/<pk>/', views.ListaDePreciosVentaDetRetrieve.as_view(), name= 'lista_de_precios_venta_det_retrieve'),
        path('lista_de_precios_venta_det_delete/<pk>/', views.ListaDePreciosVentaDetDelete.as_view(), name= 'lista_de_precios_venta_det_delete'),
        path('lista_de_precios_venta_det_update/<pk>/', views.ListaDePreciosVentaDetUpdate.as_view(), name= 'lista_de_precios_venta_det_update'),
        path('lista_de_precios_venta_det_get_update/<pk>/', views.ListaDePreciosVentaDetGetUpdate.as_view(), name= 'lista_de_precios_venta_det_get_update'),
        path('lista_de_precios_venta_det_get_update_delete/<pk>/', views.ListaDePreciosVentaDetGetUpdateDelete.as_view(), name= 'lista_de_precios_venta_det_get_update_delete'),
        path('lista_de_precios_venta_partidas/<lista>/partidas', views.ListaDePreciosVentaPartidasList.as_view(), name= 'lista_de_precios_venta_partidas_list'),
]

urlPreciosPorCliente = [
        path('precios_por_cliente', views.PreciosPorClienteList.as_view(), name= 'precios_por_cliente_list'),
        path('precios_por_cliente_create', views.PreciosPorClienteCreate.as_view(), name= 'precios_por_cliente_create'),
        path('precios_por_cliente_retrieve/<pk>/', views.PreciosPorClienteRetrieve.as_view(), name= 'precios_por_cliente_retrieve'),
        path('precios_por_cliente_delete/<pk>/', views.PreciosPorClienteDelete.as_view(), name= 'precios_por_cliente_delete'),
        path('precios_por_cliente_update/<pk>/', views.PreciosPorClienteUpdate.as_view(), name= 'precios_por_cliente_update'),
        path('precios_por_cliente_get_update/<pk>/', views.PreciosPorClienteGetUpdate.as_view(), name= 'precios_por_cliente_get_update'),
        path('precios_por_cliente_get_update_delete/<pk>/', views.PreciosPorClienteGetUpdateDelete.as_view(), name= 'precios_por_cliente_get_update_delete'),
]

urlPreciosPorClienteDet = [
        path('precios_por_cliente_det', views.PreciosPorClienteList.as_view(), name= 'precios_por_cliente_det_list'),
        path('precios_por_cliente_det_create', views.PreciosPorClienteCreate.as_view(), name= 'precios_por_cliente_det_create'),
        path('precios_por_cliente_det_retrieve/<pk>/', views.PreciosPorClienteRetrieve.as_view(), name= 'precios_por_cliente_det_retrieve'),
        path('precios_por_cliente_det_delete/<pk>/', views.PreciosPorClienteDelete.as_view(), name= 'precios_por_cliente_det_delete'),
        path('precios_por_cliente_det_update/<pk>/', views.PreciosPorClienteUpdate.as_view(), name= 'precios_por_cliente_det_update'),
        path('precios_por_cliente_det_get_update/<pk>/', views.PreciosPorClienteGetUpdate.as_view(), name= 'precios_por_cliente_det_get_update'),
        path('precios_por_cliente_det_get_update_delete/<pk>/', views.PreciosPorClienteGetUpdateDelete.as_view(), name= 'precios_por_cliente_det_get_update_delete'),
]

urlSocio = [
        path('socios', views.SocioList.as_view(), name= 'socios_list'),
        path('socio_create', views.SocioCreate.as_view(), name= 'socio_create'),
        path('socio_retrieve/<pk>/', views.SocioRetrieve.as_view(), name= 'socio_retrieve'),
        path('socio_delete/<pk>/', views.SocioDelete.as_view(), name= 'socio_delete'),
        path('socio_update/<pk>/', views.SocioUpdate.as_view(), name= 'socio_update'),
        path('socio_get_update/<pk>/', views.SocioGetUpdate.as_view(), name= 'socio_get_update'),
        path('socio_get_update_delete/<pk>/', views.SocioGetUpdateDelete.as_view(), name= 'socio_get_update_delete'),
]


urlpatterns  =  urlProductos + urlClientes + urlClienteContactos + urlComunicacionEmpresa + urlClienteCredito + urlClase + urlLinea + urlMarca

urlpatterns  += urlProveedor + urlBanco + urlCuentaDeBanco + urlProductoServicio + urlDescuentoPorVolumen + urlSocio

urlpatterns += urlListaDePreciosVenta + urlListaDePreciosVentaDet + urlPreciosPorCliente + urlPreciosPorClienteDet