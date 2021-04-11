from django.contrib.auth import login
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from users.models import TerraUser, UsersStates
from api.serializers import UserSerializer, StateSerializer

import requests

class LoginUserAndGetUsersStatesView(ListAPIView):
    queryset = TerraUser.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        email = request.data['email']
        user = TerraUser.objects.get(email=email)
        login(request, user=user)
        return Response(self.get_user_states(user))

    def get_user_states(self, user):
        states = UsersStates.objects.filter(user=user)
        states_params = {}
        for state in states:
            prefix = state.url_prefix
            port = state.port
            states_params = {'prefix': prefix, 'port': port}
        return states_params


