from rest_framework import serializers
from brainrot.models import BrainrotItem


class BrainrotItemSerializer(serializers.ModelSerializer):
    """Serializer para el modelo BrainrotItem"""
    category_name = serializers.CharField(source='category.name', read_only=True)
    img_url = serializers.SerializerMethodField()
    
    class Meta:
        model = BrainrotItem
        fields = [
            'id',
            'name',
            'description',
            'img',
            'img_url',
            'category',
            'category_name',
            'is_featured',
            'views_count',
            'created',
            'updated',
        ]
        read_only_fields = ['id', 'created', 'updated', 'views_count', 'img_url']
    
    def get_img_url(self, obj):
        """Obtiene la URL completa de la imagen"""
        if obj.img:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.img.url)
            return obj.img.url
        return None