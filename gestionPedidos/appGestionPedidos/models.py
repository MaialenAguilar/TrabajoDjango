from django.db import models

# Create your models here.
class Cliente(models.Model):
    cif = models.Charfield(max_lengh=12)
    nombre_empresa = models.CharField(max_length=80)
    direccion = models.Charfield(max_length=120)

