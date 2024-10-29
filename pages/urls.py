from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),      # Добавляем корневой URL
    path('data/', views.data, name='data'),
    path('test/', views.test, name='test'),
]
