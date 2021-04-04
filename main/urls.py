from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('register/', views.RegisterForm.as_view(), name='register'),
  path('login/', views.LoginForm.as_view(), name='login'),
]