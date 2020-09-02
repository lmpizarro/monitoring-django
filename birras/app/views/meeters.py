from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from app.services import MeetUPInterface

meetup_interface = MeetUPInterface()


class GetMeetupList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):


        meetups = meetup_interface.getActiveMeetUps()

        return Response({'error': False, 'data': meetups, 'endpoint': 'get_meetup_list'})


class GetMeetupDetails(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk, format=None):


        data = {'error': True}
        meetup_detail = meetup_interface.getMeetUpsDetails(pk)

        if meetup_detail['error'] == False:
            data = meetup_detail

        data['endpoint'] = 'get_meetup_details'
        return Response(data)


class GetMeetUpsToday(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):

        data = meetup_interface.getMeetUpsToday()
        if data['error'] == False:
            data['endpoint'] = 'get_meetups_today'
        else:
            data = {'error': True, 'endpoint': 'get_meetups_today'}

        return Response(data)


class MeetupDetail(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):

        meetup_id = meetup_interface.CreateMeetUP(request.data)

        data = {'endpoint': 'create_meetup', 'error': True}
        if meetup_id != None:
            data['error'] = False
            data['meeter_id'] = meetup_id

        return Response(data)

    def delete(self, request, pk, format=None):

        data = {'error': True, 'pk': pk}

        meetup_interface.DeleteMeetUp(pk)

        return Response(data)

class CreateMeeter(APIView):
    def post(self, request, format=None):

        data = meetup_interface.CreateMeeter(request.data)

        data['endpoint'] = 'create_meeter'

        return Response(data)


class ConfirmCreateMeeter(APIView):

    def get(self, request, email, format=None):

        data = {'endpoint': 'confirm_create_meeter', 'error': True, 'email': email}

        err = meetup_interface.ConfirmCreateMeeter(email)

        data['error'] = err['error']

        return Response(data)


class DeleteMeeter(APIView):

    def post(self, request, format=None):
        data = {'endpoint': 'delete_meeter', 'error': True, 'request': request.data}

        ret = meetup_interface.DeleteMeeter(request.data)

        data['error'] = ret['error']
        return Response(data)


class ConfirmDeleteMeeter(APIView):

    def get(self, request, email, format=None):
        data = {'endpoint': 'confirm_delete_meeter', 'error': True, 'request': email}

        ret = meetup_interface.ConfirmDeleteMeeter(email)

        data['error'] = ret['error']
        data['message'] = ret['message']
        return Response(data)


class SubscribeMeetup(APIView):
    def post(self, request, format=None):


        data = {'endpoint': 'subscribe_meet_up', 'error': True}
        ret = meetup_interface.SubscribeMeetUp(request.data)

        if not ret['error']:
            data['error'] = False
            data['message'] = ret['message']

        return Response(data)


class UnsubscribeMeetUp(APIView):
    def post(self, request, format=None):
        print(request.data)

        data = {'endpoint': 'unsubscribe_meet_up', 'error': True}
        ret = meetup_interface.UnsubscribeMeetUp(request.data)

        if not ret['error']:
            data['error'] = False
            data['message'] = ret['message']
        return Response(request.data)


class Checkin(APIView):
    def post(self, request, format=None):
        data = {'endpoint': 'checkin_meet_up', 'error': True, 'request': request.data}


        ret = meetup_interface.CheckinMeetUp(request.data)

        data['error'] = ret['error']

        return Response(data)



