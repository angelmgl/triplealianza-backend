from rest_framework import serializers
from .models import PostModel


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = "__all__"


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = ("id", "featured_image", "title", "description", "slug")