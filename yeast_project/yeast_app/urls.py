# yeast_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_purity/', views.get_purity, name='get_purity'),
]

