from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from my_blog.serializers import ArticleSerializer, CategorySerializer

from .models import Category, Article


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
