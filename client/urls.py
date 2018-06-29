from django.urls import path
from client import views

urlpatterns = [
    path('', views.Login.as_view()),
]