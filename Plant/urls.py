"""nurseryMarket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from . import views as plantHomeView
from .views import plantListView, plantDetailView, plantCreateView, plantUpdateView, plantDeleteView, managerPlantListView, myOrdersView, orderDetailView

urlpatterns = [
    path('', plantHomeView.home, name='plant-home'),
    path('cart/', plantHomeView.cartView , name='cart'),
    path('myorders/', plantHomeView.myOrdersView , name='myorders'),
    path('manager/<str:username>/', managerPlantListView.as_view(template_name='Plant/manager_plants.html'), name='manager-plants'),
    path('plants/', plantListView.as_view(), name='plant-list'),
    path('plant/<int:pk>/', plantDetailView.as_view(), name='plant-detail'),
    path('myorders/<int:pk>/', orderDetailView.as_view(), name='order-detail'),
    path('plant/<int:pk>/update/', plantUpdateView.as_view(), name='plant-update'),
    path('plant/<int:pk>/delete/', plantDeleteView.as_view(), name='plant-delete'),
    # path('myorders/<int:pk>/orderDelete/', orderDeleteView.as_view(), name='order-delete'),
    path('plant/new/', plantCreateView.as_view(), name='plant-create'),
]
