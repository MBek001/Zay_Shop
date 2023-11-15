from django.urls import path
from .views import *

urlpatterns = [
    path('', Homeview.as_view(), name='home'),
    path('about', about),
    path('shop', shop),
    path('contact', contact),
    path('shop-single', shop_single),
    path('register', register),
    path('forgot_password', fr_password),
    path('shopping_cart', ShoppingCartView.as_view(), name='shopping-cart'),
    path('add-product', AddproductView.as_view(), name='add-product'),
]



