from django.urls import path
from . import views

urlpatterns = [

    #path('', views.clientes, name='clientes'),
    path('clientes/<int:pk>/', views.ClienteDetailView.as_view(), name='detalle_cliente'),
    path('componentes/', views.componentes, name='componentes'),
    path('componentes/<int:componente_id>/', views.detalle_componentes, name='detalle_componentes'),
    path('categorias/', views.categorias, name='categorias'),
    path('productos/', views.productos, name='productos'),
    path('productos/<int:producto_id>/', views.detalle_productos, name='detalle_productos'),
    path('pedidos/<int:pedido_id>/', views.detalle_pedidos, name='detalle_pedidos'),


   # path('', views.clientes, name='clientes'),
    path('clientes/', views.ClientesListView.as_view(), name='clientes'),
   # path('clientes/<int:cliente_id>/', views.detalle_cliente, name='detalle_cliente'),
    path('clientes/<int:pk>/', views.Detalle_ClienteDetailView.as_view(), name='detalle_cliente'),
   # path('componentes/', views.componentes, name='componentes'),
    path('componentes/', views.ComponentesListView.as_view(), name='componentes'),
   # path('componentes/<int:componente_id>/', views.detalle_componentes, name='detalle_componentes'),
    path('componentes/<int:pk>/', views.Detalle_CompoentesDetailView.as_view(), name='detalle_componentes'),
   # path('categorias/', views.categorias, name='categorias'),
    path('categorias/', views.CategoriasListView.as_view(), name='categorias'),
   # path('productos/', views.productos, name='productos'),
    path('productos/', views.ProductosListView.as_view(), name='productos'),
   # path('productos/<int:producto_id>/', views.detalle_productos, name='detalle_productos'),
     path('productos/<int:pk>/', views.Detalle_ProductosDetailView.as_view(), name='detalle_productos'),
   # path('pedidos/', views.pedidos, name='pedidos'),
    path('pedidos/', views.PedidosListView.as_view(), name='pedidos'),
   # path('pedidos/<int:pedido_id>/', views.detalle_pedidos, name='detalle_pedidos')
    path('pedidos/<int:pk>/', views.Detalle_PedidosDetailView.as_view(), name='detalle_pedidos'),
    path('pedidos/crear/', views.CrearPedidoView.as_view(), name='crear_pedido'),
    path('productos/crear/', views.CrearProductoView.as_view(), name='Insertar_Producto')



]
