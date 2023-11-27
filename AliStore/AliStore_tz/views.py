from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product, Characteristic
from .serializers import ProductSerializer
from rest_framework import generics


class ProductAPIView(generics.ListAPIView):
    Product_query = Product.objects.all()
    Characteristic_query = Characteristic.objects.all()
    queryset = list(chain(Product_query, Product_query))
    serializer_class = ProductSerializer


def base_view(request):
    return render(request, 'base.html')
