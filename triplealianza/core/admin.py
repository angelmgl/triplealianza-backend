from django.contrib import admin
from .models import CategoryModel, PostModel, MenuModel, PageModel

@admin.register(PageModel)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_at', 'updated_at')

@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_at', 'updated_at')

@admin.register(PostModel)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'slug', 'created_at', 'updated_at')

@admin.register(MenuModel)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('text', 'order', 'url')