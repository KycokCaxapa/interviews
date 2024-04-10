from django.urls import path
from .views import *

urlpatterns = [
    path('products/', ProductListView.as_view()),
    path('products/<int:pk>/', ProductDetailView.as_view()),
    path('lessons/<int:product_id>/', LessonByProductView.as_view()),
]
