from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login_leitor.html'), name='login'),
    path('login-admin/', auth_views.LoginView.as_view(template_name='users/login_adm.html'), name='login-admin'),
]