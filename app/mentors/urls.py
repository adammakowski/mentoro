from . import views
from django.urls import path
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('all', views.mentors_all, name='mentors_all'),
    path('mentor/<int:pk>/', views.mentors_detail, name='mentors_detail'),
    path('new', views.mentors_new, name='mentors_new'),
    path('add/success/', views.mentors_new_success, name='mentors_new_success'),
]