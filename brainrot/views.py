from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import BrainrotItem, Category, Comment


def item_list(request):
    """Vista de lista con filtros por categoría y fecha"""
    queryset = BrainrotItem.objects.all()
    
    # Filtro 1: Por categoría
    category_slug = request.GET.get('category')
    if category_slug:
        queryset = queryset.filter(category__slug=category_slug)
    
    # Filtro 2: Por fecha (recientes, antiguos)
    date_filter = request.GET.get('date_filter')
    if date_filter == 'recent':
        queryset = queryset.order_by('-created')
    elif date_filter == 'old':
        queryset = queryset.order_by('created')
    elif date_filter == 'featured':
        queryset = queryset.filter(is_featured=True)
    
    # Búsqueda
    search_query = request.GET.get('search')
    if search_query:
        queryset = queryset.filter(
            Q(name__icontains=search_query) | 
            Q(description__icontains=search_query)
        )
    
    paginator = Paginator(queryset, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    # Obtener todas las categorías para el filtro
    categories = Category.objects.all()
    
    context = {
        "page_title": "Roba un Brainrot - Items",
        "banner_url": "https://images.alphacoders.com/139/1396558.jpg",
        "page_obj": page_obj,
        "categories": categories,
        "current_category": category_slug,
        "current_date_filter": date_filter,
        "search_query": search_query,
    }
    return render(request, "brainrot/item_list.html", context)


def item_detail(request, pk: int):
    """Vista de detalle que incrementa el contador de visitas"""
    item = get_object_or_404(BrainrotItem, pk=pk)
    
    # Incrementar contador de visitas
    item.views_count += 1
    item.save(update_fields=['views_count'])
    
    # Obtener comentarios aprobados
    comments = item.comments.filter(is_approved=True)
    
    context = {
        "page_title": f"{item.name} - Roba un Brainrot",
        "banner_url": item.img.url if item.img else "https://images.alphacoders.com/139/1396558.jpg",
        "item": item,
        "comments": comments,
    }
    return render(request, "brainrot/item_detail.html", context)