# Generated by Django 3.0.5 on 2020-04-22 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cif', models.CharField(max_length=10)),
                ('nombre_empresa', models.CharField(max_length=80)),
                ('direccion', models.CharField(max_length=120)),
                ('codigo_postal', models.IntegerField()),
                ('Localidad', models.CharField(max_length=120)),
                ('Provincia', models.CharField(max_length=60)),
                ('telefono', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('persona_contacto', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Componente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_referencia', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=120)),
                ('marca', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referencia', models.CharField(max_length=10)),
                ('precio', models.FloatField()),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appGestionPedidos.Categoria')),
                ('componentes', models.ManyToManyField(to='appGestionPedidos.Componente')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificador', models.CharField(max_length=10)),
                ('fecha_pedido', models.DateField()),
                ('entregado', models.BooleanField(default=False)),
                ('fecha_entrega', models.DateField()),
                ('cantidad', models.IntegerField()),
                ('base_imponible', models.FloatField()),
                ('iva', models.IntegerField(default=21)),
                ('precio_total', models.FloatField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appGestionPedidos.Cliente')),
                ('producto', models.ManyToManyField(to='appGestionPedidos.Producto')),
            ],
        ),
    ]
