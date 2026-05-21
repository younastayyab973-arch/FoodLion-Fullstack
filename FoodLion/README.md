# 🍔 FoodLion - Complete Food Delivery Management System

A modern, full-stack food delivery platform built with Django REST API and responsive HTML5/CSS3/JavaScript frontend.

## ✨ Features

### Backend (Django REST API)
- ✅ JWT Authentication System
- ✅ User Management (Admin, Restaurants, Riders, Customers)
- ✅ Restaurant Management (CRUD)
- ✅ Menu Items Management (CRUD)
- ✅ Order Management System
- ✅ Admin Dashboard APIs
- ✅ CORS Configured

### Frontend (7 Dashboard Panels)
- ✅ **Admin Dashboard** - System administration with hamburger menu
- ✅ **Restaurant Panel** - Restaurant operations
- ✅ **Menu Management** - Advanced menu CRUD
- ✅ **Order Management** - Order tracking
- ✅ **Cart Management** - Abandoned cart recovery
- ✅ **Rider Panel** - Delivery partner management
- ✅ **Customer Panel** - Customer accounts

## 🚀 Quick Start

### Local Development

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python setup_admin_data.py
python manage.py runserver
```

Access at: http://localhost:8000/dashboard-portal.html

## 🔐 Admin Credentials

Email: ray@gmail.com
Password: Ray123

## 📊 Dashboard Panels

1. Admin Dashboard - `/admin-dashboard.html`
2. Restaurant Panel - `/restaurant-panel.html`
3. Menu Management - `/menu-management.html`
4. Order Management - `/order-management.html`
5. Cart Management - `/cart-management.html`
6. Rider Panel - `/rider-panel.html`
7. Customer Panel - `/customer-panel.html`
8. Dashboard Portal - `/dashboard-portal.html` (Hub)

## 🛠️ Technology Stack

- Django 4.2 + Django REST Framework
- JWT Authentication
- SQLite/PostgreSQL
- HTML5 + CSS3 + Vanilla JavaScript
- CORS Enabled

## 📚 Documentation

- README_ADMIN.md - Admin guide
- SETUP_GUIDE.md - Backend setup
- QUICK_REFERENCE.md - Quick reference
- COMPLETE_SYSTEM_SUMMARY.md - Full docs

---

**FoodLion v1.0 - Ready to Deploy! 🚀**