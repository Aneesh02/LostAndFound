from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lost/', views.lost, name='lost'),
    path('found/', views.found, name='found'),
]