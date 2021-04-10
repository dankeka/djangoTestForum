from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
  path('', views.index, name='index'),
  path('register/', views.RegisterForm.as_view(), name='register'),
  path('login/', views.LoginForm.as_view(), name='login'),
  path('logout/', views.logout, name='logout'),
  path('section/<int:pk>/', views.section, name='section'),
  path('theme/<int:pk>/', views.theme, name='theme'),
  path('addMsg/', views.addMsg, name='addMsg'),
]