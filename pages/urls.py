from django.urls import path
from .views import HomePage, BibliotecaPage

urlpatterns = [
    path('', HomePage.as_view(), name='inicio'),
    path('biblioteca/', BibliotecaPage.as_view(), name='biblioteca')
]