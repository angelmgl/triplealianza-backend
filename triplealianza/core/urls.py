from django.urls import path
from .views import welcome
from .views import PostList, PostDetail, CategoryDetail, CategoryList

urlpatterns = [
    path("welcome/", welcome, name="welcome"),
    path("posts/", PostList.as_view(), name="post-list"),
    path("posts/<slug>/", PostDetail.as_view(), name="post-detail"),
    path("categories/", CategoryList.as_view(), name="category-list"),
    path("categories/<slug>/", CategoryDetail.as_view(), name="category-detail")
]