"""
Frontend views to serve HTML files from Django
"""
from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings
from pathlib import Path


class FrontendView(TemplateView):
    """Serve frontend HTML files"""
    template_name = None
    
    def get_template_names(self):
        """Get the template name from URL"""
        return [self.template_name] if self.template_name else ['dashboard-portal.html']


def serve_html(request, template_name):
    """Serve HTML files from the frontend directory"""
    return render(request, template_name)


def dashboard_portal(request):
    """Dashboard Portal - Main hub"""
    return render(request, 'dashboard-portal.html')


def admin_dashboard(request):
    """Admin Dashboard"""
    return render(request, 'admin-dashboard.html')


def admin_login(request):
    """Admin Login Page"""
    return render(request, 'admin-login.html')


def restaurant_panel(request):
    """Restaurant Panel"""
    return render(request, 'restaurant-panel.html')


def menu_management(request):
    """Menu Management"""
    return render(request, 'menu-management.html')


def order_management(request):
    """Order Management"""
    return render(request, 'order-management.html')


def cart_management(request):
    """Cart Management"""
    return render(request, 'cart-management.html')


def rider_panel(request):
    """Rider Panel"""
    return render(request, 'rider-panel.html')


def customer_panel(request):
    """Customer Panel"""
    return render(request, 'customer-panel.html')


def home(request):
    """Home Page"""
    return render(request, 'home.html')


def about(request):
    """About Page"""
    return render(request, 'about.html')


def services(request):
    """Services Page"""
    return render(request, 'services.html')


def contact(request):
    """Contact Page"""
    return render(request, 'contacts.html')


def restaurants(request):
    """Restaurants Page"""
    return render(request, 'restaurants.html')


def login_page(request):
    """Login Page"""
    return render(request, 'login.html')


def signup_page(request):
    """Signup Page"""
    return render(request, 'signup.html')