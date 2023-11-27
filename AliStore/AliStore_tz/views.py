from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Category
from .serializers import CategorySerializer
from rest_framework import generics


class CategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


def base_view(request):
    return render(request, 'base.html')
