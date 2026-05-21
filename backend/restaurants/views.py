from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Restaurant, Category
from .serializers import RestaurantSerializer, CategorySerializer


class RestaurantListView(APIView):
    def get(self, request):
        restaurants = Restaurant.objects.filter(is_active=True)
        category = request.query_params.get('category')
        if category:
            restaurants = restaurants.filter(category__name__icontains=category)
        
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response({'success': True, 'data': serializer.data})
    
    def post(self, request):
        if not request.user.is_authenticated or not request.user.is_admin_user:
            return Response({'success': False, 'message': 'Admin access required'}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'success': False, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class RestaurantDetailView(APIView):
    def get(self, request, pk):
        try:
            restaurant = Restaurant.objects.get(id=pk, is_active=True)
            serializer = RestaurantSerializer(restaurant)
            return Response({'success': True, 'data': serializer.data})
        except Restaurant.DoesNotExist:
            return Response({'success': False, 'message': 'Restaurant not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk):
        if not request.user.is_authenticated or not request.user.is_admin_user:
            return Response({'success': False, 'message': 'Admin access required'}, status=status.HTTP_403_FORBIDDEN)
        
        try:
            restaurant = Restaurant.objects.get(id=pk)
            serializer = RestaurantSerializer(restaurant, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'success': True, 'data': serializer.data})
            return Response({'success': False, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Restaurant.DoesNotExist:
            return Response({'success': False, 'message': 'Restaurant not found'}, status=status.HTTP_404_NOT_FOUND)


class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response({'success': True, 'data': serializer.data})
