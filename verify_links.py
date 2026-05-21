# verify_links.py
"""Verification script for FoodLion frontend-backend integration.
Runs locally without deploying. It:
1. Scans all .html files under the project root for href, action, and JS endpoint patterns.
2. Loads Django URL patterns from the project's URL configuration.
3. Compares frontend URLs with backend routes and reports mismatches.
4. Uses Django's test client to perform GET requests on each backend endpoint to ensure a 200 response.
5. Checks that the admin dashboard page loads and that the /admin/ URL is reachable.
6. Writes a detailed report to `LINK_VERIFICATION_REPORT.md`.
"""

import os
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Django setup
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent
# Ensure the project root and backend directory are on sys.path
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
backend_path = PROJECT_ROOT / 'backend'
if str(backend_path) not in sys.path:
    sys.path.insert(0, str(backend_path))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'foodlion.settings')
# Ensure testserver is allowed for the test client
import django

django.setup()
from django.conf import settings
if hasattr(settings, 'ALLOWED_HOSTS'):
    if 'testserver' not in settings.ALLOWED_HOSTS:
        settings.ALLOWED_HOSTS.append('testserver')


from django.urls import get_resolver, URLPattern, URLResolver
from django.test import Client

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def flatten_urlpatterns(resolver, prefix=''):
    """Recursively collect all URL patterns (including those from included apps).
    Returns a list of full path strings (without the leading '^' or trailing '$').
    """
    patterns = []
    for p in resolver.url_patterns:
        if isinstance(p, URLPattern):
            pattern = prefix + p.pattern.regex.pattern
            # Strip regex tokens that Django adds (e.g., ^, $)
            pattern = pattern.lstrip('^').rstrip('$')
            patterns.append(pattern)
        elif isinstance(p, URLResolver):
            nested_prefix = prefix + p.pattern.regex.pattern
            patterns.extend(flatten_urlpatterns(p, nested_prefix))
    return patterns

def extract_frontend_urls(html_path):
    """Return a set of URLs found in <a href>, <form action>, and simple JS fetch strings.
    This is a lightweight extraction using regex; it captures relative URLs.
    """
    urls = set()
    content = html_path.read_text(encoding='utf-8')
    # href="..."
    for match in re.findall(r'href\s*=\s*"([^"]+)"', content, re.IGNORECASE):
        if not match.startswith('http'):
            urls.add(match.split('?')[0].split('#')[0])
    # action="..."
    for match in re.findall(r'action\s*=\s*"([^"]+)"', content, re.IGNORECASE):
        if not match.startswith('http'):
            urls.add(match.split('?')[0].split('#')[0])
    # simple fetch('/api/...') or $.ajax({url: '/api/...'} )
    for match in re.findall(r'fetch\s*\(\s*"([^\"]+)"', content):
        if not match.startswith('http'):
            urls.add(match.split('?')[0].split('#')[0])
    for match in re.findall(r'url\s*:\s*"([^\"]+)"', content):
        if not match.startswith('http'):
            urls.add(match.split('?')[0].split('#')[0])
    return urls

def normalize_path(path):
    """Remove leading/trailing slashes for easier comparison."""
    return path.strip('/')

# ---------------------------------------------------------------------------
# Main verification logic
# ---------------------------------------------------------------------------
def main():
    report_lines = []
    # 1. Gather backend routes
    resolver = get_resolver()
    backend_routes = set(normalize_path(p) for p in flatten_urlpatterns(resolver))
    report_lines.append('## Backend Routes (extracted from Django)')
    for r in sorted(backend_routes):
        report_lines.append(f'- {r}')
    report_lines.append('')

    # 2. Scan frontend HTML files
    html_files = list(PROJECT_ROOT.rglob('*.html'))
    report_lines.append('## Frontend HTML Files Scanned')
    for f in html_files:
        report_lines.append(f'- {f.relative_to(PROJECT_ROOT)}')
    report_lines.append('')

    # 3. Extract URLs from each HTML file
    frontend_urls = set()
    file_url_map = {}
    for html in html_files:
        urls = extract_frontend_urls(html)
        normalized = {normalize_path(u) for u in urls}
        frontend_urls.update(normalized)
        file_url_map[html] = normalized

    # 4. Compare sets
    missing_backend = frontend_urls - backend_routes
    missing_frontend = backend_routes - frontend_urls

    report_lines.append('## URLs present in frontend but missing in backend')
    if missing_backend:
        for u in sorted(missing_backend):
            report_lines.append(f'- {u}')
    else:
        report_lines.append('None')
    report_lines.append('')

    report_lines.append('## Backend routes not referenced by frontend')
    if missing_frontend:
        for u in sorted(missing_frontend):
            report_lines.append(f'- {u}')
    else:
        report_lines.append('None')
    report_lines.append('')

    # 5. Test each backend route with Django test client (GET only for simplicity)
    client = Client()
    report_lines.append('## Backend Route GET Request Results')
    for route in sorted(backend_routes):
        path = '/' + route if not route.startswith('/') else route
        try:
            response = client.get(path)
            status = response.status_code
        except Exception as e:
            status = f'Error: {e}'
        report_lines.append(f'- `{path}` → {status}')
    report_lines.append('')

    # 6. Admin dashboard checks
    report_lines.append('## Admin Dashboard Checks')
    admin_dashboard_path = PROJECT_ROOT / 'admin-dashboard.html'
    if admin_dashboard_path.exists():
        report_lines.append('- admin-dashboard.html file exists')
        # Simple check that it contains reference to /admin/ URL
        content = admin_dashboard_path.read_text(encoding='utf-8')
        if '/admin/' in content:
            report_lines.append('- Contains `/admin/` link')
        else:
            report_lines.append('- Missing `/admin/` link')
    else:
        report_lines.append('- admin-dashboard.html NOT FOUND')

    # Test Django admin URL
    admin_response = client.get('/admin/')
    report_lines.append(f'- `/admin/` GET status: {admin_response.status_code}')

    # Write report
    report_path = PROJECT_ROOT / 'LINK_VERIFICATION_REPORT.md'
    report_path.write_text('\n'.join(report_lines), encoding='utf-8')
    print(f'Report written to {report_path}')

if __name__ == '__main__':
    main()
