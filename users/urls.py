from django.contrib.auth.views import LoginView
from django.urls import path
from users.views import CreateUserView, ManagerUserView, CreateTokenView

app_name = "users"

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="create"),
    path("login/", CreateTokenView.as_view(), name="login"),
    path("me/", ManagerUserView.as_view(), name="me"),
]
