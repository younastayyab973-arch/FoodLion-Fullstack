# 🚀 FoodLion - Live Hosting & Deployment Guide

## ✅ QUICK LINKS

Your GitHub repository is ready:
👉 **GitHub**: https://github.com/manahilaltaf20/FoodLion

---

## 🌐 DEPLOYMENT OPTIONS

### **Option 1: Railway.app (RECOMMENDED - Easiest)**

#### Step 1: Go to Railway.app
1. Open: https://railway.app
2. Click **"Start a New Project"**
3. Select **"Deploy from GitHub"**

#### Step 2: Connect GitHub
1. Authorize Railway to access your GitHub
2. Select repository: **manahilaltaf20/FoodLion**
3. Click **"Deploy Now"**

#### Step 3: Set Environment Variables
Railway will ask for environment variables. Add these:

```
DEBUG=False
SECRET_KEY=django-insecure-your-production-secret-key-here
JWT_SECRET=your-jwt-secret-key-here
ALLOWED_HOSTS=*.railway.app,yourdomain.com
CORS_ALLOWED_ORIGINS=https://yourdomain.railway.app
DATABASE_URL=postgresql://... (Railway auto-generates this)
```

#### Step 4: Wait for Deployment
- Railway automatically detects Procfile
- Builds and deploys your app
- Takes ~3-5 minutes

#### Step 5: Get Your Public URL
After deployment completes:
1. Go to your Railway project dashboard
2. Click on your web service
3. Copy the **Public URL**

Example: `https://foodlion-production.up.railway.app`

---

### **Option 2: Render.com**

#### Step 1: Create Account
1. Go to: https://render.com
2. Sign up (or login with GitHub)

#### Step 2: Connect Repository
1. Click **"New +"**
2. Select **"Web Service"**
3. Connect your GitHub repository
4. Select: **manahilaltaf20/FoodLion**

#### Step 3: Configure Build
1. **Name**: `foodlion`
2. **Runtime**: `Python 3.11`
3. **Build Command**: 
   ```
   cd backend && pip install -r requirements_prod.txt && python manage.py migrate && python manage.py collectstatic --noinput
   ```
4. **Start Command**: 
   ```
   cd backend && gunicorn foodlion.wsgi
   ```

#### Step 4: Set Environment Variables
Add these in Render dashboard:

```
DEBUG=False
SECRET_KEY=your-production-secret-key
JWT_SECRET=your-jwt-secret
ALLOWED_HOSTS=*.onrender.com,yourdomain.com
CORS_ALLOWED_ORIGINS=https://yourdomain.onrender.com
DATABASE_URL=postgresql://... (get from Render PostgreSQL)
```

#### Step 5: Deploy
- Click **"Create Web Service"**
- Render auto-deploys from GitHub pushes
- Takes ~5-10 minutes

---

### **Option 3: Heroku (Paid)**

#### Requirements
1. Heroku account: https://www.heroku.com
2. Heroku CLI installed

#### Deployment
```bash
# Install Heroku CLI and login
heroku login

# Create app
heroku create foodlion-app

# Set environment variables
heroku config:set DEBUG=False
heroku config:set SECRET_KEY=your-production-secret-key
heroku config:set JWT_SECRET=your-jwt-secret
heroku config:set DATABASE_URL=postgresql://...

# Deploy from GitHub
git push heroku main

# Run migrations
heroku run "cd backend && python manage.py migrate"

# Get URL
heroku open
```

---

## 📋 ENVIRONMENT VARIABLES EXPLAINED

| Variable | What to use | Example |
|----------|------------|----------|
| `DEBUG` | Must be `False` | `False` |
| `SECRET_KEY` | Strong random string | `django-insecure-abc123xyz789...` |
| `JWT_SECRET` | Random string for tokens | `jwt-secret-key-12345` |
| `ALLOWED_HOSTS` | Your domain + platform domain | `foodlion.onrender.com,yourdomain.com` |
| `CORS_ALLOWED_ORIGINS` | Frontend URL | `https://yourdomain.onrender.com` |
| `DATABASE_URL` | Connection string (auto on Railway/Render) | `postgresql://user:pass@host:5432/db` |

---

## 🔑 GENERATE SECURE KEYS

### Generate SECRET_KEY:
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

### Generate JWT_SECRET:
```python
import secrets
print(secrets.token_urlsafe(50))
```

---

## ✅ VERIFICATION CHECKLIST

After deployment, verify everything works:

- [ ] App deployed successfully (no errors in logs)
- [ ] Visit public URL in browser
- [ ] Dashboard portal loads: `{public_url}/dashboard-portal.html`
- [ ] Admin login works with: `ray@gmail.com` / `Ray123`
- [ ] Can access all dashboard panels
- [ ] API endpoints respond at: `{public_url}/api/`

### Test with cURL:
```bash
# Replace with your public URL
curl https://your-app-url.herokuapp.com/api/restaurants/
```

Should return JSON with restaurants list (no auth needed for this endpoint).

---

## 🔗 YOUR LIVE LINKS (After Deployment)

Once deployed, your application will be accessible at:

### On Railway.app:
- Public URL: `https://your-app-name-production.up.railway.app`
- Dashboard: `https://your-app-name-production.up.railway.app/dashboard-portal.html`
- API: `https://your-app-name-production.up.railway.app/api/`

### On Render.com:
- Public URL: `https://your-app-name.onrender.com`
- Dashboard: `https://your-app-name.onrender.com/dashboard-portal.html`
- API: `https://your-app-name.onrender.com/api/`

### On Heroku:
- Public URL: `https://your-app-name.herokuapp.com`
- Dashboard: `https://your-app-name.herokuapp.com/dashboard-portal.html`
- API: `https://your-app-name.herokuapp.com/api/`

---

## 🚨 TROUBLESHOOTING

### "502 Bad Gateway" Error
- Check environment variables are set
- Verify database connection string
- Check build logs for errors
- Ensure `SECRET_KEY` and `JWT_SECRET` are set

### "ModuleNotFoundError" During Build
- Verify `requirements_prod.txt` has all dependencies
- Check build command runs migrations

### "ALLOWED_HOSTS" Error
- Add your deployment URL to `ALLOWED_HOSTS` environment variable

### Database Not Created
- Manually run migrations via dashboard console:
  ```bash
  cd backend && python manage.py migrate
  ```

### Static Files Not Loading
- Run collectstatic:
  ```bash
  python manage.py collectstatic --noinput
  ```

---

## 📱 TESTING PRODUCTION

### Test Admin Login
```bash
curl -X POST https://your-app-url/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"email":"ray@gmail.com","password":"Ray123"}'
```

### Test API Endpoints
```bash
# Get all restaurants
curl https://your-app-url/api/restaurants/

# Get menu items
curl https://your-app-url/api/menu-items/

# Get dashboard stats (requires token)
curl -H "Authorization: Bearer YOUR_TOKEN" \
  https://your-app-url/api/admin/dashboard/
```

---

## 🔄 CONTINUOUS DEPLOYMENT

All platforms support automatic deployment from GitHub:

1. Push changes to GitHub:
   ```bash
   git add .
   git commit -m "Your message"
   git push origin main
   ```

2. Your platform automatically:
   - Detects the push
   - Builds the app
   - Runs tests (if configured)
   - Deploys to production

3. Your app updates live in ~2-5 minutes

---

## 💾 BACKUP & DATA

### Before Deploying
- Export your local database if needed:
  ```bash
  python manage.py dumpdata > backup.json
  ```

### Production Database
- Use PostgreSQL instead of SQLite
- Most platforms provide automatic backups
- Enable encryption at rest

---

## 🎯 NEXT STEPS

1. **Deploy Now**: Choose one of the 3 options above
2. **Test Thoroughly**: Verify all features work
3. **Monitor Logs**: Watch for errors in deployment logs
4. **Set Up Monitoring**: Enable logging and alerts
5. **Scale as Needed**: Increase resources if traffic grows

---

## 🆘 GETTING HELP

### Check These Files
- `SETUP_GUIDE.md` - Backend configuration
- `README.md` - Project overview
- `QUICK_REFERENCE.md` - Quick commands

### Check Logs
- Railway: Dashboard → Logs tab
- Render: Dashboard → Logs tab
- Heroku: `heroku logs --tail`

### GitHub Issues
Open an issue on GitHub: https://github.com/manahilaltaf20/FoodLion/issues

---

## 📝 DEPLOYMENT SUMMARY

**Your app is ready to deploy!**

✅ GitHub repository created and code pushed
✅ Deployment files configured (Procfile, requirements.txt)
✅ Environment variables documented
✅ All 3 deployment options ready

**Choose your platform and deploy in 5 minutes! 🚀**

---

**FoodLion v1.0 - Live Hosting Ready! 🍔**