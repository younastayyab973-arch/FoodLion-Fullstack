from django.urls import path
from . import views

urlpatterns = [
    path('', views.MenuItemListView.as_view(), name='menu-item-list'),
    path('<int:pk>/', views.MenuItemDetailView.as_view(), name='menu-item-detail'),
]
