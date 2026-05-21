from django.urls import path
from . import views

urlpatterns = [
    path('', views.RestaurantListView.as_view(), name='restaurant-list'),
    path('<int:pk>/', views.RestaurantDetailView.as_view(), name='restaurant-detail'),
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
]
