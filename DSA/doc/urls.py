from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('dept/', views.dept, name='dept'),
    path('deptpage/<id>/', views.deptpage, name='deptapge'),
]
