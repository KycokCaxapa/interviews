from rest_framework import serializers
from .models import Product, Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'name', 'video_link']


class ProductListSerializer(serializers.ModelSerializer):
    lesson_count = serializers.IntegerField(source='lesson_set.count', read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'start_date', 'cost', 'lesson_count']


class ProductDetailSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'start_date', 'cost', 'lessons']

