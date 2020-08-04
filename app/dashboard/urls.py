from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.dashboard_index, name='dashboard_index'),
    path('add/new', views.add_new, name='add_new'),
]
