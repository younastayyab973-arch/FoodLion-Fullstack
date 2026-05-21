from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order, OrderItem
from .serializers import OrderSerializer
from menu_items.models import MenuItem


class OrderListCreateView(APIView):
    def get(self, request):
        if not request.user.is_authenticated:
            return Response({'success': False, 'message': 'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)
        
        orders = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response({'success': True, 'data': serializer.data})
    
    def post(self, request):
        if not request.user.is_authenticated:
            return Response({'success': False, 'message': 'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)
        
        delivery_address = request.data.get('delivery_address')
        phone = request.data.get('phone')
        items = request.data.get('items', [])
        
        if not delivery_address or not phone or not items:
            return Response({'success': False, 'message': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)
        
        order = Order.objects.create(user=request.user, delivery_address=delivery_address, phone=phone)
        
        for item in items:
            try:
                menu_item = MenuItem.objects.get(id=item['menu_item_id'])
                OrderItem.objects.create(order=order, menu_item=menu_item, quantity=item.get('quantity', 1))
            except MenuItem.DoesNotExist:
                order.delete()
                return Response({'success': False, 'message': 'Menu item not found'}, status=status.HTTP_400_BAD_REQUEST)
        
        order.calculate_total()
        order.save()
        
        serializer = OrderSerializer(order)
        return Response({'success': True, 'data': serializer.data}, status=status.HTTP_201_CREATED)


class OrderDetailView(APIView):
    def get(self, request, pk):
        if not request.user.is_authenticated:
            return Response({'success': False, 'message': 'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)
        
        try:
            order = Order.objects.get(id=pk)
            if order.user != request.user and not request.user.is_admin_user:
                return Response({'success': False, 'message': 'Not authorized'}, status=status.HTTP_403_FORBIDDEN)
            
            serializer = OrderSerializer(order)
            return Response({'success': True, 'data': serializer.data})
        except Order.DoesNotExist:
            return Response({'success': False, 'message': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk):
        if not request.user.is_authenticated or not request.user.is_admin_user:
            return Response({'success': False, 'message': 'Admin access required'}, status=status.HTTP_403_FORBIDDEN)
        
        try:
            order = Order.objects.get(id=pk)
            status_update = request.data.get('status')
            if status_update:
                order.status = status_update
                order.save()
            
            serializer = OrderSerializer(order)
            return Response({'success': True, 'data': serializer.data})
        except Order.DoesNotExist:
            return Response({'success': False, 'message': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)
