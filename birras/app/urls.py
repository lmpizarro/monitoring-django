from django.urls import path
from app import views

urlpatterns = [
    path('hello/', views.HelloBeerService.as_view(), name='hellobeer'),
    path('temperature/', views.GetWeatherTemperature.as_view(), name='gettemperature'),
    path('bottlesByPerson/', views.GetBottlesByPerson.as_view(), name='bottleByPerson'),
]
