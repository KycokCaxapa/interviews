from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Product, Lesson
from .serializers import *


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Фильтрация по продуктам, к которым пользователь имеет доступ
        user = self.request.user
        return Product.objects.filter(groups__students=user)


class LessonByProductView(generics.ListAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Получение списка уроков по конкретному продукту, к которому пользователь имеет доступ
        user = self.request.user
        product_id = self.kwargs.get('product_id')
        return Lesson.objects.filter(product__groups__students=user, product_id=product_id)
