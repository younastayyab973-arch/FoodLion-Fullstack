"""
Complete FoodLion Django Backend Bootstrap
This script creates all directories and files needed for the Django backend
"""
import os
import json
from pathlib import Path


BASE_DIR = Path(__file__).parent
BACKEND_DIR = BASE_DIR / 'backend'

# File structure to create
FILES_TO_CREATE = {
    'requirements.txt': '''Django>=4.2
djangorestframework>=3.14
django-cors-headers>=4.3
PyJWT>=2.8
python-dotenv>=1.0
bcrypt>=4.0
''',
    '.env': '''# Django Configuration
DEBUG=True
SECRET_KEY=your-secret-key-here-change-in-production
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
    'restaurants/__init__.py': '',
    'menu_items/__init__.py': '',
    'orders/__init__.py': '',
    'adminpanel/__init__.py': '',
}


def create_files():
    """Create all necessary files."""
    BACKEND_DIR.mkdir(parents=True, exist_ok=True)
    
    for file_path, content in FILES_TO_CREATE.items():
        full_path = BACKEND_DIR / file_path
        full_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Created: {file_path}")


if __name__ == '__main__':
    print("Creating FoodLion Django Backend Structure...")
    print("=" * 70)
    
    try:
        create_files()
        print("=" * 70)
        print("✓ Django backend structure created successfully!")
        print(f"✓ Backend directory: {BACKEND_DIR}")
        print("\nNext steps:")
        print("  1. cd backend")
        print("  2. python -m venv venv")
        print("  3. venv\\Scripts\\activate  (Windows) or source venv/bin/activate (Linux/Mac)")
        print("  4. pip install -r requirements.txt")
        print("  5. cp .env.example .env  (and update with your settings)")
        print("  6. python manage.py migrate")
        print("  7. python manage.py runserver")
    except Exception as e:
        print(f"✗ Error: {e}")
        import traceback
        traceback.print_exc()
