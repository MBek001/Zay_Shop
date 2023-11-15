from django.urls import path
from .views import *
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    LoginView
)

urlpatterns = [

    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginingView.as_view(), name='login'),
    path('logout', LogoutingView.as_view(), name='logout'),


]