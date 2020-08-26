from django.urls import path
from app import views

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
]
