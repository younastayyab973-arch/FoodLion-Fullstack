import math
from django.db.models import Sum, Count
from django.utils import timezone
from rest_framework.response import Response
from rest_framework import status
from .permissions import AdminAPIView
from authentication.models import User
from authentication.serializers import UserSerializer
from restaurants.models import Restaurant
from restaurants.serializers import RestaurantSerializer
from orders.models import Order
from orders.serializers import OrderSerializer

PAGE_SIZE = 25


def _paginate(qs, request):
    """Return (page_qs, total, page, pages) for a queryset."""
    try:
        page = max(1, int(request.query_params.get('page', 1)))
    except (ValueError, TypeError):
        page = 1
    total = qs.count()
    pages = max(1, math.ceil(total / PAGE_SIZE))
    page = min(page, pages)
    offset = (page - 1) * PAGE_SIZE
    return qs[offset:offset + PAGE_SIZE], total, page, pages


class DashboardView(AdminAPIView):
    """Admin dashboard with key metrics."""
    
    def get(self, request):
        today = timezone.now().date()
        data = {
            'total_restaurants': Restaurant.objects.count(),
            'total_orders': Order.objects.count(),
            'pending_orders': Order.objects.filter(status='pending').count(),
            'total_revenue': float(Order.objects.aggregate(t=Sum('total_price'))['t'] or 0),
            'todays_orders': Order.objects.filter(created_at__date=today).count(),
            'total_users': User.objects.count(),
            'recent_orders': OrderSerializer(
                Order.objects.select_related('user').prefetch_related('items').order_by('-created_at')[:8],
                many=True,
            ).data,
        }
        return Response({'success': True, 'data': data})


class AdminRestaurantListView(AdminAPIView):
    """Admin restaurant management."""
    
    def get(self, request):
        qs = Restaurant.objects.all()
        q = request.query_params.get('q')
        if q:
            qs = qs.filter(name__icontains=q)
        
        qs, total, page, pages = _paginate(qs, request)
        return Response({
            'success': True,
            'total': total, 'page': page, 'pages': pages,
            'restaurants': RestaurantSerializer(qs, many=True).data,
        })
    
    def post(self, request):
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'success': False, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class AdminRestaurantDetailView(AdminAPIView):
    """Admin restaurant detail view."""
    
    def get(self, request, pk):
        try:
            restaurant = Restaurant.objects.get(id=pk)
            serializer = RestaurantSerializer(restaurant)
            return Response({'success': True, 'data': serializer.data})
        except Restaurant.DoesNotExist:
            return Response({'success': False, 'message': 'Restaurant not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk):
        try:
            restaurant = Restaurant.objects.get(id=pk)
            serializer = RestaurantSerializer(restaurant, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'success': True, 'data': serializer.data})
            return Response({'success': False, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Restaurant.DoesNotExist:
            return Response({'success': False, 'message': 'Restaurant not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, pk):
        try:
            restaurant = Restaurant.objects.get(id=pk)
            restaurant.is_active = False
            restaurant.save()
            return Response({'success': True, 'message': 'Restaurant deactivated'})
        except Restaurant.DoesNotExist:
            return Response({'success': False, 'message': 'Restaurant not found'}, status=status.HTTP_404_NOT_FOUND)


class AdminOrderListView(AdminAPIView):
    """Admin order management."""
    
    def get(self, request):
        qs = Order.objects.select_related('user').prefetch_related('items')
        status_filter = request.query_params.get('status')
        if status_filter:
            qs = qs.filter(status=status_filter)
        
        qs, total, page, pages = _paginate(qs, request)
        return Response({
            'success': True,
            'total': total, 'page': page, 'pages': pages,
            'orders': OrderSerializer(qs, many=True).data,
        })


class AdminOrderDetailView(AdminAPIView):
    """Admin order detail view."""
    
    def get(self, request, pk):
        try:
            order = Order.objects.select_related('user').prefetch_related('items').get(id=pk)
            serializer = OrderSerializer(order)
            return Response({'success': True, 'data': serializer.data})
        except Order.DoesNotExist:
            return Response({'success': False, 'message': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk):
        try:
            order = Order.objects.get(id=pk)
            new_status = request.data.get('status')
            if new_status:
                order.status = new_status
                order.save()
            
            serializer = OrderSerializer(order)
            return Response({'success': True, 'data': serializer.data})
        except Order.DoesNotExist:
            return Response({'success': False, 'message': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)


class AdminUserListView(AdminAPIView):
    """Admin user management."""
    
    def get(self, request):
        qs = User.objects.all()
        q = request.query_params.get('q')
        if q:
            qs = qs.filter(email__icontains=q)
        
        qs, total, page, pages = _paginate(qs, request)
        return Response({
            'success': True,
            'total': total, 'page': page, 'pages': pages,
            'users': UserSerializer(qs, many=True).data,
        })
