import random
import string

from django.conf import settings
from django.core.mail import send_mail


def generate_prefix(length):
    char_range = string.ascii_letters + string.digits
    prefix = ''.join(random.sample(char_range, length))
    return prefix


def send_registration_mail(**kwargs):
    title = 'Регистрационные данные TerraAI'
    user = kwargs['user']
    message = f'Ваши данные для регистрации:\n' \
              f'токен: {kwargs["token"]}\n' \
              f'доменный префикс: {kwargs["prefix"]}\n' \
              f'серверный порт: {kwargs["port"]}'

    return send_mail(title, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)