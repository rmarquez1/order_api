from django.urls import path
from menu import views

urlpatterns = [
    path('', views.MenuView.as_view()),
]