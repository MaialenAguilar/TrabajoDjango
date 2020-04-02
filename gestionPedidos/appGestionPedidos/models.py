from django.db import models

# Create your models here.
class Cliente(models.Model):
    cif = models.Charfield(max_lengh=12)
    nombre_empresa = models.CharField(max_length=80)
    direccion = models.Charfield(max_length=120)
    codigo_postal = models.IntegerField()
    Localidad = models.CharField(max_length=120)
    Provincia = models.CharField(max_length=60)
    telefono = models.IntegerField()
    email = models.EmailField()
    persona_contacto = models.CharField(120)

class Componente(models.Model):
    codigo_referencia = models.IntegerField()
    nombre = models.CharField(max_length=120)
    marca = models.CharField(max_length=80)

class Categoría(models.Model):
    nombre = models.CharField(max_length=60)
    

