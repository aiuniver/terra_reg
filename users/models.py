from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import CASCADE


class TerraUser(AbstractUser):
    username = None
    first_name = models.CharField(max_length=20, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    email = models.EmailField(unique=True, verbose_name='email')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta(AbstractUser.Meta):
        pass


class UsersStates(models.Model):
    user = models.ForeignKey(TerraUser, on_delete=CASCADE, related_name='user')
    url_prefix = models.CharField(max_length=10, unique=True, verbose_name='Префикс ссылки на Terra GUI')
    port = models.IntegerField(unique=True, verbose_name='Индивидуальный порт соединения')
