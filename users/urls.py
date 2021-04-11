from django.urls import path
from . import views as register_views


app_name = "users"

urlpatterns = [
    path("registration/", register_views.RegisterView.as_view(), name="registration"),
    path("register/", register_views.RegisterSuccessView.as_view(), name="success_reg"),
]