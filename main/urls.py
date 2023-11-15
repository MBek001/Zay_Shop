from django.urls import path
from .views import *
from django.views.decorators.csrf import csrf_exempt

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
    #API
    path('increment', csrf_exempt(IncrementCountAPIView.as_view()), name='increment'),
    path('decrement', csrf_exempt(DecrementCountAPIView.as_view()), name='decrement'),
    path('change', csrf_exempt(ChangeCountAPIView.as_view()), name='change'),
]



