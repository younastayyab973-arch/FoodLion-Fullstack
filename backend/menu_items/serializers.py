from rest_framework import serializers
from .models import MenuItem


class MenuItemSerializer(serializers.ModelSerializer):
    restaurant_name = serializers.CharField(source='restaurant.name', read_only=True)
    
    class Meta:
        model = MenuItem
        fields = ['id', 'restaurant', 'restaurant_name', 'category', 'name', 'description', 'price', 'image', 'is_available', 'created_at']
        read_only_fields = ['id', 'created_at']
