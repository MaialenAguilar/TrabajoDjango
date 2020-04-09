from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clientes/<int:cliente_id>/', views.detalle, name='detalle'),
    path('', views.componentes, name='componentes'),
    path('componentes/<int:componentes_id>/', views.detalle_componentes, name='detalle_componentes'),
    path('', views.Categoria, name='categorias'),
    path('', views.Producto, name='productos'),
    path('productos/<int:productos_id>/', views.detalle_productos, name='detalle_productos'),
    path('pedidos/<int:pedidos_id>/', views.detalle_pedidos, name='detalle_pedidos')
]