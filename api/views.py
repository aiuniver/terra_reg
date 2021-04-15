from django.contrib.auth import login
from django.core.management.utils import get_random_secret_key
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from users.models import TerraUser, UsersStates
from api.serializers import UserSerializer, StateSerializer
from django.conf import settings

import requests


class LoginUserAndGetUsersStatesView(ListAPIView):
    queryset = TerraUser.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        email = request.data["email"]
        token = request.data["user_token"]
        user = TerraUser.objects.filter(email=email).first()
        if user and self.verify_token(user, token):
            login(request, user=user)
        else:
            message = f"Пользователь {email} в системе не зарегистрирован"
            return Response({"message": message})
        return Response(self.get_user_states(user))

    def get_user_states(self, user):
        state = UsersStates.objects.filter(user=user).first()
        makefile = settings.MAKEFILE_PATTERN.format(
            prefix=state.url_prefix, port=state.port
        )
        envfile = ""
        return {"makefile": makefile, "envfile": envfile}

    @staticmethod
    def verify_token(user, token):
        if token == user.user_token:
            return True
        else:
            return False
