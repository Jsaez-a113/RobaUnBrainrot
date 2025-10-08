from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import BrainrotItem


def item_list(request):
    queryset = BrainrotItem.objects.all()
    paginator = Paginator(queryset, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "page_title": "Roba un Brainrot - Items",
        "banner_url": "https://images.alphacoders.com/139/1396558.jpg",
        "page_obj": page_obj,
    }
    return render(request, "brainrot/item_list.html", context)


def item_detail(request, pk: int):
    item = get_object_or_404(BrainrotItem, pk=pk)
    context = {
        "page_title": f"{item.name} - Roba un Brainrot",
        "banner_url": item.img.url if item.img else "https://images.alphacoders.com/139/1396558.jpg",
        "item": item,
    }
    return render(request, "brainrot/item_detail.html", context)