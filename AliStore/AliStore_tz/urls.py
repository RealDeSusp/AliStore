from django.urls import path
from .views import base_view, ProductListAPIView


urlpatterns = [
    path('', base_view, name='base'),
    path('products/<int:category_id>/', ProductListAPIView.as_view(), name='product-list'),
]
