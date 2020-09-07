from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_index, name='home_index'),
    path('pricing/', views.home_pricing, name='home_pricing'),
    path('courses/', views.home_courses, name='home_courses'),
    path('aboutus/', views.home_aboutus, name='home_aboutus'),
    path('salescharges/', views.home_salescharges, name='home_salescharges'),
    path('affiliate/', views.home_affiliate, name='home_affiliate'),
    path('support/', views.home_support, name='home_support'),
    path('privacypolicy/', views.home_privacypolicy, name='home_privacypolicy'),
    path('terms/mentors_instructions_and_regulations', views.mentors_instructions_and_regulations, name='mentors_instructions_and_regulations'),
]
