from django.urls import path
from app import views
from app.views import meeters

from django.conf.urls import url

from rest_framework import permissions
from rest_framework.urlpatterns import format_suffix_patterns
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
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    path('hello/', views.HelloBeerService.as_view(), name='hellobeer'),
    # Devuelve la temperatura del momento
    path('temperature/', views.GetWeatherTemperature.as_view(), name='gettemperature'),
    # Devuelve la cantidad de botellas por personas a comprar en el momento
    path('bottlesByPerson/', views.GetBottlesByPerson.as_view(), name='bottleByPerson'),

    # devuelve las bottles_dada una cantidad meeters with the actual temperature
    path('get_bottles_meeters/<int:meeters>/', views.GetBottlesMeeters.as_view(), name='get_bottles_meeters'),

    # devuelve las bottles_dada una cantidad meeters with an arbitrary temperature
    path('get_bottles_meeters_temp/', views.GetBottlesMeetersTemp.as_view(), name='get_bottles_meeters_temp'),

    path('get_meetups_today/', meeters.GetMeetUpsToday.as_view(), name='get_meetups_today'),


    # get a list of active meetups
    path('getMeetUps/', meeters.GetMeetupList.as_view(), name='getMeetUps'),

    # get the details of a meetup by pk
    path('get_meetup_details/<int:pk>/', meeters.GetMeetupDetails.as_view(), name='get_meetup_details'),

    # create a meetup: only admin
    path('Meetup/', meeters.MeetupDetail.as_view(), name='create_meetup'),

    # delete a meetup by pk: only admin
    path('Meetup/<int:pk>/', meeters.MeetupDetail.as_view(), name='delete_meetup'),

    # create a meeter(user)
    path('create_meeter/', meeters.CreateMeeter.as_view(), name='create_meeter'),

    # TODO: a confirm create of a meeter, create_meeter send email with endpoint to confirm creation
    path('confirm_create_meeter/', meeters.ConfirmCreateMeeter.as_view(), name='confirm_create_meter'),

    # TODO: meeter delete (a meeter can delete itself) with email and endpoint confirmation
    path('confirm_delete_meeter/', meeters.ConfirmDeleteMeeter.as_view(), name='confirm_delete_meter'),

    # meeter register to a meetup
    path('subscribe_meetup/', meeters.SubscribeMeetup.as_view(), name='subscribe_meetup'),

    # TODO: a confirmation of subscription to a meetup??¿¿
    # TODO: a confirmation of unsubscription to a meetup??¿¿

    # meeter unsubscribe to a meetup
    path('unsubscribe_meetup/', meeters.UnsubscribeMeetUp.as_view(), name='unsubscribe_meetup'),

    # meeter checkin a meetup
    path('checkin/', meeters.Checkin.as_view(), name='checkin_meetup')
]

urlpatterns = format_suffix_patterns(urlpatterns)