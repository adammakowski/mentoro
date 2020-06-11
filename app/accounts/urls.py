from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.accounts_index, name='accounts_index'),
]
