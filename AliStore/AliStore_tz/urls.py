from django.urls import path, include
from .views import CustomProductAPIView, base_view

urlpatterns = [
    path('api/products/<int:category_id>/', CustomProductAPIView.as_view(), name='custom-product-list'),
    path('', base_view, name='base'),
]
