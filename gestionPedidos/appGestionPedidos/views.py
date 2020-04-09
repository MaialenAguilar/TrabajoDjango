from .models import Cliente
from django.http import HttpResponse
from django.shortcuts import render

# Devuelve el listado de clientes
def index(request):
    clientes = Cliente.objects.order_by('nombre_empresa')
    output = ', '.join([d.nombre_empresa for d in clientes])
    return HttpResponse(output)

#devuelve los datos de un cliente
def detalle(request, clientes_id):
	clientes = Cliente.objects.get(pk=clientes_id)
	output = ', '.join([str(clientes_id), Cliente.nombre_empresa, str(Cliente.telefono), Cliente.persona_contacto])
	return HttpResponse(output)

# Devuelve el listado de componentes
def index(request):
    componentes = Componente.objects.order_by('nombre_componente')
    output = ', '.join([d.nombre_empresa for d in clientes])
    return HttpResponse(output)
