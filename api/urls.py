from django.urls import path

from . import views as api_views


app_name = "apps_api"

urlpatterns = [
    path("login/", api_views.LoginUserAndGetUsersStatesView.as_view(), name="login"),
]
