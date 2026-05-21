from django.urls import path
from . import page_views

urlpatterns = [
    path('', page_views.admin_dashboard, name='admin-dashboard'),
]
