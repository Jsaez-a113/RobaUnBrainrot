from django.contrib import admin
from django.utils.html import format_html
from .models import BrainrotItem, Category, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "created", "items_count")
    search_fields = ("name", "description")
    prepopulated_fields = {"slug": ("name",)}
    
    def items_count(self, obj):
        """Muestra la cantidad de items en esta categoría"""
        count = obj.items.count()
        return count
    items_count.short_description = "Items"


@admin.register(BrainrotItem)
class BrainrotItemAdmin(admin.ModelAdmin):
    # Parámetro 1: list_display - Columnas visibles en la lista
    list_display = (
        "thumbnail_preview",
        "name", 
        "category", 
        "is_featured",
        "views_count",
        "created", 
        "updated"
    )
    
    # Parámetro 2: list_filter - Filtros laterales
    list_filter = (
        "category",
        "is_featured",
        "created",
        "updated",
    )
    
    # Parámetro 3: search_fields - Campos buscables
    search_fields = ("name", "description", "category__name")
    
    # Parámetro 4: list_editable - Campos editables directamente en la lista
    list_editable = ("is_featured", "views_count")
    
    # Parámetro 5: fieldsets - Agrupa campos en secciones
    fieldsets = (
        ("Información Básica", {
            "fields": ("name", "description", "category")
        }),
        ("Imagen", {
            "fields": ("img",)
        }),
        ("Opciones", {
            "fields": ("is_featured", "views_count")
        }),
        ("Fechas", {
            "fields": ("created", "updated"),
            "classes": ("collapse",)
        }),
    )
    
    # Parámetro 6: readonly_fields - Campos de solo lectura
    readonly_fields = ("created", "updated", "thumbnail_preview")
    
    # Parámetro 7: list_per_page - Items por página
    list_per_page = 20
    
    # Parámetro 8: date_hierarchy - Navegación por fecha
    date_hierarchy = "created"
    
    # Parámetro 9: ordering - Orden por defecto
    ordering = ("-created",)
    
    # Parámetro 10: actions - Acciones personalizadas
    actions = ["mark_as_featured", "mark_as_not_featured"]
    
    def thumbnail_preview(self, obj):
        """Muestra una miniatura de la imagen en el admin"""
        if obj.img:
            return format_html(
                '<img src="{}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 4px;" />',
                obj.img.url
            )
        return "Sin imagen"
    thumbnail_preview.short_description = "Imagen"
    
    def mark_as_featured(self, request, queryset):
        """Marca los items seleccionados como destacados"""
        queryset.update(is_featured=True)
        self.message_user(request, f"{queryset.count()} items marcados como destacados.")
    mark_as_featured.short_description = "Marcar como destacados"
    
    def mark_as_not_featured(self, request, queryset):
        """Quita la marca de destacado de los items seleccionados"""
        queryset.update(is_featured=False)
        self.message_user(request, f"{queryset.count()} items desmarcados como destacados.")
    mark_as_not_featured.short_description = "Quitar marca de destacados"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("item", "user", "content_preview", "is_approved", "created")
    list_filter = ("is_approved", "created")
    search_fields = ("content", "user__username", "item__name")
    list_editable = ("is_approved",)
    readonly_fields = ("created",)
    
    def content_preview(self, obj):
        """Muestra una vista previa del contenido del comentario"""
        return obj.content[:50] + "..." if len(obj.content) > 50 else obj.content
    content_preview.short_description = "Contenido"