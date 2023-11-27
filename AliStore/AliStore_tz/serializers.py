from rest_framework import serializers
from .models import Product, ProductCharacteristics


class ProductCharacteristicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCharacteristics
        fields = ('characteristic__name', 'value')


class ProductSerializer(serializers.ModelSerializer):
    characteristics = ProductCharacteristicsSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('name', 'characteristics')
