from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_index, name='dashboard_index'),
    path('add/new/', views.add_new, name='add_new'),
    path('public/profile/', views.dashboard_public_profile, name='dashboard_public_profile'),
]
