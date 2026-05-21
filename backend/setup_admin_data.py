#!/usr/bin/env python
"""
Complete FoodLion Setup and Data Seeding Script
Run this after: python manage.py migrate
"""
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'foodlion.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from django.contrib.auth import get_user_model
from restaurants.models import Restaurant, Category
from menu_items.models import MenuItem

User = get_user_model()

def create_categories():
    """Create food categories."""
    categories_data = [
        ('Biryani', 'Delicious Pakistani biryani dishes'),
        ('Cakes', 'Fresh and delicious cakes'),
        ('KFC', 'Fried chicken and sides'),
        ('Dominos', 'Pizza and Italian food'),
    ]
    
    for name, description in categories_data:
        category, created = Category.objects.get_or_create(
            name=name,
            defaults={'description': description}
        )
        if created:
            print(f"✓ Created category: {name}")
    
    return {c.name: c for c in Category.objects.all()}


def create_restaurants(categories):
    """Create restaurants."""
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
        restaurant, created = Restaurant.objects.get_or_create(
            name=rest_data['name'],
            defaults={**rest_data, 'category': categories[category_name]}
        )
        restaurants[rest_data['name']] = restaurant
        if created:
            print(f"✓ Created restaurant: {rest_data['name']}")
    
    return restaurants


def create_menu_items(restaurants, categories):
    """Create menu items."""
    menu_items_data = [
        # Biryani
        {
            'restaurant': 'Karachi Biryani House',
            'name': 'Chicken Biryani',
            'price': 450,
            'description': 'Authentic Karachi style chicken biryani',
            'category': 'Biryani',
        },
        {
            'restaurant': 'Karachi Biryani House',
            'name': 'Beef Biryani',
            'price': 550,
            'description': 'Tender beef biryani',
            'category': 'Biryani',
        },
        {
            'restaurant': 'Karachi Biryani House',
            'name': 'Prawn Biryani',
            'price': 650,
            'description': 'Fresh prawn biryani',
            'category': 'Biryani',
        },
        # Cakes
        {
            'restaurant': 'Sweet Dreams Bakery',
            'name': 'Chocolate Cake',
            'price': 800,
            'description': 'Rich chocolate cake',
            'category': 'Cakes',
        },
        {
            'restaurant': 'Sweet Dreams Bakery',
            'name': 'Vanilla Cake',
            'price': 700,
            'description': 'Classic vanilla cake',
            'category': 'Cakes',
        },
        {
            'restaurant': 'Sweet Dreams Bakery',
            'name': 'Cheesecake',
            'price': 900,
            'description': 'New York style cheesecake',
            'category': 'Cakes',
        },
        # KFC
        {
            'restaurant': 'KFC Pakistan',
            'name': '2 Piece Chicken Combo',
            'price': 550,
            'description': '2 pieces fried chicken with fries',
            'category': 'KFC',
        },
        {
            'restaurant': 'KFC Pakistan',
            'name': '5 Piece Chicken Combo',
            'price': 1200,
            'description': '5 pieces fried chicken',
            'category': 'KFC',
        },
        {
            'restaurant': 'KFC Pakistan',
            'name': 'Zinger Burger',
            'price': 450,
            'description': 'Crispy zinger patty burger',
            'category': 'KFC',
        },
        # Pizza
        {
            'restaurant': 'Dominos Pizza',
            'name': 'Pepperoni Pizza Medium',
            'price': 700,
            'description': 'Classic pepperoni pizza',
            'category': 'Dominos',
        },
        {
            'restaurant': 'Dominos Pizza',
            'name': 'Chicken Tikka Pizza Large',
            'price': 1000,
            'description': 'Large pizza with chicken tikka',
            'category': 'Dominos',
        },
        {
            'restaurant': 'Dominos Pizza',
            'name': 'Veggie Pizza',
            'price': 600,
            'description': 'Fresh vegetables pizza',
            'category': 'Dominos',
        },
    ]
    
    count = 0
    for item_data in menu_items_data:
        restaurant = restaurants[item_data.pop('restaurant')]
        category = categories[item_data.pop('category')]
        
        menu_item, created = MenuItem.objects.get_or_create(
            restaurant=restaurant,
            name=item_data['name'],
            defaults={**item_data, 'restaurant': restaurant, 'category': category}
        )
        if created:
            print(f"✓ Created menu item: {item_data['name']}")
            count += 1
    
    return count


def create_admin_user():
    """Create admin user."""
    admin_user, created = User.objects.get_or_create(
        email='ray@gmail.com',
        defaults={
            'first_name': 'Ray',
            'last_name': 'Admin',
            'is_staff': True,
            'is_superuser': True,
            'is_admin_user': True,
        }
    )
    if created:
        admin_user.set_password('Ray123')
        admin_user.save()
        print(f"✓ Created admin user: ray@gmail.com (password: Ray123)")
    
    return admin_user


def main():
    """Run setup."""
    print("\n" + "=" * 70)
    print("FoodLion Database Setup and Seeding")
    print("=" * 70 + "\n")
    
    print("Creating categories...")
    categories = create_categories()
    
    print("\nCreating restaurants...")
    restaurants = create_restaurants(categories)
    
    print("\nCreating menu items...")
    create_menu_items(restaurants, categories)
    
    print("\nCreating admin user...")
    create_admin_user()
    
    print("\n" + "=" * 70)
    print("✓ Setup Complete!")
    print("=" * 70)
    print("\nAdmin Dashboard Login:")
    print("  Email: ray@gmail.com")
    print("  Password: Ray123")
    print("\nAccess admin panel at: http://localhost:8000/admin-panel/")
    print()


if __name__ == '__main__':
    main()
