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
# 1. Clone repository
git clone https://github.com/manahilaltaf20/FoodLion.git
cd FoodLion

# 2. Navigate to backend
cd backend

# 3. Create virtual environment
python -m venv venv

# 4. Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# 5. Install dependencies
pip install -r requirements.txt

# 6. Run migrations
python manage.py migrate

# 7. Seed sample data
python setup_admin_data.py

# 8. Start server
python manage.py runserver

# 9. Open in browser
http://localhost:8000/dashboard-portal.html
```

## 🔐 Admin Credentials

```
Email: ray@gmail.com
Password: Ray123
```

## 📊 Sample Data Included

- **4 Restaurants**: Karachi Biryani House, Sweet Dreams Bakery, KFC Pakistan, Dominos Pizza
- **12 Menu Items**: Biryani, Cakes, Fried Chicken, Pizza
- **Admin Account**: Pre-configured

## 🌐 API Endpoints

### Authentication
```
POST   /api/auth/login/          - User login
POST   /api/auth/signup/         - User registration
POST   /api/auth/logout/         - User logout
POST   /api/auth/refresh/        - Refresh token
GET    /api/auth/profile/        - Get user profile
```

### Restaurants
```
GET    /api/restaurants/         - List all restaurants
GET    /api/restaurants/<id>/    - Get restaurant detail
POST   /api/restaurants/         - Create restaurant (admin)
PUT    /api/restaurants/<id>/    - Update restaurant (admin)
```

### Menu Items
```
GET    /api/menu-items/          - List menu items
GET    /api/menu-items/<id>/     - Get menu item detail
POST   /api/menu-items/          - Create menu item (admin)
PUT    /api/menu-items/<id>/     - Update menu item (admin)
```

### Orders
```
GET    /api/orders/              - List user orders
POST   /api/orders/              - Create order
GET    /api/orders/<id>/         - Get order detail
PUT    /api/orders/<id>/         - Update order (admin)
```

### Admin
```
GET    /api/admin/dashboard/     - Dashboard statistics
GET    /api/admin/restaurants/   - Admin restaurant list
GET    /api/admin/orders/        - Admin order list
GET    /api/admin/users/         - Admin user list
```

## 📱 Dashboard URLs

| Panel | URL |
|-------|-----|
| Dashboard Portal | `/dashboard-portal.html` |
| Admin Dashboard | `/admin-dashboard.html` |
| Restaurant Panel | `/restaurant-panel.html` |
| Menu Management | `/menu-management.html` |
| Order Management | `/order-management.html` |
| Cart Management | `/cart-management.html` |
| Rider Panel | `/rider-panel.html` |
| Customer Panel | `/customer-panel.html` |

## 🏗️ Project Structure

```
FoodLion/
├── backend/
│   ├── manage.py
│   ├── requirements.txt
│   ├── .env
│   ├── setup_admin_data.py
│   ├── foodlion/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── authentication/      (User management)
│   ├── restaurants/         (Restaurant CRUD)
│   ├── menu_items/          (Menu management)
│   ├── orders/              (Order management)
│   └── adminpanel/          (Admin APIs)
├── admin-dashboard.html     (Main admin panel)
├── restaurant-panel.html    (Restaurant panel)
├── menu-management.html     (Menu CRUD)
├── order-management.html    (Order tracking)
├── cart-management.html     (Cart recovery)
├── rider-panel.html         (Rider dashboard)
├── customer-panel.html      (Customer accounts)
├── dashboard-portal.html    (Central hub)
└── [Documentation files]
```

## 🔧 Technology Stack

- **Backend**: Django 4.2, Django REST Framework
- **Database**: SQLite (development) / PostgreSQL (production)
- **Authentication**: JWT (PyJWT)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **API Protocol**: REST
- **CORS**: Enabled

## 📚 Documentation

- **README_ADMIN.md** - Complete admin guide
- **SETUP_GUIDE.md** - Backend setup documentation
- **QUICK_REFERENCE.md** - Quick reference guide
- **COMPLETE_SYSTEM_SUMMARY.md** - Full system documentation
- **PROJECT_COMPLETION.md** - Project completion checklist

## 🚀 Deployment

This project is configured for deployment on Railway.app, Render.com, or similar platforms.

### Environment Variables Required

```
DEBUG=False
SECRET_KEY=your-secret-key
JWT_SECRET=your-jwt-secret
ALLOWED_HOSTS=yourdomain.com
CORS_ALLOWED_ORIGINS=https://yourdomain.com
```

## 📝 License

MIT License - Feel free to use for your projects

## 👨‍💻 Author

Created with ❤️ by the FoodLion Team

## 🤝 Support

For issues and support, please open an issue on GitHub.

## 🎯 Future Enhancements

- [ ] Payment Gateway Integration (Stripe, JazzCash)
- [ ] Email Notifications
- [ ] Real-time WebSocket Updates
- [ ] Mobile App (React Native)
- [ ] Advanced Analytics Dashboard
- [ ] Multi-language Support
- [ ] Dark Mode UI
- [ ] API Rate Limiting

---

**FoodLion v1.0 - Ready to Go! 🚀**
