from django.urls import path
from app import views
from app.views import meeters

from django.conf.urls import url

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


 
urlpatterns = [
    path('hello/', views.HelloBeerService.as_view(), name='hellobeer'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('temperature/', views.GetWeatherTemperature.as_view(), name='gettemperature'),
    path('bottlesByPerson/', views.GetBottlesByPerson.as_view(), name='bottleByPerson'),
    path('getMeetUps/', meeters.GetMeetup.as_view(), name='getMeetUps'),
]
