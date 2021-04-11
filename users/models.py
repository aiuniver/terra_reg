from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import CASCADE
from utils.registartion_utils import generate_prefix
from hashlib import sha256



class TerraUser(AbstractUser):
    username = None
    first_name = models.CharField(max_length=20, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    email = models.EmailField(unique=True, verbose_name='email')
    user_token = models.CharField(max_length=30, unique=True, verbose_name='токен авторизации')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta(AbstractUser.Meta):
        pass

    def create_token(self):
        self.user_token = sha256(generate_prefix(20).encode('utf-8')).hexdigest()


class UsersStates(models.Model):
    user = models.ForeignKey(TerraUser, on_delete=CASCADE, related_name='user')
    url_prefix = models.CharField(max_length=10, unique=True, verbose_name='Префикс ссылки на Terra GUI')
    port = models.IntegerField(unique=True, verbose_name='Индивидуальный порт соединения')
