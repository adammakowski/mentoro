from django.urls import path
from . import views

urlpatterns = [
    path('all', views.blog_all, name='blog_all'),
    path('<int:pk>/', views.blog_detail, name='blog_detail'),
    path('new', views.blog_new, name='blog_new'),
    path('<int:pk>/edit/', views.blog_edit, name='blog_edit'),
]
