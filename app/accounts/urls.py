from django.urls import path
from . import views

urlpatterns = [
    path('', views.accounts_index, name='accounts_index'),
    path('login/account_locked/', views.account_locked, name='account_locked'),
]
