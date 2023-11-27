from django.urls import path, include
from .views import ProductAPIView, base_view

urlpatterns = [
    path('', ProductAPIView.as_view()),
    path('', base_view, name='base'),
]
