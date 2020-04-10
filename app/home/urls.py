from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.home_index, name='home_index'),
]
