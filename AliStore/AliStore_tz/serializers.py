from rest_framework import serializers
from .models import Product, Characteristic, ProductCharacteristics


class PrimaryCharacteristicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Characteristic
        fields = ('name', 'value')


class ProductSerializer(serializers.ModelSerializer):
    primary_characteristics = PrimaryCharacteristicSerializer(many=True, read_only=True, source='get_primary_characteristics')

    class Meta:
        model = Product
        fields = ('name', 'primary_characteristics')


class PaginatedProductSerializer(serializers.Serializer):
    count = serializers.IntegerField()
    next = serializers.CharField(allow_blank=True)
    previous = serializers.CharField(allow_blank=True)
    results = ProductSerializer(many=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        queryset = self.context['request'].data['results']
        serializer = ProductSerializer(instance=queryset, many=True)
        data['results'] = serializer.data
        return data
