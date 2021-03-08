from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.RegisterApi.as_view()),
]


