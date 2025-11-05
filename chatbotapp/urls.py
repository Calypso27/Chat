from django.urls import path
from . import views

app_name = 'chatbotapp'  # Ajouter un namespace

urlpatterns = [
    path('', views.home, name='home'),
    path('get_response/', views.get_response, name='get_response'),
]