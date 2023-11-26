from rest_framework import serializers
from .models import Product, ProductCharacteristics, Characteristic


class CharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characteristic
        fields = ['name', 'type', 'values']


class ProductCharacteristicsSerializer(serializers.ModelSerializer):
    characteristic = CharacteristicSerializer()

    class Meta:
        model = ProductCharacteristics
        fields = ['characteristic', 'value']


class ProductSerializer(serializers.ModelSerializer):
    product_characteristics = ProductCharacteristicsSerializer(source='productcharacteristics_set', many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['name', 'product_characteristics']
