# Generated by Django 5.0.7 on 2024-07-23 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comida', '0004_datospedido_itemspedido_delete_pedido'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemspedido',
            old_name='envioId',
            new_name='DatosPedidoId',
        ),
    ]
