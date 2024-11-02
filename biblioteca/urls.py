from django.urls import path
from .views import BibliotecaView

urlpatterns = [
    path('biblioteca/', BibliotecaView.as_view(template_name='biblioteca/biblioteca.html'), name='biblioteca'),
]