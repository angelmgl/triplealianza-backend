from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class ImageModel(models.Model):
    title = models.CharField(max_length=150, verbose_name="Título")
    image = models.ImageField(upload_to='images', verbose_name="Imagen")

    class Meta:
        verbose_name = "Imagen"
        verbose_name_plural = "Imágenes"

    def __str__(self):
        return self.title


class BasePostModel(models.Model):
    title = models.CharField(max_length=150, verbose_name="Título")
    seo_title = models.CharField(max_length=150, verbose_name="Título SEO", default="")
    slug = models.CharField(max_length=150, verbose_name="Slug URL", unique=True)
    description = models.TextField(verbose_name="Descripción")
    featured_image = models.ForeignKey(ImageModel, on_delete=models.SET_NULL, null=True, blank=True)
    content = RichTextUploadingField(verbose_name="Contenido")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última edición")

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


class PageModel(BasePostModel):
    class Meta:
        verbose_name = "Página"
        verbose_name_plural = "Páginas"

    def __str__(self):
        return self.title


class MenuModel(models.Model):
    text = models.CharField(max_length=50, verbose_name="Texto")
    url = models.CharField(max_length=50, verbose_name="URL")
    order = models.IntegerField(unique=True, verbose_name="Orden")

    class Meta:
        verbose_name = "Enlace del menú"
        verbose_name_plural = "Enlaces del menú"
        ordering = ['order']

    def __str__(self):
        return self.text