from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
  path('register/', views.RegisterView.as_view(), name='register'),
  path('login/', auth_views.LoginView.as_view(template_name='flexer/login.html'), name='login'),
  path('profile/', views.ProfileView.as_view(), name='profile'),
  path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]