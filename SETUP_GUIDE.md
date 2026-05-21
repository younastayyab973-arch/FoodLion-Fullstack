# FoodLion Admin Dashboard - Complete Setup Guide

## ✅ WHAT'S INCLUDED

Your FoodLion backend now has:

✓ Complete Django REST API
✓ User Authentication (JWT tokens)
✓ Restaurant Management
✓ Menu Items Management
✓ Order Management
✓ Admin Dashboard with APIs
✓ Sample Data (4 restaurants, 12 menu items)
✓ Admin User (ready to use)

---

## 🚀 QUICK START (After Backend Created)

### Step 1: Activate Virtual Environment & Install Dependencies
```bash
cd backend
venv\Scripts\activate
pip install -r requirements.txt
```

### Step 2: Run Migrations
```bash
python manage.py migrate
```

### Step 3: Seed Sample Data
```bash
python setup_admin_data.py
```

This creates:
- ✅ 4 Categories (Biryani, Cakes, KFC, Dominos)
- ✅ 4 Restaurants with details
- ✅ 12 Menu Items across restaurants
- ✅ Admin user (admin@foodlion.com / admin123)

### Step 4: Start Server
```bash
python manage.py runserver
```

Server runs at: **http://localhost:8000**

---

## 📱 API ENDPOINTS

### Authentication
- `POST /api/auth/signup/` - Register new user
- `POST /api/auth/login/` - Login user
- `POST /api/auth/logout/` - Logout
- `POST /api/auth/refresh/` - Refresh token
- `GET /api/auth/profile/` - Get user profile
- `PUT /api/auth/profile/` - Update profile

### Restaurants
- `GET /api/restaurants/` - List all restaurants
- `POST /api/restaurants/` - Create restaurant (admin)
- `GET /api/restaurants/<id>/` - Get restaurant detail
- `PUT /api/restaurants/<id>/` - Update restaurant (admin)

### Menu Items
- `GET /api/menu-items/` - List menu items
- `POST /api/menu-items/` - Create menu item (admin)
- `GET /api/menu-items/<id>/` - Get menu item detail
- `PUT /api/menu-items/<id>/` - Update menu item (admin)

### Orders
- `GET /api/orders/` - List user orders
- `POST /api/orders/` - Create order
- `GET /api/orders/<id>/` - Get order detail
- `PUT /api/orders/<id>/` - Update order (admin)

### Admin Dashboard
- `GET /api/admin/dashboard/` - Dashboard stats
- `GET /api/admin/restaurants/` - Admin restaurant list
- `GET /api/admin/orders/` - Admin order list
- `GET /api/admin/users/` - Admin user list

---

## 📊 SAMPLE DATA CREATED

### Categories
1. Biryani - Pakistani rice dishes
2. Cakes - Bakery items
3. KFC - Fried chicken
4. Dominos - Pizza

### Restaurants
1. **Karachi Biryani House** - Clifton, Karachi ⭐ 4.8
2. **Sweet Dreams Bakery** - Defence, Karachi ⭐ 4.6
3. **KFC Pakistan** - Gulshan-e-Iqbal, Karachi ⭐ 4.7
4. **Dominos Pizza** - Zamzama, Karachi ⭐ 4.5

### Menu Items (12 total)
- Chicken Biryani (Rs. 450)
- Beef Biryani (Rs. 550)
- Prawn Biryani (Rs. 650)
- Chocolate Cake (Rs. 800)
- Vanilla Cake (Rs. 700)
- Cheesecake (Rs. 900)
- 2 Piece Chicken Combo (Rs. 550)
- 5 Piece Chicken Combo (Rs. 1200)
- Zinger Burger (Rs. 450)
- Pepperoni Pizza Medium (Rs. 700)
- Chicken Tikka Pizza Large (Rs. 1000)
- Veggie Pizza (Rs. 600)

---

## 🔐 DEFAULT CREDENTIALS

### Admin User
- **Email:** admin@foodlion.com
- **Password:** admin123
- **Access:** http://localhost:8000/admin/

---

## 🧪 TEST THE API (Using Postman or cURL)

### 1. Login as Admin
```bash
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "email": "admin@foodlion.com",
    "password": "admin123"
  }'
```

Response:
```json
{
  "success": true,
  "user": {...},
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

### 2. Get Dashboard Stats (Use access_token)
```bash
curl http://localhost:8000/api/admin/dashboard/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

### 3. List Restaurants
```bash
curl http://localhost:8000/api/restaurants/
```

### 4. Create Order
```bash
curl -X POST http://localhost:8000/api/orders/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "delivery_address": "Karachi, Pakistan",
    "phone": "03001234567",
    "items": [
      {"menu_item_id": 1, "quantity": 2},
      {"menu_item_id": 3, "quantity": 1}
    ]
  }'
```

---

## 📝 ENVIRONMENT VARIABLES (.env)

Located in `backend/.env`:

```
DEBUG=True
SECRET_KEY=django-insecure-your-secret-key
JWT_SECRET=your-jwt-secret
ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:8000,http://localhost:3000
```

**For production:** Change DEBUG=False, use strong SECRET_KEY and JWT_SECRET

---

## 🛠️ ADMIN PANEL

Access Django Admin Panel:
- URL: `http://localhost:8000/admin/`
- Email: `admin@foodlion.com`
- Password: `admin123`

Features:
- Manage users
- Manage restaurants
- Manage menu items
- Manage orders
- View site activity

---

## 📦 PROJECT STRUCTURE

```
backend/
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables
├── db.sqlite3            # SQLite database
├── setup_admin_data.py   # Data seeding script
│
├── foodlion/             # Main project
│   ├── settings.py       # Django settings
│   ├── urls.py           # URL routing
│   └── wsgi.py           # WSGI config
│
├── authentication/       # User auth app
│   ├── models.py         # User model with JWT
│   ├── views.py          # Auth endpoints
│   └── serializers.py    # Data serializers
│
├── restaurants/          # Restaurant management
│   ├── models.py         # Restaurant & Category models
│   ├── views.py          # REST endpoints
│   └── serializers.py    # Serializers
│
├── menu_items/           # Menu management
│   ├── models.py         # MenuItem model
│   ├── views.py          # REST endpoints
│   └── serializers.py    # Serializers
│
├── orders/              # Order management
│   ├── models.py        # Order & OrderItem models
│   ├── views.py         # REST endpoints
│   └── serializers.py   # Serializers
│
└── adminpanel/          # Admin dashboard
    ├── api_views.py     # Admin API endpoints
    ├── permissions.py   # Admin permission checks
    └── urls.py          # Admin URLs
```

---

## 🔄 WORKFLOW EXAMPLE

### For End Users:
1. Signup: `POST /api/auth/signup/`
2. Login: `POST /api/auth/login/` → get access_token
3. Browse restaurants: `GET /api/restaurants/`
4. View menu items: `GET /api/menu-items/?restaurant=1`
5. Create order: `POST /api/orders/`
6. Track order: `GET /api/orders/<order_id>/`

### For Admin:
1. Login: `POST /api/auth/login/`
2. View dashboard: `GET /api/admin/dashboard/`
3. Manage restaurants: `GET/POST/PUT /api/admin/restaurants/`
4. Manage orders: `GET/PUT /api/admin/orders/`
5. Update order status: `PUT /api/admin/orders/<id>/`

---

## 🚀 NEXT STEPS

1. **Frontend Integration:** Connect your existing HTML/CSS/JS to these APIs
2. **Deploy:** Use Heroku, PythonAnywhere, or DigitalOcean
3. **Database:** Upgrade to PostgreSQL for production
4. **Email Notifications:** Add order confirmation emails
5. **Payment Integration:** Add Stripe/JazzCash payments
6. **Real-time Updates:** Add WebSockets for live order tracking

---

## ⚠️ TROUBLESHOOTING

### Issue: "ModuleNotFoundError: No module named 'django'"
**Fix:** Activate venv and run `pip install -r requirements.txt`

### Issue: "Port 8000 already in use"
**Fix:** Run server on different port: `python manage.py runserver 8001`

### Issue: "Database not found"
**Fix:** Run migrations: `python manage.py migrate`

### Issue: "No data showing"
**Fix:** Run seed script: `python setup_admin_data.py`

---

## 📞 SUPPORT

For issues or questions:
1. Check Django error messages carefully
2. Verify all packages are installed
3. Ensure database migrations are run
4. Check that .env file exists with correct values

---

**Your FoodLion backend is ready! 🎉**
Start the server and begin building your food delivery app!
