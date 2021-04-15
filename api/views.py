from dataclasses import dataclass
from django.contrib.auth import login
from django.core.management.utils import get_random_secret_key
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from users.models import TerraUser, UsersStates
from api.serializers import UserSerializer
from django.conf import settings


@dataclass
class LoginUserResponse:
    success: bool
    data: dict
    error: str

    def __init__(self, **kwargs):
        self.success = kwargs.get("success", True)
        self.data = kwargs.get("data", {})
        self.error = kwargs.get("error", "")


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
            return Response(
                LoginUserResponse(
                    success=False,
                    error=f"Пользователь «{email}» в системе не зарегистрирован",
                ).__dict__
            )
        return Response(
            LoginUserResponse(
                data=self.get_user_states(user),
            ).__dict__
        )

    def get_user_states(self, user):
        state = UsersStates.objects.filter(user=user).first()
        makefile = settings.MAKEFILE_PATTERN.format(
            prefix=state.url_prefix,
            port=state.port,
            tunnel_user=settings.COLAB_TUNNEL_USER,
            rsa_key_file=settings.COLAB_RSA_KEY_FILE,
            rsa_key=settings.COLAB_RSA_KEY,
        )
        envfile = settings.ENVFILE_PATTERN.format(
            secret_key=f"'{get_random_secret_key()}'",
            debug=settings.COLAB_DEBUG,
            allowed_hosts=settings.COLAB_ALLOWED_HOST,
            api_url=settings.COLAB_API_URL,
        )
        return {
            "Makefile": makefile,
            ".env": envfile,
            settings.COLAB_RSA_KEY_FILE: settings.COLAB_RSA_KEY,
        }

    @staticmethod
    def verify_token(user, token):
        if token == user.user_token:
            return True
        else:
            return False
