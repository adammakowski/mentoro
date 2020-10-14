from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.views.decorators.cache import cache_page
import debug_toolbar


# Sentry SDK
def trigger_error(request):
    division_by_zero = 1 / 0


# Django Debug Toolbar
if bool(settings.DEBUG):
    import debug_toolbar

urlpatterns = [
    # sentry werify
    path('sentry-debug/', trigger_error),  # Sentry SDK
    path('__debug__/', include(debug_toolbar.urls)),  # Django Debug Toolbar https://github.com/jazzband/django-debug-toolbar
    # admin path
    path('admin/', admin.site.urls),
    # defender admin
    path('admin/defender/', include('defender.urls')),
    # Filepond
    path('fp/', include('django_drf_filepond.urls')),
    # Ckeditor uploader
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # sites path
    path('', include('home.urls')),
    # accounts app paths
    path('accounts/', include('accounts.urls')),
    # dashboard path
    path('dashboard/', include('dashboard.urls')),
    # Mentoro|Courses path
    path('courses/', include('courses.urls')),
    # Mentoro|Mentors path
    path('mentors/', include('mentors.urls')),
    # Mentoro|Library path
    path('library/', include('library.urls')),
    # Mentoro|Blog path
    path('blog/', include('blog.urls')),
    # Social Auth
    path('social/accounts/', include('allauth.urls')),
    # The two-step activation workflow
    path('accounts/', include('django_registration.backends.activation.urls')),
    # user authorizations
    path('accounts/login/', auth_views.LoginView.as_view(template_name='account_login.html'), name='account_login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='account_logout.html'), name='account_logout'),
    # user password change
    path('accounts/password_change', auth_views.PasswordChangeView.as_view(template_name='account_password_change.html'), name='account_password_change'),
    path('accounts/password_change_done', auth_views.PasswordChangeDoneView.as_view(template_name='account_password_change_done.html'), name='account_password_change_done'),
    # user password reset
    path('accounts/password_reset', auth_views.PasswordResetView.as_view(template_name='account_password_reset.html'), name='account_password_reset'),
    path('accounts/password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('accounts/password_reset_done', auth_views.PasswordResetDoneView.as_view(template_name='account_password_reset_done.html'), name='password_reset_done'),
    path('accounts/password_reset_complete', auth_views.PasswordResetCompleteView.as_view(template_name='account_password_reset_complete.html'), name='account_password_reset_complete'),
]
if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
