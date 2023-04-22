from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from rest_framework import serializers
from .models import PostModel, CategoryModel, MenuModel, ImageModel, PageModel


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    featured_image = ImageSerializer()

    class Meta:
        model = PostModel
        fields = "__all__"


class PostListSerializer(serializers.ModelSerializer):
    featured_image = ImageSerializer()

    class Meta:
        model = PostModel
        fields = ("id", "featured_image", "title", "description", "slug")


class CategorySerializer(serializers.ModelSerializer):
    featured_image = ImageSerializer()

    class Meta:
        model = CategoryModel
        fields = "__all__"


class CategoryListSerializer(serializers.ModelSerializer):
    featured_image = ImageSerializer()

    class Meta:
        model = CategoryModel
        fields = ("id", "featured_image", "title", "description", "slug")


class PageSerializer(serializers.ModelSerializer):
    featured_image = ImageSerializer()

    class Meta:
        model = PageModel
        fields = "__all__"


class PageListSerializer(serializers.ModelSerializer):
    featured_image = ImageSerializer()

    class Meta:
        model = PostModel
        fields = ("id", "featured_image", "title", "description", "slug")


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuModel
        fields = "__all__"