from .models import Cliente

from django.shortcuts import render

# Devuelve el listado de clientes
def index(request):
    clientes = Cliente.objects.order_by('nombre_empresa')
    output = ', '.join([d.nombre_empresa for d in Cliente])
    return HttpResponse(output)

#devuelve los datos de un cliente
def detail(request, cliente_id):
	clientes = Clienteo.objects.get(pk=cliente_id)
	output = ', '.join([str(cliente_id), clientes.nombre_empresa, str(cliente.telefono)])
	return HttpResponse(output)
