from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from app.services import MeetUPInterface


class GetMeetupList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):

        MI = MeetUPInterface()

        meetups = MI.getActiveMeetUps()

        return Response({'error': False, 'data': meetups, 'endpoint': 'get_meetup_list'})


class GetMeetupDetails(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk, format=None):

        MI = MeetUPInterface()

        data = {'error': True}
        meetup_detail = MI.getMeetUpsDetails(pk)

        if meetup_detail['error'] == False:
            data = meetup_detail

        data['endpoint'] = 'get_meetup_details'
        return Response(data)


class GetMeetUpsToday(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        MI = MeetUPInterface()

        data = MI.getMeetUpsToday()
        if data['error'] == False:
            data['endpoint'] = 'get_meetups_today'
        else:
            data = {'error': True, 'endpoint': 'get_meetups_today'}

        return Response(data)


class MeetupDetail(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request, format=None):
        MI = MeetUPInterface()

        meetup_id = MI.CreateMeetUP(request.data)

        data = {'endpoint': 'create_meetup', 'error': True}
        if meetup_id != None:
            data['error'] = False
            data['meeter_id'] = meetup_id

        return Response(data)

    def delete(self, request, pk, format=None):
        MI = MeetUPInterface()

        data = {'error': True, 'pk': pk}

        MI.DeleteMeetUp(pk)

        return Response(data)

class CreateMeeter(APIView):
    def post(self, request, format=None):
        MI = MeetUPInterface()

        meeter_id = MI.CreateMeeter(request.data)

        data = {'endpoint': 'create_meeter', 'error': True}
        if meeter_id != None:
            data['error'] = False
            data['meeter_id'] = meeter_id

        return Response(data)


class SubscribeMeetup(APIView):
    def post(self, request, format=None):

        MI = MeetUPInterface()

        data = {'endpoint': 'subscribe_meet_up', 'error': True}
        ret = MI.SubscribeMeetUp(request.data)

        if not ret['error']:
            data['error'] = False
            data['message'] = ret['message']

        return Response(data)


class UnsubscribeMeetUp(APIView):
    def post(self, request, format=None):
        print(request.data)

        data = {'endpoint': 'unsubscribe_meet_up', 'error': True}
        MI = MeetUPInterface()
        ret = MI.UnsubscribeMeetUp(request.data)

        if not ret['error']:
            data['error'] = False
            data['message'] = ret['message']
        return Response(request.data)


class Checkin(APIView):
    def post(self, request, format=None):
        data = {'endpoint': 'unsubscribe_meet_up', 'error': True, 'request': request.data}

        MI = MeetUPInterface()

        ret = MI.CheckinMeetUp(request.data)

        return Response(data)

class ConfirmCreateMeeter(APIView):
    pass

class ConfirmDeleteMeeter(APIView):
    pass
