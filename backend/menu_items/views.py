from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MenuItem
from .serializers import MenuItemSerializer


class MenuItemListView(APIView):
    def get(self, request):
        menu_items = MenuItem.objects.filter(is_available=True)
        restaurant = request.query_params.get('restaurant')
        if restaurant:
            menu_items = menu_items.filter(restaurant__id=restaurant)
        
        serializer = MenuItemSerializer(menu_items, many=True)
        return Response({'success': True, 'data': serializer.data})
    
    def post(self, request):
        if not request.user.is_authenticated or not request.user.is_admin_user:
            return Response({'success': False, 'message': 'Admin access required'}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = MenuItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'success': False, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class MenuItemDetailView(APIView):
    def get(self, request, pk):
        try:
            menu_item = MenuItem.objects.get(id=pk, is_available=True)
            serializer = MenuItemSerializer(menu_item)
            return Response({'success': True, 'data': serializer.data})
        except MenuItem.DoesNotExist:
            return Response({'success': False, 'message': 'Menu item not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk):
        if not request.user.is_authenticated or not request.user.is_admin_user:
            return Response({'success': False, 'message': 'Admin access required'}, status=status.HTTP_403_FORBIDDEN)
        
        try:
            menu_item = MenuItem.objects.get(id=pk)
            serializer = MenuItemSerializer(menu_item, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'success': True, 'data': serializer.data})
            return Response({'success': False, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except MenuItem.DoesNotExist:
            return Response({'success': False, 'message': 'Menu item not found'}, status=status.HTTP_404_NOT_FOUND)
