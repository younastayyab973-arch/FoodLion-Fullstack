#!/usr/bin/env python
"""
Complete Integration Setup for FoodLion
This script sets up the integrated backend-frontend system
Run this ONCE to configure everything
"""
import os
import sys
import django
from pathlib import Path

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'foodlion.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from django.core.management import call_command
from django.contrib.auth import get_user_model
from restaurants.models import Restaurant, Category
from menu_items.models import MenuItem

print("\n" + "=" * 80)
print("FoodLion - Complete Integration Setup")
print("=" * 80 + "\n")

# Step 1: Run migrations
print("📦 Step 1: Running migrations...")
try:
    call_command('migrate', verbosity=0)
    print("   ✅ Migrations completed successfully\n")
except Exception as e:
    print(f"   ❌ Migration error: {e}\n")

# Step 2: Collect static files
print("📁 Step 2: Collecting static files...")
try:
    call_command('collectstatic', '--noinput', verbosity=0)
    print("   ✅ Static files collected\n")
except Exception as e:
    print(f"   ⚠️  Static files warning: {e}\n")

# Step 3: Create or update admin user
print("👤 Step 3: Setting up admin user...")
User = get_user_model()
admin_email = 'ray@gmail.com'
admin_password = 'Ray123'

admin_user, created = User.objects.get_or_create(
    email=admin_email,
    defaults={
        'first_name': 'Ray',
        'last_name': 'Admin',
        'is_staff': True,
        'is_superuser': True,
        'is_admin_user': True,
    }
)

if created:
    admin_user.set_password(admin_password)
    admin_user.save()
    print(f"   ✅ Admin user created: {admin_email}\n")
else:
    print(f"   ✅ Admin user already exists: {admin_email}\n")

# Step 4: Setup sample data
print("🍔 Step 4: Setting up sample data...")

# Create categories
categories_data = [
    ('Biryani', 'Delicious Pakistani biryani dishes'),
    ('Cakes', 'Fresh and delicious cakes'),
    ('KFC', 'Fried chicken and sides'),
    ('Dominos', 'Pizza and Italian food'),
]

categories = {}
for name, description in categories_data:
    category, _ = Category.objects.get_or_create(
        name=name,
        defaults={'description': description}
    )
    categories[name] = category
    print(f"   ✅ Category: {name}")

# Create restaurants
restaurants_data = [
    {
        'name': 'Karachi Biryani House',
        'category': 'Biryani',
        'address': 'Clifton, Karachi',
        'phone': '021-1234567',
        'email': 'biryani@foodlion.com',
        'rating': 4.8,
    },
    {
        'name': 'Sweet Dreams Bakery',
        'category': 'Cakes',
        'address': 'Defence, Karachi',
        'phone': '021-2345678',
        'email': 'cakes@foodlion.com',
        'rating': 4.6,
    },
    {
        'name': 'KFC Pakistan',
        'category': 'KFC',
        'address': 'Gulshan-e-Iqbal, Karachi',
        'phone': '021-3456789',
        'email': 'kfc@foodlion.com',
        'rating': 4.7,
    },
    {
        'name': 'Dominos Pizza',
        'category': 'Dominos',
        'address': 'Zamzama, Karachi',
        'phone': '021-4567890',
        'email': 'pizza@foodlion.com',
        'rating': 4.5,
    },
]

restaurants = {}
for rest_data in restaurants_data:
    category_name = rest_data.pop('category')
    restaurant, _ = Restaurant.objects.get_or_create(
        name=rest_data['name'],
        defaults={**rest_data, 'category': categories[category_name]}
    )
    restaurants[rest_data['name']] = restaurant
    print(f"   ✅ Restaurant: {rest_data['name']}")

# Create menu items
menu_items_data = [
    {'restaurant': 'Karachi Biryani House', 'name': 'Chicken Biryani', 'price': 450, 'description': 'Authentic Karachi style chicken biryani', 'category': 'Biryani'},
    {'restaurant': 'Karachi Biryani House', 'name': 'Beef Biryani', 'price': 550, 'description': 'Tender beef biryani', 'category': 'Biryani'},
    {'restaurant': 'Karachi Biryani House', 'name': 'Prawn Biryani', 'price': 650, 'description': 'Fresh prawn biryani', 'category': 'Biryani'},
    {'restaurant': 'Sweet Dreams Bakery', 'name': 'Chocolate Cake', 'price': 800, 'description': 'Rich chocolate cake', 'category': 'Cakes'},
    {'restaurant': 'Sweet Dreams Bakery', 'name': 'Vanilla Cake', 'price': 700, 'description': 'Classic vanilla cake', 'category': 'Cakes'},
    {'restaurant': 'Sweet Dreams Bakery', 'name': 'Cheesecake', 'price': 900, 'description': 'New York style cheesecake', 'category': 'Cakes'},
    {'restaurant': 'KFC Pakistan', 'name': '2 Piece Chicken Combo', 'price': 550, 'description': '2 pieces fried chicken with fries', 'category': 'KFC'},
    {'restaurant': 'KFC Pakistan', 'name': '5 Piece Chicken Combo', 'price': 1200, 'description': '5 pieces fried chicken', 'category': 'KFC'},
    {'restaurant': 'KFC Pakistan', 'name': 'Zinger Burger', 'price': 450, 'description': 'Crispy zinger patty burger', 'category': 'KFC'},
    {'restaurant': 'Dominos Pizza', 'name': 'Pepperoni Pizza Medium', 'price': 700, 'description': 'Classic pepperoni pizza', 'category': 'Dominos'},
    {'restaurant': 'Dominos Pizza', 'name': 'Chicken Tikka Pizza Large', 'price': 1000, 'description': 'Large pizza with chicken tikka', 'category': 'Dominos'},
    {'restaurant': 'Dominos Pizza', 'name': 'Veggie Pizza', 'price': 600, 'description': 'Fresh vegetables pizza', 'category': 'Dominos'},
]

items_created = 0
for item_data in menu_items_data:
    restaurant = restaurants[item_data.pop('restaurant')]
    category = categories[item_data.pop('category')]
    menu_item, created = MenuItem.objects.get_or_create(
        restaurant=restaurant,
        name=item_data['name'],
        defaults={**item_data, 'restaurant': restaurant, 'category': category}
    )
    if created:
        items_created += 1

print(f"   ✅ Menu items: {items_created} created/verified\n")

print("=" * 80)
print("✅ SETUP COMPLETE!")
print("=" * 80)
print("\n📊 System Status:")
print(f"  • Admin User: {admin_email}")
print(f"  • Restaurants: {Restaurant.objects.count()}")
print(f"  • Menu Items: {MenuItem.objects.count()}")
print(f"  • Categories: {Category.objects.count()}")
print("\n🚀 Now run your server:")
print("   python manage.py runserver")
print("\n🌐 Access your site at:")
print("   http://localhost:8000")
print("   http://localhost:8000/admin-dashboard.html")
print("   http://localhost:8000/dashboard-portal.html")
print("\n")