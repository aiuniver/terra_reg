import os

from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .forms import RegisterForm
from .models import TerraUser, UsersStates
from utils.registartion_utils import generate_prefix, send_registration_mail


class RegisterView(CreateView):
    model = TerraUser
    template_name = "users/registration.html"
    form_class = RegisterForm
    success_url = reverse_lazy("users:success_reg")

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.create_token()
        self.object.save()
        user_states = self.create_users_state()
        os.system(
            "sh nginx_create_conf.sh {prefix} {port}".format(
                prefix=user_states[0], port=user_states[1]
            )
        )
        send_registration_mail(
            user=self.object,
            prefix=user_states[0],
            port=user_states[1],
            token=self.object.user_token,
        )
        return response

    def create_users_state(self):
        last_port = None
        if self.is_stated:
            message = f"Sorry! User {self.object.email} already exists."
            return message
        last_user = UsersStates.objects.all().last()
        if last_user:
            last_port = last_user.port
        if last_port:
            port = last_port + 1
        else:
            port = 9120
        prefix = self.set_prefix()
        new_state = UsersStates()
        prepared_state = self.set_user_state(new_state, self.object, prefix, port)
        prepared_state.save()
        return prefix, port

    @property
    def is_stated(self):
        return UsersStates.objects.filter(user=self.object).exists()

    @staticmethod
    def set_prefix():
        prefix = generate_prefix(10)
        return prefix

    @staticmethod
    def set_user_state(state, user, prefix, port):
        state.user = user
        state.url_prefix = prefix
        state.port = port
        return state


class RegisterSuccessView(TemplateView):
    template_name = "users/register_success.html"
