from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics, pagination
from rest_framework.response import Response
from .models import PostModel, CategoryModel, MenuModel
from bs4 import BeautifulSoup
from django.conf import settings
from .serializers import PostListSerializer, PostSerializer, CategorySerializer, CategoryListSerializer, MenuSerializer

# A utility function to update all media URLs in the content field of a given object
def add_domain_to_media_urls(content: str) -> str:
    soup = BeautifulSoup(content, features="html.parser")
    domain = settings.DOMAIN_URL
    for img in soup.find_all('img'):
        if img['src'].startswith('/media/'):
            img['src'] = f"{domain}{img['src']}"
    return str(soup)


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

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        data = response.data
        data['content'] = add_domain_to_media_urls(data['content'])
        response.data = data
        return response


class CategoryList(generics.ListAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategoryListSerializer
    pagination_class = PostPagination


class CategoryDetail(generics.RetrieveAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        data = response.data
        data['content'] = add_domain_to_media_urls(data['content'])
        response.data = data
        return response


class MenuList(generics.ListAPIView):
    queryset = MenuModel.objects.all()
    serializer_class = MenuSerializer