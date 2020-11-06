from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # dashboard
    path('dashboard', views.account_dashboard, name='account_dashboard'),
    # user authorizations
    path('signup', views.account_signup, name='account_signup'),
    path('login', auth_views.LoginView.as_view(template_name='account_login.html'), name='account_login'),
    path('logout', auth_views.LogoutView.as_view(template_name='account_logout.html'), name='account_logout'),
    # user password change
    path('password_change', auth_views.PasswordChangeView.as_view(template_name='account_password_change.html'), name='account_password_change'),
    path('password_change_done', auth_views.PasswordChangeDoneView.as_view(template_name='account_password_change_done.html'), name='account_password_change_done'),
    # user password reset
    path('password_reset', auth_views.PasswordResetView.as_view(template_name='account_password_reset.html'), name='account_password_reset'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_done', auth_views.PasswordResetDoneView.as_view(template_name='account_password_reset_done.html'), name='password_reset_done'),
    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(template_name='account_password_reset_complete.html'), name='account_password_reset_complete'),

    path('', views.accounts_index, name='accounts_index'),
    path('login/account_locked/', views.account_locked, name='account_locked'),
    # Public user profile
    path('public/<int:pk>/', views.public_detail, name='public_detail'),
    path('public/<int:pk>/edit/', views.public_profile_edit, name='public_profile_edit'),
    # account my blog
    path('my_blog/', views.account_my_blog, name='account_my_blog'),
]
