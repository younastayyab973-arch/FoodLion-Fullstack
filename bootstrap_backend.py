#!/usr/bin/env python3
"""
FoodLion Django Backend - Complete Bootstrap Script
Creates all directories and files needed for the Django backend with admin dashboard
"""
import os
from pathlib import Path
import json

BASE_DIR = Path(__file__).parent
BACKEND_DIR = BASE_DIR / 'backend'

# Define all files to create with their content
FILES = {
    'requirements.txt': '''Django>=4.2
djangorestframework>=3.14
django-cors-headers>=4.3
PyJWT>=2.8
python-dotenv>=1.0
bcrypt>=4.0
''',
    
    '.env': '''# Django Configuration
DEBUG=True
SECRET_KEY=django-insecure-your-secret-key-here-change-in-production
JWT_SECRET=your-jwt-secret-key-here-change-in-production

# Server
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:8000,http://127.0.0.1:8000,http://localhost:3000
''',
    
    '.gitignore': '''# Environment
.env
.env.local
.venv
venv/
env/

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# Database
*.sqlite3
*.db

# Logs
*.log
''',

    'manage.py': '''#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'foodlion.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
''',

    'foodlion/__init__.py': '',

    'foodlion/wsgi.py': '''"""
WSGI config for foodlion project.
For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'foodlion.settings')
application = get_wsgi_application()
''',

    'foodlion/settings.py': '''import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / '.env')

# ─── Secret Key & Debug ────────────────────────────────────────────────────────

_secret_key = os.getenv('SECRET_KEY')
if not _secret_key:
    raise RuntimeError("SECRET_KEY environment variable is not set")
SECRET_KEY = _secret_key

_jwt_secret = os.getenv('JWT_SECRET')
if not _jwt_secret:
    raise RuntimeError("JWT_SECRET environment variable is not set")
JWT_SECRET = _jwt_secret

DEBUG = os.getenv('DEBUG', 'False') == 'True'

_allowed_hosts = os.getenv('ALLOWED_HOSTS', 'localhost,127.0.0.1')
ALLOWED_HOSTS = [h.strip() for h in _allowed_hosts.split(',') if h.strip()]

# ─── Installed Apps ────────────────────────────────────────────────────────────

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'authentication',
    'restaurants',
    'menu_items',
    'orders',
    'adminpanel',
]

# ─── Middleware ────────────────────────────────────────────────────────────────

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ─── URLs & Templates ──────────────────────────────────────────────────────────

ROOT_URLCONF = 'foodlion.urls'

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
        ],
    },
}]

WSGI_APPLICATION = 'foodlion.wsgi.application'

# ─── Database ──────────────────────────────────────────────────────────────────

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ─── Authentication ────────────────────────────────────────────────────────────

AUTH_USER_MODEL = 'authentication.User'

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ─── REST Framework ────────────────────────────────────────────────────────────

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'authentication.backends.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/hour',
        'login': '5/minute',
    },
}

# ─── CORS ──────────────────────────────────────────────────────────────────────

_cors_origins = os.getenv('CORS_ALLOWED_ORIGINS', 'http://localhost:8000,http://127.0.0.1:8000')
CORS_ALLOWED_ORIGINS = [o.strip() for o in _cors_origins.split(',') if o.strip()]

CORS_ALLOW_CREDENTIALS = True

# ─── Internationalization ──────────────────────────────────────────────────────

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ─── Static files ──────────────────────────────────────────────────────────────

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ─── Logging ────────────────────────────────────────────────────────────────────

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}
''',

    'foodlion/urls.py': '''from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django admin panel
    path('admin/', admin.site.urls),

    # ── REST API routes ──────────────────────────────────────────────────────
    path('api/auth/',        include('authentication.urls')),
    path('api/restaurants/', include('restaurants.urls')),
    path('api/menu-items/',  include('menu_items.urls')),
    path('api/orders/',      include('orders.urls')),
    path('api/admin/',       include('adminpanel.api_urls')),

    # ── Admin panel pages ────────────────────────────────────────────────────
    path('admin-panel/', include('adminpanel.urls')),
]
''',

    'authentication/__init__.py': '',
    
    'authentication/models.py': '''from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    """Custom user manager for email-based authentication."""
    
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    """Custom User model with email-based authentication."""
    email = models.EmailField(unique=True)
    username = None
    phone = models.CharField(max_length=15, blank=True)
    is_admin_user = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = UserManager()
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.email
''',

    'authentication/serializers.py': '''from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'phone', 'is_admin_user', 'created_at']
        read_only_fields = ['id', 'created_at']


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    password_confirm = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['email', 'password', 'password_confirm', 'first_name', 'last_name', 'phone']
    
    def validate(self, data):
        if data['password'] != data.pop('password_confirm'):
            raise serializers.ValidationError("Passwords do not match")
        return data
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
''',

    'authentication/backends.py': '''import jwt
from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import User


class JWTAuthentication(TokenAuthentication):
    """JWT authentication backend."""
    
    def authenticate(self, request):
        auth = self.get_authorization_header(request).split()
        
        if not auth or auth[0].lower() != b'bearer':
            return None
        
        if len(auth) == 1:
            raise AuthenticationFailed('Invalid token header. No credentials provided.')
        elif len(auth) > 2:
            raise AuthenticationFailed('Invalid token header. Token string should not contain spaces.')
        
        try:
            token = auth[1].decode('utf-8')
        except UnicodeDecodeError:
            raise AuthenticationFailed('Invalid token encoding.')
        
        return self.authenticate_credentials(token)
    
    def authenticate_credentials(self, key):
        try:
            payload = jwt.decode(key, settings.JWT_SECRET, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token expired')
        except jwt.InvalidTokenError:
            raise AuthenticationFailed('Invalid token')
        
        try:
            user = User.objects.get(id=payload['user_id'])
        except User.DoesNotExist:
            raise AuthenticationFailed('User not found')
        
        if not user.is_active:
            raise AuthenticationFailed('User inactive')
        
        return (user, key)
''',

    'authentication/urls.py': '''from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('refresh/', views.RefreshTokenView.as_view(), name='refresh'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
]
''',

    'authentication/views.py': '''from datetime import datetime, timedelta
import jwt
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer, SignupSerializer, LoginSerializer


def generate_tokens(user):
    """Generate JWT access and refresh tokens."""
    access_payload = {
        'user_id': user.id,
        'email': user.email,
        'exp': datetime.utcnow() + timedelta(hours=24),
        'iat': datetime.utcnow(),
    }
    
    refresh_payload = {
        'user_id': user.id,
        'exp': datetime.utcnow() + timedelta(days=7),
        'iat': datetime.utcnow(),
    }
    
    access_token = jwt.encode(access_payload, settings.JWT_SECRET, algorithm='HS256')
    refresh_token = jwt.encode(refresh_payload, settings.JWT_SECRET, algorithm='HS256')
    
    return access_token, refresh_token


class SignupView(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            access_token, refresh_token = generate_tokens(user)
            return Response({
                'success': True,
                'user': UserSerializer(user).data,
                'access_token': access_token,
                'refresh_token': refresh_token,
            }, status=status.HTTP_201_CREATED)
        return Response({'success': False, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'success': False, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = User.objects.get(email=serializer.validated_data['email'])
            if not user.check_password(serializer.validated_data['password']):
                return Response({'success': False, 'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        except User.DoesNotExist:
            return Response({'success': False, 'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
        access_token, refresh_token = generate_tokens(user)
        return Response({
            'success': True,
            'user': UserSerializer(user).data,
            'access_token': access_token,
            'refresh_token': refresh_token,
        })


class LogoutView(APIView):
    def post(self, request):
        return Response({'success': True, 'message': 'Logged out successfully'})


class RefreshTokenView(APIView):
    def post(self, request):
        refresh_token = request.data.get('refresh_token')
        if not refresh_token:
            return Response({'success': False, 'message': 'Refresh token required'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            payload = jwt.decode(refresh_token, settings.JWT_SECRET, algorithms=['HS256'])
            user = User.objects.get(id=payload['user_id'])
            access_token, new_refresh_token = generate_tokens(user)
            return Response({
                'success': True,
                'access_token': access_token,
                'refresh_token': new_refresh_token,
            })
        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError, User.DoesNotExist):
            return Response({'success': False, 'message': 'Invalid refresh token'}, status=status.HTTP_401_UNAUTHORIZED)


class ProfileView(APIView):
    def get(self, request):
        if not request.user.is_authenticated:
            return Response({'success': False, 'message': 'Not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
        
        return Response({
            'success': True,
            'user': UserSerializer(request.user).data,
        })
    
    def put(self, request):
        if not request.user.is_authenticated:
            return Response({'success': False, 'message': 'Not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
        
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'user': serializer.data})
        return Response({'success': False, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
''',

    'restaurants/__init__.py': '',
    
    'restaurants/models.py': '''from django.db import models


class Category(models.Model):
    """Restaurant category (e.g., Biryani, Cakes, KFC, Dominos)."""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    image = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'categories'
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Restaurant(models.Model):
    """Restaurant information."""
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    image = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    rating = models.FloatField(default=0, help_text='0-5 star rating')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name
''',

    'restaurants/serializers.py': '''from rest_framework import serializers
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
''',

    'restaurants/urls.py': '''from django.urls import path
from . import views

urlpatterns = [
    path('', views.RestaurantListView.as_view(), name='restaurant-list'),
    path('<int:pk>/', views.RestaurantDetailView.as_view(), name='restaurant-detail'),
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
]
''',

    'restaurants/views.py': '''from rest_framework.views import APIView
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
''',

    'menu_items/__init__.py': '',
    
    'menu_items/models.py': '''from django.db import models
from restaurants.models import Restaurant, Category


class MenuItem(models.Model):
    """Menu item for a restaurant."""
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menu_items')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField(blank=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.restaurant.name}"
''',

    'menu_items/serializers.py': '''from rest_framework import serializers
from .models import MenuItem


class MenuItemSerializer(serializers.ModelSerializer):
    restaurant_name = serializers.CharField(source='restaurant.name', read_only=True)
    
    class Meta:
        model = MenuItem
        fields = ['id', 'restaurant', 'restaurant_name', 'category', 'name', 'description', 'price', 'image', 'is_available', 'created_at']
        read_only_fields = ['id', 'created_at']
''',

    'menu_items/urls.py': '''from django.urls import path
from . import views

urlpatterns = [
    path('', views.MenuItemListView.as_view(), name='menu-item-list'),
    path('<int:pk>/', views.MenuItemDetailView.as_view(), name='menu-item-detail'),
]
''',

    'menu_items/views.py': '''from rest_framework.views import APIView
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
''',

    'orders/__init__.py': '',
    
    'orders/models.py': '''from django.db import models
from django.contrib.auth import get_user_model
from menu_items.models import MenuItem

User = get_user_model()


class Order(models.Model):
    """Customer order."""
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('preparing', 'Preparing'),
        ('ready', 'Ready'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    delivery_address = models.CharField(max_length=500)
    phone = models.CharField(max_length=20)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Order #{self.id} - {self.user.email}"
    
    def calculate_total(self):
        """Calculate total from order items."""
        total = sum(item.quantity * item.menu_item.price for item in self.items.all())
        self.total_price = total
        return total


class OrderItem(models.Model):
    """Individual item in an order."""
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    menu_item = models.ForeignKey(MenuItem, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        ordering = ['id']
    
    def __str__(self):
        return f"{self.quantity}x {self.menu_item.name}"
    
    def save(self, *args, **kwargs):
        self.price = self.menu_item.price
        super().save(*args, **kwargs)
''',

    'orders/serializers.py': '''from rest_framework import serializers
from .models import Order, OrderItem
from menu_items.serializers import MenuItemSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    menu_item = MenuItemSerializer(read_only=True)
    
    class Meta:
        model = OrderItem
        fields = ['id', 'menu_item', 'quantity', 'price']
        read_only_fields = ['price']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = Order
        fields = ['id', 'user', 'status', 'total_price', 'delivery_address', 'phone', 'notes', 'items', 'created_at', 'updated_at']
        read_only_fields = ['id', 'user', 'total_price', 'created_at', 'updated_at']
''',

    'orders/urls.py': '''from django.urls import path
from . import views

urlpatterns = [
    path('', views.OrderListCreateView.as_view(), name='order-list'),
    path('<int:pk>/', views.OrderDetailView.as_view(), name='order-detail'),
]
''',

    'orders/views.py': '''from rest_framework.views import APIView
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
''',

    'adminpanel/__init__.py': '',
    
    'adminpanel/permissions.py': '''from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class AdminAPIView(APIView):
    """Base class ensuring only admins can access."""
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response({'success': False, 'message': 'Authentication required'}, status=status.HTTP_401_UNAUTHORIZED)
        
        if not request.user.is_admin_user:
            return Response({'success': False, 'message': 'Admin access required'}, status=status.HTTP_403_FORBIDDEN)
        
        return super().dispatch(request, *args, **kwargs)
''',

    'adminpanel/api_urls.py': '''from django.urls import path
from . import api_views

urlpatterns = [
    path('dashboard/', api_views.DashboardView.as_view(), name='dashboard'),
    path('restaurants/', api_views.AdminRestaurantListView.as_view(), name='admin-restaurants'),
    path('restaurants/<int:pk>/', api_views.AdminRestaurantDetailView.as_view(), name='admin-restaurant-detail'),
    path('orders/', api_views.AdminOrderListView.as_view(), name='admin-orders'),
    path('orders/<int:pk>/', api_views.AdminOrderDetailView.as_view(), name='admin-order-detail'),
    path('users/', api_views.AdminUserListView.as_view(), name='admin-users'),
]
''',

    'adminpanel/urls.py': '''from django.urls import path
from . import page_views

urlpatterns = [
    path('', page_views.admin_dashboard, name='admin-dashboard'),
]
''',

    'adminpanel/page_views.py': '''from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test


def is_admin(user):
    return user.is_authenticated and user.is_admin_user


@user_passes_test(is_admin)
def admin_dashboard(request):
    return render(request, 'adminpanel/dashboard.html')
''',

    'adminpanel/api_views.py': '''import math
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
''',
}


def create_backend():
    """Create all backend files."""
    print("\\n" + "=" * 70)
    print("FoodLion Django Backend Bootstrap")
    print("=" * 70 + "\\n")
    
    # Create all directories first
    dirs = set()
    for file_path in FILES.keys():
        dir_path = BACKEND_DIR / file_path.rsplit('/', 1)[0] if '/' in file_path else BACKEND_DIR
        dirs.add(dir_path)
    
    for dir_path in sorted(dirs):
        dir_path.mkdir(parents=True, exist_ok=True)
        print(f"✓ Directory: {dir_path.relative_to(BASE_DIR)}")
    
    # Create all files
    print("\\nCreating files...")
    print("-" * 70)
    
    for file_path, content in FILES.items():
        full_path = BACKEND_DIR / file_path
        full_path.parent.mkdir(parents=True, exist_ok=True)
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ {file_path}")
    
    print("\\n" + "=" * 70)
    print("✓ Backend created successfully!")
    print("=" * 70)
    print("\\nNext steps:")
    print("  1. cd backend")
    print("  2. python -m venv venv")
    print("  3. venv\\\\Scripts\\\\activate  (Windows)")
    print("  4. pip install -r requirements.txt")
    print("  5. python manage.py migrate")
    print("  6. python manage.py createsuperuser")
    print("  7. python manage.py runserver")
    print()


if __name__ == '__main__':
    create_backend()
