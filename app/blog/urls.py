from . import views
from django.urls import path
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('all/', views.post_list, name='blog_all'),
    path('post/<int:pk>/', views.post_detail, name='blog_detail'),
    path('new/', views.post_new, name='blog_new'),
    path('comment/success/', views.blog_comment_success, name='blog_comment_success'),
    path('category/', views.category_list, name='category_all'),
    path('category/<int:pk>/', views.category_detail, name='category_detail'),
]
