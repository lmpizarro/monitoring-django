from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from app.models import MeetUP
from app.services import MeetUPInterface

class GetMeetupList(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request):

        MI = MeetUPInterface()

        meetups = MI.getActiveMeetUps()

        return Response({'error': False, 'data': meetups})

class GetMeetupDetails(APIView):

    def get(self, request, pk, format=None):

        MI = MeetUPInterface()

        data = {'error': True}
        meetup_detail = MI.getMeetUpsDetails(pk)

        if meetup_detail['error'] == False:
            data = meetup_detail

        return Response(data)

class GetMeetUpsToday(APIView):

    def get(self, request):
        MI = MeetUPInterface()

        data = MI.getMeetUpsToday()
        if data['error'] == False:
            return Response(data)
        else:
            return Response({'error': True})

