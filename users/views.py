from django.contrib.auth import authenticate
from django.db import IntegrityError
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from random import randint

from .forms import RegisterForm
from .models import TerraUser, UsersStates
from utils.registartion_utils import generate_prefix


class RegisterView(CreateView):
    model = TerraUser
    template_name = 'users/registration.html'
    form_class = RegisterForm
    success_url = reverse_lazy('users:success_reg')

    def post(self, request, *args, **kwargs):
        response = super(RegisterView, self).post(request)
        print('RESPONSE: ', response)
        login_username = request.POST['email']
        # login_password = request.POST['password1']
        created_user = TerraUser.objects.get(email=login_username)
        user_states = self.create_users_state(created_user)
        content = {'prefix': user_states[0], 'port': user_states[1]}
        return HttpResponseRedirect(self.success_url, content=content)

    def create_users_state(self, new_user):
        prefix, port = self.set_state_values()
        new_state = UsersStates()
        prepared_state = self.set_user_state(new_state, new_user, prefix, port)
        prepared_state.save()
        # try:
        #     prepared_state.save()
        # except IntegrityError as e:
        #     prefix, port = self.set_state_values()
        #     self.set_user_state(new_state, new_user, prefix, port)
        #     self.create_users_state(new_user)
        return prefix, port


    @staticmethod
    def set_state_values():
        prefix = generate_prefix(10)
        port = randint(9120, 65000)
        return prefix, port

    @staticmethod
    def set_user_state(state, user, prefix, port):
        state.user = user
        state.url_prefix = prefix
        state.port = port
        return state


class RegisterSuccessView(TemplateView):
    template_name = 'users/register_success.html'
