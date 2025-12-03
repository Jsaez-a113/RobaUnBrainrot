from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from brainrot.models import BrainrotItem
from .serializers import BrainrotItemSerializer


@api_view(['GET', 'POST'])
def brainrot_items(request):
    """
    API endpoint para listar y crear items brainrot.
    
    GET: Retorna lista de todos los items
    POST: Crea un nuevo item
    """
    if request.method == 'GET':
        items = BrainrotItem.objects.all().order_by('-created')
        serializer = BrainrotItemSerializer(items, many=True, context={'request': request})
        return Response({
            'count': len(serializer.data),
            'results': serializer.data
        }, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = BrainrotItemSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
