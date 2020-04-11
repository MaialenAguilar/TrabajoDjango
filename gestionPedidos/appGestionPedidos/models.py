from django.db import models

# Create your models here.
class Cliente(models.Model):
    cif = models.CharField(max_length=10)
    nombre_empresa = models.CharField(max_length=80)
    direccion = models.CharField(max_length=120)
    codigo_postal = models.IntegerField()
    Localidad = models.CharField(max_length=120)
    Provincia = models.CharField(max_length=60)
    telefono = models.IntegerField()
    email = models.EmailField()
    persona_contacto = models.CharField(max_length=120)

    def __str__(self):
        return f'{self.nombre_empresa}'


class Componente(models.Model):
    codigo_referencia = models.CharField(max_length=10)
    nombre = models.CharField(max_length=120)
    marca = models.CharField(max_length=80)

class Categoria(models.Model):
    nombre = models.CharField(max_length=60)
    def __str__(self):
        return f'{self.nombre}'

class Producto(models.Model):
    referencia = models.CharField(max_length=10)
    precio = models.FloatField()
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    componentes = models.ManyToManyField(Componente)

    def __str__(self):
        return f'{self.nombre}--> {self.categoria}'

class Pedido(models.Model):
    identificador = models.CharField(max_length=10)
    fecha_pedido = models.DateField()
    entregado =models.BooleanField(default=False)
    fecha_entrega = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ManyToManyField(Producto)
    cantidad = models.IntegerField()
    base_imponible = models.FloatField()
    iva = models.IntegerField(default=21)
    precio_total = models.FloatField()



    

