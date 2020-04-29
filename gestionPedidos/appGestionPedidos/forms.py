from django import forms
from django.forms import ModelForm, Widget
from .models import Cliente, Categoria, Producto, Componente, Pedido
class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            # Recorremos todos los campos del modelo para añadirle class="form-control
            self.fields[field].widget.attrs.update({'class': 'form-control'})

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
         #Establecemos el formato de input que deseamos
        widgets = {
            'componentes': forms.SelectMultiple()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            # Recorremos todos los campos del modelo para añadirle class="form-control
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class PedidoForm(ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'
        #Establecemos el formato de input que deseamos
        widgets = {
            'fecha_pedido': forms.SelectDateWidget,
            'fecha_entrega': forms.SelectDateWidget
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            # Recorremos todos los campos del modelo para añadirle class="form-control
            self.fields[field].widget.attrs.update({'class': 'form-control'})





