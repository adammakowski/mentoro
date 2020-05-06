"""mentoro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from user import views as user_views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    # sentry werify
    path('sentry-debug/', trigger_error),
    # admin path
    path('admin/', admin.site.urls),
    # sites path
    path('', include('home.urls')),
    # users auth
    path('user/register/', user_views.register, name='user_register'),
    path('user/login/', auth_views.LoginView.as_view(template_name='user_login.html'), name='user_login'),
    path('user/logout/', auth_views.LogoutView.as_view(template_name='user_logout.html'), name='user_logout'),
    # user password change
    path('user/password_change', auth_views.PasswordChangeView.as_view(template_name='user_password_change.html'), name='password_change'),
    path('user/password_change_done', auth_views.PasswordChangeDoneView.as_view(template_name='user_password_change_done.html'), name='password_change_done'),
    # user password reset
    path('user/password_reset', auth_views.PasswordResetView.as_view(template_name='user_password_reset.html'), name='password_reset'),
    path('user/password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='user_password_reset_confirm.html'), name='password_reset_confirm'),
    path('user/password_reset_done', auth_views.PasswordResetDoneView.as_view(template_name='user_password_reset_done.html'), name='password_reset_done'),
    path('user/password_reset_complete', auth_views.PasswordResetCompleteView.as_view(template_name='user_password_reset_complete.html'), name='password_reset_complete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
