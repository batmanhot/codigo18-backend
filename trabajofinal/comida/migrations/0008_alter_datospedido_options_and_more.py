# Generated by Django 5.0.7 on 2024-07-26 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comida', '0007_alter_datospedido_options_alter_infonegocio_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='datospedido',
            options={'ordering': ['-id'], 'verbose_name': 'Atencion de Pedido', 'verbose_name_plural': 'Atencion de Pedidos'},
        ),
        migrations.AlterField(
            model_name='datospedido',
            name='pedidoatendido',
            field=models.BooleanField(null=True),
        ),
    ]