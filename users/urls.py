from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path("", views.Users.as_view()),
    path("log-in", views.LogIn.as_view()),
    path("activate/<str:Jwt>", views.Activate.as_view()),
    path("is-email-available", views.is_email_available.as_view()),
    path("is-username-available", views.is_username_available.as_view()),
]
