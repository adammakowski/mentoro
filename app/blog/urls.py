from . import views
from django.urls import path
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('all/', views.post_list, name='blog_all'),
    path('post/<int:pk>/', views.post_detail, name='blog_detail'),
    path('post/new/', views.post_new, name='blog_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='blog_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='blog_delete'),
    path('comment/success/', views.blog_comment_success, name='blog_comment_success'),
    path('category/', views.category_list, name='category_all'),
    path('category/<int:pk>/', views.category_detail, name='category_detail'),
]
