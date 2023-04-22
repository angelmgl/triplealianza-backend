from django.urls import path
from .views import (
    welcome,
    PostList, 
    PostListByCategory, 
    PostDetail, 
    PageList, 
    PageDetail, 
    CategoryDetail, 
    CategoryList, 
    MenuList,
    SlideList
)

urlpatterns = [
    path("welcome/", welcome, name="welcome"),
    path("menu/", MenuList.as_view(), name="menu-list"),
    path("posts/", PostList.as_view(), name="post-list"),
    path("posts/category/<slug:category_slug>/", PostListByCategory.as_view(), name="post-list-by-category"),
    path("posts/<slug:slug>/", PostDetail.as_view(), name="post-detail"),
    path("categories/", CategoryList.as_view(), name="category-list"),
    path("categories/<slug>/", CategoryDetail.as_view(), name="category-detail"),
    path("pages/", PageList.as_view(), name="page-list"),
    path("pages/<slug>/", PageDetail.as_view(), name="page-detail"),
    path("slides/", SlideList.as_view(), name="slide-list"),
]