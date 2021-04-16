from rest_framework.serializers import ModelSerializer
from users.models import TerraUser, UsersStates


class UserSerializer(ModelSerializer):

    class Meta:
        model = TerraUser
        fields = ('email', 'user_token')


class StateSerializer(ModelSerializer):
    class Meta:
        model = UsersStates
        fields = ('url_prefix', 'port')
