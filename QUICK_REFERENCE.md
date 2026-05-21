# 🍔 FoodLion - Quick Reference Guide

## ⚡ Quick Start (Copy-Paste)

```bash
# 1. Go to backend
cd e:\FoodLion\backend

# 2. Activate venv
venv\Scripts\activate

# 3. Setup database
python manage.py migrate

# 4. Add sample data
python setup_admin_data.py

# 5. Run server
python manage.py runserver

# 6. Open in browser
http://localhost:8000/dashboard-portal.html
```

---

## 🔐 Login Credentials

| Role | Email | Password |
|------|-------|----------|
| Admin | ray@gmail.com | Ray123 |

---

## 🌐 All URLs at a Glance

| Panel | URL | Purpose |
|-------|-----|---------|
| Dashboard Portal | `http://localhost:8000/dashboard-portal.html` | Navigation hub |
| Admin Dashboard | `http://localhost:8000/admin-dashboard.html` | Admin panel with hamburger menu |
| Restaurant Panel | `http://localhost:8000/restaurant-panel.html` | Restaurant operations |
| Menu Management | `http://localhost:8000/menu-management.html` | Menu CRUD |
| Order Management | `http://localhost:8000/order-management.html` | Order tracking |
| Cart Management | `http://localhost:8000/cart-management.html` | Cart analytics |
| Rider Panel | `http://localhost:8000/rider-panel.html` | Delivery tracking |
| Customer Panel | `http://localhost:8000/customer-panel.html` | Customer account |
| Admin Login | `http://localhost:8000/admin-login.html` | Authentication |
| Backend API | `http://localhost:8000/api/` | API endpoints |

---

## 📊 Dashboard Panels Summary

| # | Panel | Access | Purpose |
|---|-------|--------|---------|
| 1 | Admin Dashboard | Hamburger menu | Full system control |
| 2 | Restaurant Panel | Direct link | Restaurant operations |
| 3 | Menu Management | Direct link | Menu items CRUD |
| 4 | Order Management | Direct link | Order tracking |
| 5 | Cart Management | Direct link | Abandoned cart recovery |
| 6 | Rider Panel | Direct link | Delivery partner mgmt |
| 7 | Customer Panel | Direct link | Customer accounts |

---

## 🎯 Key Features by Panel

### Admin Dashboard
- Hamburger menu toggle
- 8 navigation sections
- User management
- Restaurant management
- Menu management
- Order management
- Rider management
- Customer management
- Cart management

### Restaurant Panel
- Real-time statistics
- Pending orders queue
- Menu management
- Order history
- Quick actions

### Menu Management
- Grid & table views
- Search & filter
- CRUD operations
- Stock tracking
- Bulk export

### Order Management
- Status filtering
- Order details
- Customer info
- Status updates
- Revenue tracking

### Cart Management
- Active cart monitoring
- Abandoned recovery
- Cart analytics
- Conversion metrics

### Rider Panel
- Earnings dashboard
- Active deliveries
- Performance metrics
- Delivery history

### Customer Panel
- Profile management
- Order history
- Saved addresses
- Account settings

---

## 📁 Important Files

| File | Purpose |
|------|---------|
| `backend/manage.py` | Django management |
| `backend/requirements.txt` | Python dependencies |
| `backend/setup_admin_data.py` | Sample data seeder |
| `admin-dashboard.html` | Main admin panel |
| `dashboard-portal.html` | Navigation hub |
| `SETUP_GUIDE.md` | Backend documentation |
| `README_ADMIN.md` | Admin guide |
| `COMPLETE_SYSTEM_SUMMARY.md` | Full system docs |

---

## 🔧 Common Commands

```bash
# Start server
python manage.py runserver

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Seed sample data
python setup_admin_data.py

# Activate venv
venv\Scripts\activate

# Install packages
pip install -r requirements.txt

# Access Django shell
python manage.py shell

# View logs
python manage.py runserver --verbosity 2
```

---

## 🎨 Color Scheme

| Component | Gradient |
|-----------|----------|
| Admin | #667eea → #764ba2 (Purple) |
| Restaurant | #4facfe → #00f2fe (Cyan) |
| Menu | #fa709a → #fee140 (Pink-Yellow) |
| Order | #667eea → #764ba2 (Purple) |
| Cart | #f093fb → #f5576c (Pink-Red) |
| Rider | #f093fb → #f5576c (Pink-Red) |
| Customer | #667eea → #764ba2 (Purple) |

---

## 📱 Responsive Design

- ✅ Desktop (1200px+)
- ✅ Tablet (768px - 1199px)
- ✅ Mobile (< 768px)
- ✅ Hamburger menu on small screens
- ✅ Touch-friendly buttons

---

## 🔗 API Endpoints Quick List

```
# Auth
POST   /api/auth/login/
POST   /api/auth/signup/
GET    /api/auth/profile/

# Restaurants
GET    /api/restaurants/
POST   /api/restaurants/

# Menu Items
GET    /api/menu-items/
POST   /api/menu-items/

# Orders
GET    /api/orders/
POST   /api/orders/

# Admin
GET    /api/admin/dashboard/
GET    /api/admin/restaurants/
GET    /api/admin/orders/
GET    /api/admin/users/
```

---

## 🚨 Troubleshooting

| Issue | Solution |
|-------|----------|
| Backend won't start | Check port 8000 is free, run `python manage.py runserver` |
| Login fails | Run `python setup_admin_data.py` to create admin user |
| API not responding | Ensure backend is running and URL is correct |
| CORS errors | Check `.env` CORS_ALLOWED_ORIGINS setting |
| 404 errors | Verify file paths and URLs are correct |
| Database errors | Run `python manage.py migrate` |

---

## 💾 Backup Important Files

```
- backend/.env (Configuration)
- backend/db.sqlite3 (Database)
- backend/setup_admin_data.py (Data script)
- All HTML files (Frontend)
```

---

## 🌟 Pro Tips

1. **Use Postman** - Test API endpoints before frontend
2. **Check Browser Console** - View errors with F12
3. **Enable Logging** - Add verbosity to Django commands
4. **Cache Clearing** - Ctrl+Shift+Delete in browser
5. **Mobile Testing** - Use Chrome DevTools device emulation
6. **Version Control** - Commit your changes to Git

---

## 📈 Performance Tips

- Lazy load images
- Paginate large lists
- Cache API responses
- Minify CSS/JS for production
- Use CDN for static files
- Enable database indexing

---

## 🔐 Security Checklist

- [ ] Change admin password in production
- [ ] Use HTTPS only
- [ ] Set DEBUG=False
- [ ] Update SECRET_KEY
- [ ] Configure CORS properly
- [ ] Validate all inputs
- [ ] Use environment variables
- [ ] Enable CSRF protection

---

## 📚 Documentation Files

| File | Contents |
|------|----------|
| SETUP_GUIDE.md | Backend setup & API docs |
| README_ADMIN.md | Admin panel guide |
| DASHBOARD_GUIDE.md | Dashboard system guide |
| COMPLETE_SYSTEM_SUMMARY.md | Full documentation |
| QUICK_REFERENCE.md | This file |

---

## 🎓 Next Steps

1. ✅ **Explore** - Test all 7 panels
2. ✅ **Learn** - Study the code structure
3. ✅ **Customize** - Update colors, data, features
4. ✅ **Integrate** - Add payment, email, SMS
5. ✅ **Deploy** - Push to production
6. ✅ **Monitor** - Set up logging & analytics

---

## 📞 Getting Help

1. **Check Documentation** - Read relevant guide
2. **Browser Console** - F12 to see errors
3. **Backend Logs** - Check Django terminal output
4. **Network Tab** - Inspect API requests
5. **Compare Sample** - Review working code

---

## 🎉 Summary

Your FoodLion system includes:

✅ **Complete Backend** - Django REST API
✅ **7 Dashboard Panels** - Full UI system
✅ **Authentication** - JWT + Admin login
✅ **Sample Data** - 4 restaurants, 12 items
✅ **Documentation** - Complete guides
✅ **Ready to Use** - Copy-paste to start

**Start in 1 minute:**
```bash
cd e:\FoodLion\backend && venv\Scripts\activate && python manage.py runserver
```

Then open: `http://localhost:8000/dashboard-portal.html`

---

**FoodLion v1.0 - Ready to Go! 🚀**
