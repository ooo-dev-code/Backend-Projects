
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    
    path('product/<str:slug>/', views.product_detail, name="products"),
    path('product/<str:slug>/add_to_cart', views.add_to_cart, name="add_to_cart"),
    path('create_products/', views.create_products, name="create_products"),
    path('cart/', views.cart, name="cart"),
    
    path('index/', views.index, name="index"),
    path('bank/', views.add_get_bank_account, name="bank"),
        
]
