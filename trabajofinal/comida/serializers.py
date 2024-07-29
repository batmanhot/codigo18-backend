from rest_framework import serializers
from .models import Producto, InfoNegocio, DatosPedido, ItemsPedido

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = (
            'id',
            'titulo',
            'descripcion',
            'precio',
            'imagen'
        )

class InfoNegocioSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoNegocio
        fields = '__all__'


class DatosPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatosPedido
        fields = '__all__'

class ItemsPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemsPedido
        fields = '__all__'