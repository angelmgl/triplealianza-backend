from django.http import JsonResponse
from rest_framework import generics, pagination
from .models import (
    PostModel, 
    CategoryModel, 
    MenuModel, 
    PageModel,
    SlideModel,
    ImageModel
)
from bs4 import BeautifulSoup
from django.conf import settings
from django.shortcuts import get_object_or_404
from .serializers import (
    PostListSerializer,
    PostSerializer,
    CategorySerializer,
    CategoryListSerializer,
    PageSerializer,
    PageListSerializer,
    MenuSerializer,
    SlideSerializer,
    ImageSerializer
)

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
    queryset = PostModel.objects.all().order_by('-created_at')[:6]
    serializer_class = PostListSerializer


class PostListByCategory(generics.ListAPIView):
    serializer_class = PostListSerializer
    pagination_class = PostPagination

    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')
        category = get_object_or_404(CategoryModel, slug=category_slug)
        return PostModel.objects.filter(category=category)


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


class PageList(generics.ListAPIView):
    queryset = PageModel.objects.all().order_by('-created_at')
    serializer_class = PageListSerializer
    pagination_class = PostPagination


class PageDetail(generics.RetrieveAPIView):
    queryset = PageModel.objects.all()
    serializer_class = PageSerializer
    lookup_field = 'slug'

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        data = response.data
        data['content'] = add_domain_to_media_urls(data['content'])
        response.data = data
        return response


class CategoryList(generics.ListAPIView):
    queryset = CategoryModel.objects.all().order_by('-created_at')
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


class SlideList(generics.ListAPIView):
    queryset = SlideModel.objects.all()
    serializer_class = SlideSerializer


class ImageList(generics.ListAPIView):
    queryset = ImageModel.objects.all()
    serializer_class = ImageSerializer