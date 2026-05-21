from rest_framework import serializers
from .models import Restaurant, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'image']


class RestaurantSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'category', 'category_name', 'description', 'address', 'phone', 'email', 'image', 'is_active', 'rating', 'created_at']
        read_only_fields = ['id', 'created_at']
