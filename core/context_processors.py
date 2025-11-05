from brainrot.models import BrainrotItem, Category, Comment


def brainrot_stats(request):
    """
    Procesador de contexto que añade estadísticas de brainrot
    a todas las plantillas del sitio
    """
    return {
        'total_items': BrainrotItem.objects.count(),
        'total_categories': Category.objects.count(),
        'total_comments': Comment.objects.filter(is_approved=True).count(),
        'featured_items_count': BrainrotItem.objects.filter(is_featured=True).count(),
        'all_categories': Category.objects.all()[:5],  # Primeras 5 categorías para el menú
        'recent_items': BrainrotItem.objects.all()[:3],  # Últimos 3 items para mostrar
    }
