from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from rest_framework import serializers
from .models import PostModel, CategoryModel, MenuModel


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = "__all__"


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = ("id", "featured_image", "title", "description", "slug")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = "__all__"


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ("id", "featured_image", "title", "description", "slug")


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuModel
        fields = "__all__"