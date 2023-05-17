from django.urls import path

from .views import login_view, register_view, profile_view, logout


urlpatterns = [
    path("login/", login_view, name="login-page"),
    path("register/", register_view, name="register-page"),
    path("profile/", profile_view, name="profile-page"),
    path("logout/", logout, name="logout"),
]