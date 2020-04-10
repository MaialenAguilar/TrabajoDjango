from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.clientes, name='clientes'),
    path('clientes/<int:cliente_id>/', views.detalle_cliente, name='detalle_cliente'),
    path('componentes/', views.componentes, name='componentes'),
    path('componentes/<int:componente_id>/', views.detalle_componentes, name='detalle_componentes'),
    path('categorias/', views.categorias, name='categorias'),
    path('productos/', views.productos, name='productos'),
    path('productos/<int:producto_id>/', views.detalle_productos, name='detalle_productos'),
    path('pedidos/<int:pedido_id>/', views.detalle_pedidos, name='detalle_pedidos')
=======
    path('', views.index, name='index'),
    path('clientes/<int:clientes_id>/', views.detalle_cliente, name='detalle_cliente'),
    path('componentes', views.componentes, name='componentes'),
    path('componentes/<int:componentes_id>/', views.detalle_componentes, name='detalle_componentes'),
    path('', views.Categoria, name='categorias'),
    path('', views.Producto, name='productos'),
    path('productos/<int:productos_id>/', views.detalle_productos, name='detalle_productos'),
    path('pedidos/<int:pedidos_id>/', views.detalle_pedidos, name='detalle_pedidos')
>>>>>>> master
]
