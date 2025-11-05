from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """Modelo para categorizar los items brainrot"""
    name = models.CharField(max_length=100, unique=True, verbose_name="Nombre")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="Slug")
    description = models.TextField(blank=True, verbose_name="Descripción")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ['name']
    
    def __str__(self) -> str:
        return self.name


class BrainrotItem(models.Model):
    """Modelo principal para los items brainrot"""
    name = models.CharField(max_length=150, verbose_name="Nombre")
    description = models.TextField(verbose_name="Descripción")
    img = models.ImageField(upload_to='brainrot_images/', verbose_name="Imagen")
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='items',
        verbose_name="Categoría"
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")
    is_featured = models.BooleanField(default=False, verbose_name="Destacado")
    views_count = models.IntegerField(default=0, verbose_name="Visitas")

    class Meta:
        verbose_name = "Item Brainrot"
        verbose_name_plural = "Items Brainrot"
        ordering = ['-created']

    def __str__(self) -> str:
        return self.name


class Comment(models.Model):
    """Modelo para comentarios en los items brainrot"""
    item = models.ForeignKey(
        BrainrotItem,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name="Item"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='brainrot_comments',
        verbose_name="Usuario"
    )
    content = models.TextField(verbose_name="Contenido")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    is_approved = models.BooleanField(default=False, verbose_name="Aprobado")

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
        ordering = ['-created']

    def __str__(self) -> str:
        return f"Comentario de {self.user.username} en {self.item.name}"