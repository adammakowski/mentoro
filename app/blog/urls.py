from . import views
from django.urls import path
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('all', views.post_list, name='blog_all'),
    path('<slug:slug>/', views.post_detail, name='blog_detail'),
    path('comment/success/', views.blog_comment_success, name='blog_comment_success'),
]