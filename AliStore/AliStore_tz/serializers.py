from rest_framework import serializers
from .models import Product, Characteristic


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = (Product, Characteristic)
        fields = Product.name
