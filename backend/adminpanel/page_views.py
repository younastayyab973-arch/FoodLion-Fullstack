from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test


def is_admin(user):
    return user.is_authenticated and user.is_admin_user


@user_passes_test(is_admin)
def admin_dashboard(request):
    return render(request, 'adminpanel/dashboard.html')
