from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class BasePostModel(models.Model):
    title = models.CharField(max_length=150, verbose_name="Título")
    seo_title = models.CharField(max_length=150, verbose_name="Título SEO", default="")
    slug = models.CharField(max_length=150, verbose_name="Slug URL", unique=True)
    description = models.TextField(verbose_name="Descripción")
    featured_image = models.ImageField(upload_to='files', verbose_name="Imagen destacada")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última edición")
    content = RichTextUploadingField(verbose_name="Contenido")

    class Meta:
        abstract = True


class CategoryModel(BasePostModel):
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.title


class PostModel(BasePostModel):
    category = models.ForeignKey(CategoryModel, related_name="posts", on_delete=models.CASCADE, verbose_name="Categoría")

    class Meta:
        verbose_name = "Publicación"
        verbose_name_plural = "Publicaciones"

    def __str__(self):
        return self.title