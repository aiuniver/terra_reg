import os

from django.contrib.auth import authenticate
from django.db import IntegrityError
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from random import randint

from .forms import RegisterForm
from .models import TerraUser, UsersStates
from utils.registartion_utils import generate_prefix, send_registration_mail


class RegisterView(CreateView):
    model = TerraUser
    template_name = 'users/registration.html'
    form_class = RegisterForm
    success_url = reverse_lazy('users:success_reg')

    def post(self, request, *args, **kwargs):
        response = super(RegisterView, self).post(request)
        context = super().get_context_data(**kwargs)
        login_username = request.POST['email']
        created_user = TerraUser.objects.get(email=login_username)
        created_user.create_token()
        created_user.save()
        user_states = self.create_users_state(created_user)
        os.system("sh nginx_create_conf.sh {prefix} {port}".format(prefix=user_states[0], port=user_states[1]))
        if isinstance(user_states, str):
            context['message'] = user_states
            return render(request, "users/registration.html", context=context)
        else:
            context['prefix'] = user_states[0]
            context['port'] = user_states[1]
            send_registration_mail(
                user=created_user,
                prefix=context['prefix'],
                port=context['port'],
                token=created_user.user_token
            )
            return HttpResponseRedirect(self.success_url)

    def create_users_state(self, new_user):
        last_port = None
        is_stated = self.is_stated(new_user)
        if is_stated:
            message = f'Sorry! User {new_user.email} already exists.'
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
        prepared_state = self.set_user_state(new_state, new_user, prefix, port)
        prepared_state.save()
        return prefix, port

    @staticmethod
    def is_stated(new_user):
        stated_user = UsersStates.objects.filter(user=new_user)
        if stated_user:
            return True
        else:
            return False

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
    template_name = 'users/register_success.html'
