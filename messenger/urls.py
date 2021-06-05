from django.urls import path

from . import views

urlpatterns = [
 path('', views.login, name=''),
 path('register/', views.register, name='register'),
]
