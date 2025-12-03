import requests
from django.shortcuts import render
from django.conf import settings
from django.core.cache import cache


def api_items_view(request):
    """
    Vista que consume la API local para mostrar items brainrot
    """
    api_url = f"{request.scheme}://{request.get_host()}/api/items/"
    
    try:
        # Intentar obtener datos de la API
        response = requests.get(api_url, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            items = data.get('results', [])
            count = data.get('count', 0)
            error = None
        else:
            items = []
            count = 0
            error = f"Error al obtener datos de la API: {response.status_code}"
    
    except requests.exceptions.RequestException as e:
        # Si la API no está disponible, mostrar error
        items = []
        count = 0
        error = f"No se pudo conectar con la API: {str(e)}"
    
    context = {
        'page_title': 'Roba un Brainrot - Items desde API',
        'banner_url': 'https://images.alphacoders.com/139/1396558.jpg',
        'items': items,
        'count': count,
        'error': error,
        'api_url': api_url,
    }
    return render(request, 'api_consumer/api_items.html', context)
