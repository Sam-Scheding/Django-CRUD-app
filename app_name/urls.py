"""crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'model'

urlpatterns = [
    path('', views.OverView.as_view(), name='overview'),
    path('create/', views.CreateModelView.as_view(), name='create'),
    path('update/<int:pk>/', views.UpdateModelView.as_view(), name='update'),
    path('delete/<int:pk>/', views.DeleteModelView.as_view(), name='delete'),
    path('details/<int:pk>/', views.ModelDetailsView.as_view(), name='details'),

]
