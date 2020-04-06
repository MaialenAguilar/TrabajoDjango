from django import forms
from django.forms import ModelForm
from .models import Cliente, Categoria, Producto, Componente, Pedido
class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class ComponenteForm(ModelForm):
    class Meta:
        model = Componente
        fields = '__all__'

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class PedidoForm(ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'


