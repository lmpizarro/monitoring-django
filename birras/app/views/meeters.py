from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from app.models import MeetUP
from app.services import MeetUPInterface

class GetMeetup(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request):

        MI = MeetUPInterface()

        meetups = MI.getActiveMeetUps()

        return Response({'error': False, 'data': meetups})
