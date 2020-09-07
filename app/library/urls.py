from django.urls import path
from . import views

urlpatterns = [
    path('all', views.LibraryList.as_view(), name='library_all'),
    path('<slug:slug>/', views.library_detail, name='library_detail'),
    path('new', views.library_new, name='library_new'),
    path('<int:pk>/edit/', views.library_edit, name='library_edit'),
]
