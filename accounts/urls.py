from django.urls import path
from . import views


app_name = "accounts"


urlpatterns = [
    path("signup/", views.sign_up, name="signup"),
    path("current_user/", views.current_user, name="current_user"),
    path("forget_password/", views.forget_password, name="forget_password"),
    path("reset-password/<str:token>/", views.reset_password, name="reset_password"),
]
