from django.urls import path
from .views import welcome
from .views import PostList, PostDetail

urlpatterns = [
    path('welcome/', welcome, name='welcome'),
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<slug>/', PostDetail.as_view(), name='post-detail')
]