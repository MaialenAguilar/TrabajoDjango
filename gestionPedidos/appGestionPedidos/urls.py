from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

#Esto sería necesario para trabajar con LoginView, pero como hemos importado anteriormente todas las Views, no sería necesario.
from django.contrib.auth.views import LoginView


urlpatterns = [
#______________________ _______________________
    path('login/', views.get_login, name='get_login'),
    path('register/', views.register, name='do_register'),
    path('logout/', views.do_logout, name='logout'),
    path('dologin/', views.do_login, name='do_login'),
 #______________________________________________________-
    path('', views.get_login, name='get_login'),
    path('home/', login_required(views.home), name='home'),
    path('clientes/', login_required(views.ClientesListView.as_view()), name='clientes'),
    # path('clientes/<int:cliente_id>/', views.detalle_cliente, name='detalle_cliente'),
    path('clientes/<int:pk>/', login_required(views.Detalle_ClienteDetailView.as_view()), name='detalle_cliente'),
    # path('componentes/', views.componentes, name='componentes'),
    path('componentes/', login_required(views.ComponentesListView.as_view()), name='componentes'),
    # path('componentes/<int:componente_id>/', views.detalle_componentes, name='detalle_componentes'),
    path('componentes/<int:pk>/', login_required(views.Detalle_CompoentesDetailView.as_view()), name='detalle_componentes'),
    path('categorias/', login_required(views.categorias), name='categorias'),
    # path('categorias/', views.CategoriasListView.as_view(), name='categorias'),
    path('productos/', login_required(views.ProductosListView.as_view()), name='productos'),
    path('conectores/', login_required(views.ConectoresListView.as_view()), name='conectores'),
    path('modulos/', login_required(views.ModulosListView.as_view()), name='modulos'),
    path('iluminacion/', login_required(views.IluminacionListView.as_view()), name='iluminacion'),
    path('ocio/', login_required(views.OcioListView.as_view()), name='ocio'),
    path('energia/', login_required(views.EnergiaListView.as_view()), name='energia'),
    path('seguridad/', login_required(views.SeguridadListView.as_view()), name='seguridad'),
    path('sonido/', login_required(views.SonidoListView.as_view()), name='sonido'),
    path('multimedia/', login_required(views.MultimediaListView.as_view()), name='multimedia'),
    path('hogar/', login_required(views.HogarListView.as_view()), name='hogar'),
    path('automovil/', login_required(views.AutomovilListView.as_view()), name='automovil'),
    # path('productos/<int:producto_id>/', views.detalle_productos, name='detalle_productos'),
    path('productos/<int:pk>/', login_required(views.Detalle_ProductosDetailView.as_view()), name='detalle_productos'),
    # path('pedidos/', views.pedidos, name='pedidos'),
    path('pedidos/', login_required(views.PedidosListView.as_view()), name='pedidos'),
    # path('pedidos/<int:pedido_id>/', views.detalle_pedidos, name='detalle_pedidos')
    path('pedidos/<int:pk>/', login_required(views.Detalle_PedidosDetailView.as_view()), name='detalle_pedidos'),
    path('pedidos/crear/', login_required(views.CrearPedidoView.as_view()), name='crear_pedido'),
    path('productos/crear/', login_required(views.CrearProductoView.as_view()), name='Insertar_Producto'),
    path('clientes/crear/', login_required(views.CrearClienteView.as_view()), name='Añadir_Cliente'),
    path('clientes/delete/<int:pk>/', login_required(views.Eliminar_ClientesDeleteView.as_view()), name='Eliminar_Cliente'),
    path('energia/delete/<int:pk>/', login_required(views.Eliminar_EnergiaDeleteView.as_view()), name='Eliminar_Energia'),
    path('hogar/delete/<int:pk>/', login_required(views.Eliminar_HogarDeleteView.as_view()), name='Eliminar_Hogar'),
    path('iluminacion/delete/<int:pk>/', login_required(views.Eliminar_IluminacionDeleteView.as_view()), name='Eliminar_Iluminacion'),
    path('modulos/delete/<int:pk>/', login_required(views.Eliminar_ModulosDeleteView.as_view()), name='Eliminar_Modulos'),
    path('multimedia/delete/<int:pk>/', login_required(views.Eliminar_MultimediaDeleteView.as_view()), name='Eliminar_Multimedia'),
    path('ocio/delete/<int:pk>/', login_required(views.Eliminar_OcioDeleteView.as_view()), name='Eliminar_Ocio'),
    path('seguridad/delete/<int:pk>/', login_required(views.Eliminar_SeguridadDeleteView.as_view()), name='Eliminar_Seguridad'),
    path('sonido/delete/<int:pk>/', login_required(views.Eliminar_SonidoDeleteView.as_view()), name='Eliminar_Sonido'),
    path('conectores/delete/<int:pk>/', login_required(views.Eliminar_ConectoresDeleteView.as_view()), name='Eliminar_Conectores'),
    path('automovil/delete/<int:pk>/', login_required(views.Eliminar_AutomovilDeleteView.as_view()), name='Eliminar_Automovil'),
    path('pedidos/delete/<int:pk>/', login_required(views.Eliminar_PedidoDeleteView.as_view()), name='Eliminar_Pedido')

]
