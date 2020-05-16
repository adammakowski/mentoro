from django.urls import path
from . import views

urlpatterns = [
    path('all', views.courses_all, name='courses_all'),
    path('<int:pk>/', views.course_detail, name='course_detail'),
    path('new', views.course_new, name='course_new'),
    path('<int:pk>/edit/', views.course_edit, name='course_edit'),
]
