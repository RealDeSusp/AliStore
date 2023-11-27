from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product, ProductCharacteristics


class CustomProductAPIView(APIView):
    def get(self, request, category_id):
        products = Product.objects.filter(category__id=category_id)
        data = []

        for product in products:
            product_data = {
                'name': product.name,
                'characteristics': []
            }

            primary_characteristics = product.characteristics.filter(characteristic__category__type='Primary')

            for pc in primary_characteristics:
                characteristic_data = {
                    'name': pc.characteristic.name,
                    'value': pc.value
                }
                product_data['characteristics'].append(characteristic_data)

            data.append(product_data)

        return Response(data)


def base_view(request):
    return render(request, 'base.html')
