from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_index, name='home_index'),
    path('pricing/', views.home_pricing, name='home_pricing'),
    path('courses/', views.home_courses, name='home_courses'),
    path('aboutus/', views.home_aboutus, name='home_aboutus'),
    path('salescharges/', views.home_salescharges, name='home_salescharges'),
    path('affiliate/', views.home_affiliate, name='home_affiliate'),
]
