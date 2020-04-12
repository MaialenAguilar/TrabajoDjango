from .models import Cliente, Componente, Categoria, Producto, Pedido
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, get_list_or_404

from django.views.generic import DetailView, ListView
from django.shortcuts import render

from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views import View
from .forms import PedidoForm, ProductoForm

# DEVUELVE EL LISTADO DE CLIENTES

#def clientes(request):
   #clientes = get_list_or_404(Cliente.objects.order_by('nombre_empresa'))
   #context = {'lista_clientes': clientes}
   #return render(request,'clientes.html',context)


class ClientesListView(ListView):
    model = Cliente
    template_name = 'clientes.html'
    queryset = Cliente.objects.order_by('nombre_empresa')
    context_object_name = 'lista_clientes'

    def get_context_data(self, **kwargs):
        context = super(ClientesListView, self).get_context_data(**kwargs)
        context['Titulo_pagina']='Listado de clientes'
        return context


#DEVUELVE DATOS DE UN CLIENTE

    #cliente = get_object_or_404(Cliente.objects.get(pk=cliente_id))
	#output = ', '.join([str(cliente.id) , cliente.nombre_empresa, str(cliente.telefono), cliente.persona_contacto])
	#return HttpResponse(output)

    #cliente = get_object_or_404(Cliente, pk=cliente_id)
    #context = {'cliente': cliente}
    #return render(request,'Datos_Cliente.html',context)

#def detalle_cliente(request, cliente_id):
	#cliente = Cliente.objects.get(pk=cliente_id)
	#output = ', '.join([str(cliente.id) , cliente.nombre_empresa, str(cliente.telefono), cliente.persona_contacto])
	#return HttpResponse(output)
class ClienteDetailView(DetailView):
	model = Cliente
	template_name = 'base.html'


# Devuelve el listado de componentes
def componentes(request):
    componentes = Componente.objects.order_by('nombre')
    output = ', '.join([d.nombre for d in componentes])
    return HttpResponse(output)

#devuelve los datos de un componente

def detalle_componentes(request, componente_id):
	componente = Componente.objects.get(pk=componente_id)
	output = ', '.join([componente.codigo_referencia, componente.nombre, componente.marca])
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
def detalle_productos(request, producto_id):
	producto =  Producto.objects.get(pk=producto_id)
	output = ', '.join([producto.nombre, producto.descripcion, str(producto.precio)])
	return HttpResponse(output)
#devuelve los datos de cada pedido


def detalle_pedidos(request, pedido_id):
	pedidos = Pedido.objects.get(pk=pedido_id)
	output = ', '.join([pedidos.identificador, str(pedidos.cliente)])
	return HttpResponse(output)

#def detalle_cliente(request, cliente_id):

   #cliente = get_object_or_404(Cliente, pk=cliente_id)
   #context = {'cliente': cliente}
   #return render(request,'Datos_Cliente.html',context)

class Detalle_ClienteDetailView(DetailView):
    model = Cliente
    template_name ='Datos_Cliente.html'

    def get_context_data(self, **kwargs):
        context= super(Detalle_ClienteDetailView, self).get_context_data(**kwargs)
        context['Titulo_pagina']='Datos de cliente'
        return context

# DEVUELVE LISTADO DE COMPONENTES

 #output = ', '.join([d.nombre for d in componentes])
    #return HttpResponse(output)

#def componentes(request):
   # componentes = get_list_or_404(Componente.objects.order_by('nombre'))
   # context={'lista_componentes': componentes}
   # return render(request, 'componentes.html' , context)

class ComponentesListView(ListView):

    model = Componente
    template_name = 'componentes.html'
    queryset = Componente.objects.order_by('nombre')
    context_object_name ='lista_componentes'

    def get_context_data(self, **kwargs):
        context = super(ComponentesListView, self).get_context_data(**kwargs)
        context['Titulo_pagina']='Listado de componentes'
        return context


#DEVUELVE LOS DATOS DE UN COMPONENTE

    #componente = Componente.objects.get(pk=componente_id)
	#output = ', '.join([componente.codigo_referencia, componente.nombre, componente.marca])
	#return HttpResponse(output)

#def detalle_componentes(request, componente_id):
    #componente= get_object_or_404(Componente, pk= componente_id)
    #context = {'componente':componente}
    #return render(request, 'Datos_Componente.html',context)

class Detalle_CompoentesDetailView(DetailView):

    model = Componente
    template_name = 'Datos_Componente.html'

    def get_context_data(self, **kwargs):
        context= super(Detalle_CompoentesDetailView, self).get_context_data(**kwargs)
        context['Titulo_pagina']= 'Datos del componente'
        return context

# DEVUELVE EL LISTADO DE CATEGORIAS

    #output = ', '.join([d.nombre for d in categorias])
    #return HttpResponse(output)

#def categorias(request):
    #categorias = get_list_or_404(Categoria.objects.order_by('nombre'))
    #context= {'lista_categorias':categorias}
    #return render(request, 'categorias.html',context)

class CategoriasListView(ListView):

    model = Categoria
    template_name ='categorias.html'
    queryset = Categoria.objects.order_by('nombre')
    context_object_name ='lista_categorias'

    def get_context_data(self, **kwargs):

        context= super(CategoriasListView, self).get_context_data(**kwargs)
        context['Titulo_pagina']='Listado de categorias'
        return context

# DEVUELVE EL LISTADO DE PRODUCTOS

    #output = ', '.join([d.nombre for d in productos])
    #return HttpResponse(output)

#def productos(request):
    #productos = get_list_or_404(Producto.objects.order_by('nombre'))
    #context= {'lista_productos':productos}
    #return render(request, 'productos.html',context)

class ProductosListView(ListView):

    model = Producto
    template_name ='productos.html'
    queryset = Producto.objects.order_by('nombre')
    context_object_name ='lista_productos'

    def get_context_data(self, **kwargs):

        context= super(ProductosListView, self).get_context_data(**kwargs)
        context['Titulo_pagina']='Listado de productos'
        return context

#DEVUELVE LOS DATOS DE CADA PRODUCTO

#producto =  Producto.objects.get(pk=producto_id)
	#output = ', '.join([producto.nombre, producto.descripcion, str(producto.precio)])
	#return HttpResponse(output)

#def detalle_productos(request, producto_id):
    #producto= get_object_or_404(Producto, pk= producto_id)
    #context= {'producto': producto}
    #return render(request, 'datos_producto.html', context)

class Detalle_ProductosDetailView(DetailView):

    model = Producto
    template_name = 'Datos_Producto.html'

    def get_context_data(self, **kwargs):

        context = super(Detalle_ProductosDetailView, self).get_context_data(**kwargs)
        context['Titulo_pagina'] = 'Datos del producto'
        return context

#DEVUELVE LISTA DE PEDIDOS

    #output = ', '.join([d.nombre for d in productos])
    #return HttpResponse(output)

#def pedidos(request):
    #pedidos = get_list_or_404(Pedido.objects.order_by('entregado'))
    #context= {'lista_pedidos':pedidos}
    #return render(request, 'pedidos.html',context)

class PedidosListView(ListView):

    model = Pedido
    template_name ='pedidos.html'
    queryset = Pedido.objects.order_by('entregado')
    context_object_name ='lista_pedidos'

    def get_context_data(self, **kwargs):

        context= super(PedidosListView, self).get_context_data(**kwargs)
        context['Titulo_pagina']='Listado de pedidos'
        return context

#DEVUELVE LOS DATOS DE CADA PEDIDO

#pedidos = Pedido.objects.get(pk=pedido_id)
	#output = ', '.join([pedidos.identificador, str(pedidos.cliente)])
	#return HttpResponse(output)

#def detalle_pedidos(request, pedido_id):
    #pedidos= get_object_or_404(Pedido,pk=pedido_id)
    #context= {'pedido': pedidos}
    #return render(request, 'Datos_Pedido.html', context)

class Detalle_PedidosDetailView(DetailView):

    model = Pedido
    template_name = 'Datos_Pedido.html'

    def get_context_data(self, **kwargs):

        context = super(Detalle_PedidosDetailView, self).get_context_data(**kwargs)
        context['Titulo_pagina']= 'Datos del pedido'
        return context

# CREAR FORMULARIO PEDIDO

class CrearPedidoView(View):

    def get(self, request, *args, **kwargs):
        form = PedidoForm()
        context = {
            'form': form,
            'titulo_pagina': 'Realizar un pedido'
        }
        return render(request, 'Crear_Pedido.html', context)

    def post(self, request, *args, **kwargs):
        form = PedidoForm(request.POST)
        if form.is_valid():
            # pedido = Pedido()
            # pedido.fecha_pedido = form.cleaned_data['fecha_pedido']
            # pedido.entregado = form.cleaned_data['entregado']
            # pedido.fecha_entrega = form.cleaned_data['fecha_entrega']
            # pedido.cliente = form.cleaned_data['cliente']
            # pedido.cantidad = form.cleaned_data['cantidad']
            # pedido.iva = form.cleaned_data['iva']
            # pedido.precio_total = form.cleaned_data['precio_total']
            # pedido.save()

            form.save()

            # Volvemos a la lista de noticias
            return redirect('pedidos')

        return render(request, 'Crear_Pedido.html', {'form': form})


    # CREAR FORMULARIO PRODUCTOS

class CrearProductoView(View):
    def get(self, request, *args, **kwargs):
        form = ProductoForm()
        context = {
            'form': form,
            'titulo_pagina': 'Insertar un producto'
        }
        return render(request, 'Insertar_Producto.html', context)

    def post(self, request, *args, **kwargs):
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()

            # Volvemos a la lista de productos
            return redirect('productos')

        return render(request, 'Insertar_Producto.html', {'form': form})

