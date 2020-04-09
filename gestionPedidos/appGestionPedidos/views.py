from .models import Cliente, Componente, Categoria, Producto, Pedido
from django.http import HttpResponse
from django.shortcuts import render

# Devuelve el listado de clientes
def index(request):
    clientes = Cliente.objects.order_by('nombre_empresa')
    output = ', '.join([d.nombre_empresa for d in clientes])
    return HttpResponse(output)

#devuelve los datos de un cliente
def detalle_cliente(request, clientes_id):
	clientes = Cliente.objects.get(pk=clientes_id)
	output = ', '.join([str(clientes_id), Cliente.nombre_empresa, str(Cliente.telefono), Cliente.persona_contacto])
	return HttpResponse(output)

# Devuelve el listado de componentes
def componentes(request):
    componentes = Componente.objects.order_by('nombre')
    output = ', '.join([d.nombre for d in componentes])
    return HttpResponse(output)

#devuelve los datos de un componente
def detalle_componentes(request, componenetes_id):
	componentes = Cliente.objects.get(pk=componenetes_id)
	output = ', '.join([Componente.codigo_referencia, Componente.nombre, Componente.marca])
	return HttpResponse(output)

# Devuelve el listado de categorias
def categorias(request):
    categorias = Categoria.objects.order_by('nombre')
    output = ', '.join([d.nombre for d in categorias])
    return HttpResponse(output)

# Devuelve el listado de productos
def productos(request):
    productos = Producto.objects.order_by('nombre')
    output = ', '.join([d.nombre for d in productos])
    return HttpResponse(output)

#devuelve los datos de cada producto
def detalle_productos(request, productos_id):
	productos = Producto.objects.get(pk=productos_id)
	output = ', '.join([Producto.nombre, Producto.descripcion, str(Producto.precio)])
	return HttpResponse(output)

#devuelve los datos de cada pedido
def detalle_pedidos(request, pedidos_id):
	pedidos = Pedido.objects.get(pk=pedidos_id)
	output = ', '.join([Pedido.identificador, Pedido.cliente])
	return HttpResponse(output)