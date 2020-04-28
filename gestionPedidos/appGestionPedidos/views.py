from django.urls import reverse

from .models import Cliente, Componente, Categoria, Producto, Pedido
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, get_list_or_404


from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView,DeleteView, FormView, TemplateView, RedirectView
from django.views import View
from .forms import PedidoForm, ProductoForm, ClienteForm



# DEVUELVE UNA PANTALLA ESTATICA QUE ES LA DE INICIO

def home(request):
    return render(request, 'home.html')


# DEVUELVE EL LISTADO DE CLIENTES

class ClientesListView(ListView):
    model = Cliente
    template_name = 'clientes.html'
    queryset = Cliente.objects.order_by('nombre_empresa')
    context_object_name = 'lista_clientes'

    def get_context_data(self, **kwargs):
        context = super(ClientesListView, self).get_context_data(**kwargs)
        context['Titulo_pagina'] = 'Listado de clientes'
        return context


# DEVUELVE DATOS DE UN CLIENTE

class Detalle_ClienteDetailView(DetailView):
    model = Cliente
    template_name = 'Datos_Cliente.html'

    def get_context_data(self, **kwargs):
        context = super(Detalle_ClienteDetailView, self).get_context_data(**kwargs)
        context['Titulo_pagina'] = 'Datos de cliente'
        return context





# DEVUELVE LISTADO DE COMPONENTES

class ComponentesListView(ListView):
    model = Componente
    template_name = 'componentes.html'
    queryset = Componente.objects.order_by('nombre')
    context_object_name = 'lista_componentes'

    def get_context_data(self, **kwargs):
        context = super(ComponentesListView, self).get_context_data(**kwargs)
        context['Titulo_pagina'] = 'Listado de componentes'
        return context


# DEVUELVE LOS DATOS DE UN COMPONENTE

class Detalle_CompoentesDetailView(DetailView):
    model = Componente
    template_name = 'Datos_Componente.html'

    def get_context_data(self, **kwargs):
        context = super(Detalle_CompoentesDetailView, self).get_context_data(**kwargs)
        context['Titulo_pagina'] = 'Datos del componente'
        return context


# DEVUELVE EL LISTADO DE CATEGORIAS

# class CategoriasListView(ListView):
#    model = Categoria
#   template_name = 'categorias.html'
#   queryset = Categoria.objects.order_by('nombre')
#    context_object_name = 'lista_categorias'

#    def get_context_data(self, **kwargs):
#        context = super(CategoriasListView, self).get_context_data(**kwargs)
#        context['Titulo_pagina'] = 'Listado de categorias'
#        return context

def categorias(request):
    return render(request, 'categorias.html')


# DEVUELVE EL LISTADO DE PRODUCTOS, CATEGORIA CONECTORES

class ConectoresListView(ListView):
    model = Producto
    template_name = 'conectores.html'
    queryset = Producto.objects.filter(categoria__nombre='Conectores')
    context_object_name = 'lista_conectores'

    def get_context_data(self, **kwargs):
        context = super(ConectoresListView, self).get_context_data(**kwargs)
        context['Titulo_pagina'] = 'Listado de Conectores'
        return context


# DEVUELVE EL LISTADO DE PRODUCTOS, CATEGORIA MODULOS

class ModulosListView(ListView):
    model = Producto
    template_name = 'modulos.html'
    queryset = Producto.objects.filter(categoria__nombre='Modulos')
    context_object_name = 'lista_modulos'

    def get_context_data(self, **kwargs):
        context = super(ModulosListView, self).get_context_data(**kwargs)
        context['Titulo_pagina'] = 'Listado de productos'
        return context


# DEVUELVE LOS DATOS DE CADA PRODUCTO

class Detalle_ProductosDetailView(DetailView):
    model = Producto
    template_name = 'Datos_Producto.html'

    def get_context_data(self, **kwargs):
        context = super(Detalle_ProductosDetailView, self).get_context_data(**kwargs)
        context['Titulo_pagina'] = 'Datos del producto'
        return context




# DEVUELVE EL LISTADO DE PRODUCTOS, CATEGORIA ILUMINACION

class IluminacionListView(ListView):
    model = Producto
    template_name = 'iluminacion.html'
    queryset = Producto.objects.filter(categoria__nombre='Iluminacion')
    context_object_name = 'lista_iluminacion'

    def get_context_data(self, **kwargs):
        context = super(IluminacionListView, self).get_context_data(**kwargs)
        context['Titulo_pagina'] = 'Listado de productos'
        return context


# DEVUELVE EL LISTADO DE PRODUCTOS, CATEGORIA OCIO

class OcioListView(ListView):
    model = Producto
    template_name = 'ocio.html'
    queryset = Producto.objects.filter(categoria__nombre='Ocio')
    context_object_name = 'lista_ocio'

    def get_context_data(self, **kwargs):
        context = super(OcioListView, self).get_context_data(**kwargs)
        context['Titulo_pagina'] = 'Listado de productos'
        return context


# DEVUELVE EL LISTADO DE PRODUCTOS, CATEGORIA ENERGIA

class EnergiaListView(ListView):
    model = Producto
    template_name = 'energia.html'
    queryset = Producto.objects.filter(categoria__nombre='Energía')
    context_object_name = 'lista_energia'

    def get_context_data(self, **kwargs):
        context = super(EnergiaListView, self).get_context_data(**kwargs)
        context['Titulo_pagina'] = 'Listado de productos'
        return context


# DEVUELVE EL LISTADO DE PRODUCTOS, CATEGORIA SEGURIDAD

class SeguridadListView(ListView):
    model = Producto
    template_name = 'seguridad.html'
    queryset = Producto.objects.filter(categoria__nombre='Seguridad')
    context_object_name = 'lista_seguridad'

    def get_context_data(self, **kwargs):
        context = super(SeguridadListView, self).get_context_data(**kwargs)
        context['Titulo_pagina'] = 'Listado de productos'
        return context


# DEVUELVE EL LISTADO DE PRODUCTOS, CATEGORIA LUZ Y SONIDO

class SonidoListView(ListView):
    model = Producto
    template_name = 'sonido.html'
    queryset = Producto.objects.filter(categoria__nombre='Luz y Sonido')
    context_object_name = 'lista_sonido'

    def get_context_data(self, **kwargs):
        context = super(SonidoListView, self).get_context_data(**kwargs)
        context['Titulo_pagina'] = 'Listado de productos'
        return context


# DEVUELVE EL LISTADO DE PRODUCTOS, CATEGORIA MULTIMEDIA

class MultimediaListView(ListView):
    model = Producto
    template_name = 'multimedia.html'
    queryset = Producto.objects.filter(categoria__nombre='Multimedia')
    context_object_name = 'lista_multimedia'

    def get_context_data(self, **kwargs):
        context = super(MultimediaListView, self).get_context_data(**kwargs)
        context['Titulo_pagina'] = 'Listado de productos'
        return context


# DEVUELVE EL LISTADO DE PRODUCTOS, CATEGORIA HOGAR

class HogarListView(ListView):
    model = Producto
    template_name = 'hogar.html'
    queryset = Producto.objects.filter(categoria__nombre='Hogar')
    context_object_name = 'lista_hogar'

    def get_context_data(self, **kwargs):
        context = super(HogarListView, self).get_context_data(**kwargs)
        context['Titulo_pagina'] = 'Listado de productos'
        return context


# DEVUELVE EL LISTADO DE PRODUCTOS, CATEGORIA AUTOMOVIL

class AutomovilListView(ListView):
    model = Producto
    template_name = 'automovil.html'
    queryset = Producto.objects.filter(categoria__nombre='Automovil')
    context_object_name = 'lista_automovil'

    def get_context_data(self, **kwargs):
        context = super(AutomovilListView, self).get_context_data(**kwargs)
        context['Titulo_pagina'] = 'Listado de productos'
        return context


# DEVUELVE LISTA DE PEDIDOS

class PedidosListView(ListView):
    model = Pedido
    template_name = 'pedidos.html'
    queryset = Pedido.objects.order_by('entregado')
    context_object_name = 'lista_pedidos'

    def get_context_data(self, **kwargs):
        context = super(PedidosListView, self).get_context_data(**kwargs)
        context['Titulo_pagina'] = 'Listado de pedidos'
        return context


# DEVUELVE LOS DATOS DE CADA PEDIDO

class Detalle_PedidosDetailView(DetailView):
    model = Pedido
    template_name = 'Datos_Pedido.html'

    def get_context_data(self, **kwargs):
        context = super(Detalle_PedidosDetailView, self).get_context_data(**kwargs)
        context['Titulo_pagina'] = 'Datos del pedido'
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


# AÑADIR CLIENTE NUEVO

class CrearClienteView(View):
    def get(self, request, *args, **kwargs):
        form = ClienteForm()
        context = {
            'form': form,
            'titulo_pagina': 'Añadir cliente'
        }
        return render(request, 'Añadir_Cliente.html', context)

    def post(self, request, *args, **kwargs):
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()

            # Volvemos a la lista de clientes
            return redirect('clientes')

        return render(request, 'Añadir_Cliente.html', {'form': form})


class ProductosListView(ListView):
    model = Producto
    template_name = 'productos.html'
    queryset = Producto.objects.order_by('nombre')
    context_object_name = 'lista_productos'

    def get_context_data(self, **kwargs):
        context = super(ProductosListView, self).get_context_data(**kwargs)
        context['Titulo_pagina'] = 'Listado de productos'
        return context

# BORRA CLIENTE


class Eliminar_ClientesDeleteView(DeleteView):
    model = Cliente
    form_class= ClienteForm
    template_name = 'Eliminar_Cliente.html'


    def get_context_data(self, **kwargs):
     context = super(Eliminar_ClientesDeleteView, self).get_context_data(**kwargs)
     pk= self.kwargs.get('pk')
     cliente = Cliente.objects.get(id=pk)
     context.update({'cliente': cliente})
     return context

    def get_success_url(self):
        return reverse('clientes')



 # ELIMINAR PRODUCTO ENERGIA

class Eliminar_EnergiaDeleteView(DeleteView):
    model = Producto
    form_class= ProductoForm
    template_name = 'Eliminar_Energia.html'

    def get_context_data(self, **kwargs):
     context = super(Eliminar_EnergiaDeleteView, self).get_context_data(**kwargs)
     pk= self.kwargs.get('pk')
     producto = Producto.objects.get(id=pk)
     context.update({'producto': producto})
     return context

    def get_success_url(self):
        return reverse('energia')

# ELIMINAR PRODUCTO HOGAR

class Eliminar_HogarDeleteView(DeleteView):
    model = Producto
    form_class= ProductoForm
    template_name = 'Eliminar_Hogar.html'

    def get_context_data(self, **kwargs):
     context = super(Eliminar_HogarDeleteView, self).get_context_data(**kwargs)
     pk= self.kwargs.get('pk')
     producto = Producto.objects.get(id=pk)
     context.update({'producto': producto})
     return context

    def get_success_url(self):
        return reverse('hogar')

# ELIMINAR PRODUCTO ILUMINACION

class Eliminar_IluminacionDeleteView(DeleteView):
    model = Producto
    form_class= ProductoForm
    template_name = 'Eliminar_Iluminacion.html'

    def get_context_data(self, **kwargs):
     context = super(Eliminar_IluminacionDeleteView, self).get_context_data(**kwargs)
     pk= self.kwargs.get('pk')
     producto = Producto.objects.get(id=pk)
     context.update({'producto': producto})
     return context

    def get_success_url(self):
        return reverse('iluminacion')

# ELIMINAR PRODUCTO MODULOS

class Eliminar_ModulosDeleteView(DeleteView):
    model = Producto
    form_class= ProductoForm
    template_name = 'Eliminar_Modulos.html'

    def get_context_data(self, **kwargs):
     context = super(Eliminar_ModulosDeleteView, self).get_context_data(**kwargs)
     pk= self.kwargs.get('pk')
     producto = Producto.objects.get(id=pk)
     context.update({'producto': producto})
     return context

    def get_success_url(self):
        return reverse('modulos')

# ELIMINAR PRODUCTO MULTIMEDIA
class Eliminar_MultimediaDeleteView(DeleteView):
    model = Producto
    form_class= ProductoForm
    template_name = 'Eliminar_Multimedia.html'

    def get_context_data(self, **kwargs):
     context = super(Eliminar_MultimediaDeleteView, self).get_context_data(**kwargs)
     pk= self.kwargs.get('pk')
     producto = Producto.objects.get(id=pk)
     context.update({'producto': producto})
     return context

    def get_success_url(self):
        return reverse('multimedia')


# ELIMINAR PRODUCTO OCIO

class Eliminar_OcioDeleteView(DeleteView):
    model = Producto
    form_class= ProductoForm
    template_name = 'Eliminar_Ocio.html'

    def get_context_data(self, **kwargs):
     context = super(Eliminar_OcioDeleteView, self).get_context_data(**kwargs)
     pk= self.kwargs.get('pk')
     producto = Producto.objects.get(id=pk)
     context.update({'producto': producto})
     return context

    def get_success_url(self):
        return reverse('ocio')


# ELIMINAR PRODUCTO SEGURIDAD

class Eliminar_SeguridadDeleteView(DeleteView):
    model = Producto
    form_class= ProductoForm
    template_name = 'Eliminar_Seguridad.html'

    def get_context_data(self, **kwargs):
     context = super(Eliminar_SeguridadDeleteView, self).get_context_data(**kwargs)
     pk= self.kwargs.get('pk')
     producto = Producto.objects.get(id=pk)
     context.update({'producto': producto})
     return context

    def get_success_url(self):
        return reverse('seguridad')


# ELIMINAR PRODUCTO SONIDO

class Eliminar_SonidoDeleteView(DeleteView):
    model = Producto
    form_class= ProductoForm
    template_name = 'Eliminar_Sonido.html'

    def get_context_data(self, **kwargs):
     context = super(Eliminar_SonidoDeleteView, self).get_context_data(**kwargs)
     pk= self.kwargs.get('pk')
     producto = Producto.objects.get(id=pk)
     context.update({'producto': producto})
     return context

    def get_success_url(self):
        return reverse('sonido')

# ELIMINAR PRODUCTO CONECTORES

class Eliminar_ConectoresDeleteView(DeleteView):
    model = Producto
    form_class= ProductoForm
    template_name = 'Eliminar_Conectores.html'

    def get_context_data(self, **kwargs):
     context = super(Eliminar_ConectoresDeleteView, self).get_context_data(**kwargs)
     pk= self.kwargs.get('pk')
     producto = Producto.objects.get(id=pk)
     context.update({'producto': producto})
     return context

    def get_success_url(self):
        return reverse('conectores')

# ELIMINAR PRODUCTO AUTOMOVIL

class Eliminar_AutomovilDeleteView(DeleteView):
    model = Producto
    form_class= ProductoForm
    template_name = 'Eliminar_Automovil.html'

    def get_context_data(self, **kwargs):
     context = super(Eliminar_AutomovilDeleteView, self).get_context_data(**kwargs)
     pk= self.kwargs.get('pk')
     producto = Producto.objects.get(id=pk)
     context.update({'producto': producto})
     return context

    def get_success_url(self):
        return reverse('automovil')



