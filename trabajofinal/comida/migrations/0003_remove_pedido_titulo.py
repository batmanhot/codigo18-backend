# Generated by Django 5.0.7 on 2024-07-23 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comida', '0002_pedido'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='titulo',
        ),
    ]
