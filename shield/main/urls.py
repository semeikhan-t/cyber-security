from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('password-generator/', views.PasswordGeneratorView.as_view(), name='password-gen'),
    path('encryption/', views.EncryptionView.as_view(), name='encryption'),
    path('registration/', views.UserRegistration.as_view(), name='registration'),
    path('login', views.UserLogin.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout')
]
