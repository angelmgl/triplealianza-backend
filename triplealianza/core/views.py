from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics, pagination
from .models import PostModel, CategoryModel, MenuModel
from .serializers import PostListSerializer, PostSerializer, CategorySerializer, CategoryListSerializer, MenuSerializer

class PostPagination(pagination.PageNumberPagination):
    page_size = 20


def welcome(request):
    response = {
        'title': 'Welcome to triplealianza.com.py!',
        'description': 'Hey! We are under construction right now, but don\'t worry! We are working hard to get everything ready soon and provide you with the best content! Thanks for your patience and see you soon! 🚧👷‍♂️👷‍♀️'
    }
    return JsonResponse(response)


class PostList(generics.ListAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostListSerializer
    pagination_class = PostPagination


class PostDetail(generics.RetrieveAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'


class CategoryList(generics.ListAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategoryListSerializer
    pagination_class = PostPagination


class CategoryDetail(generics.RetrieveAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'


class MenuList(generics.ListAPIView):
    queryset = MenuModel.objects.all()
    serializer_class = MenuSerializer