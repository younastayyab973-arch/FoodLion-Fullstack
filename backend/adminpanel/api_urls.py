from django.urls import path
from . import api_views

urlpatterns = [
    path('dashboard/', api_views.DashboardView.as_view(), name='dashboard'),
    path('restaurants/', api_views.AdminRestaurantListView.as_view(), name='admin-restaurants'),
    path('restaurants/<int:pk>/', api_views.AdminRestaurantDetailView.as_view(), name='admin-restaurant-detail'),
    path('orders/', api_views.AdminOrderListView.as_view(), name='admin-orders'),
    path('orders/<int:pk>/', api_views.AdminOrderDetailView.as_view(), name='admin-order-detail'),
    path('users/', api_views.AdminUserListView.as_view(), name='admin-users'),
]
