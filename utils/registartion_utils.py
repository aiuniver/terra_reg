import random
import string

from django.conf import settings
from django.core.mail import send_mail


def generate_prefix(length):
    char_range = string.ascii_lowercase + string.digits
    prefix = "".join(random.sample(char_range, length))
    return prefix


def send_registration_mail(**kwargs):
    title = "Регистрационные данные TerraAI"
    user = kwargs["user"]
    message = f"""Для использования сервиса необходимо пройти по ссылке https://colab.research.google.com/github/aiuniver/terra_reg/blob/feature/colab/notebooks/TerraGUI.ipynb
В форму авторизации введите следующие данные:
- Email: {user.email}
- Token: {kwargs.get("token")}"""

    return send_mail(
        title, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False
    )
