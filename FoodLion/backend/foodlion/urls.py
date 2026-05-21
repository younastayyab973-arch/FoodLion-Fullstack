from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from foodlion import frontend_views

urlpatterns = [
    # ── Root URL (Home) ──────────────────────────────────────────────────────
    path('', frontend_views.dashboard_portal, name='home'),

    # ── Frontend Pages ───────────────────────────────────────────────────────
    path('dashboard-portal.html', frontend_views.dashboard_portal, name='dashboard-portal'),
    path('dashboard/', frontend_views.dashboard_portal, name='dashboard'),
    path('admin-dashboard.html', frontend_views.admin_dashboard, name='admin-dashboard'),
    path('admin-login.html', frontend_views.admin_login, name='admin-login'),
    path('restaurant-panel.html', frontend_views.restaurant_panel, name='restaurant-panel'),
    path('menu-management.html', frontend_views.menu_management, name='menu-management'),
    path('order-management.html', frontend_views.order_management, name='order-management'),
    path('cart-management.html', frontend_views.cart_management, name='cart-management'),
    path('rider-panel.html', frontend_views.rider_panel, name='rider-panel'),
    path('customer-panel.html', frontend_views.customer_panel, name='customer-panel'),
    path('home.html', frontend_views.home, name='home-page'),
    path('about.html', frontend_views.about, name='about'),
    path('services.html', frontend_views.services, name='services'),
    path('contacts.html', frontend_views.contact, name='contact'),
    path('restaurants.html', frontend_views.restaurants, name='restaurants-list'),
    path('login.html', frontend_views.login_page, name='login'),
    path('signup.html', frontend_views.signup_page, name='signup'),

    # ── Alternative clean URLs ───────────────────────────────────────────────
    path('dashboard-portal/', frontend_views.dashboard_portal),
    path('admin-dashboard/', frontend_views.admin_dashboard),
    path('admin-login/', frontend_views.admin_login),
    path('restaurant-panel/', frontend_views.restaurant_panel),
    path('menu-management/', frontend_views.menu_management),
    path('order-management/', frontend_views.order_management),
    path('cart-management/', frontend_views.cart_management),
    path('rider-panel/', frontend_views.rider_panel),
    path('customer-panel/', frontend_views.customer_panel),

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

# Serve static files in development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static('/images/', document_root=str(settings.BASE_DIR.parent / 'images'))