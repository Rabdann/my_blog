from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from my_blog.serializers import ArticleSerializer, CategorySerializer

from .models import Category, Article


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (SearchFilter,)
    search_fields = ["title"]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["category"]
    search_fields = ["title"]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    
    # def get_queryset(self):
    #     print(self.request.GET)
    #     category = self.request.GET.get("category")
    #     search = self.request.GET.get("search")
    #     if search is not None:
    #         return Article.objects.filter(title__icontains=search)
    #     if category is None:
    #         return Article.objects.all()
    #     return Article.objects.filter(category=category)
