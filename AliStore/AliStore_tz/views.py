from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from .models import Product
from .serializers import PaginatedProductSerializer


class ProductListAPIView(ListAPIView):
    serializer_class = PaginatedProductSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        return Product.objects.filter(category=category_id)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


def base_view(request):
    return render(request, 'base.html')
