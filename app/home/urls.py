from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.home_index, name='home_index'),
    path('courses/', views.home_courses, name='home_courses'),
    path('salescharges/', views.home_salescharges, name='home_salescharges'),
    path('affiliate/', views.home_affiliate, name='home_affiliate'),
]
