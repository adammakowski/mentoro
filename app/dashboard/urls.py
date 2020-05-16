from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.dashboard_index, name='dashboard_index'),
]
