from django.urls import path, include
from .views import CategoryAPIView, base_view

urlpatterns = [
    path('', CategoryAPIView.as_view()),
    path('', base_view, name='base'),
]
