from django.urls import path
from django.contrib.auth import views as auth_views
from .views import CadUsuarioView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='users/login_leitor.html'), name='login'),
    path('login-admin/', auth_views.LoginView.as_view(
        template_name='users/login_adm.html'), name='login-admin'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('cadastro/', CadUsuarioView.as_view(template_name='users/cadastro.html'), name='cadastro')
]
