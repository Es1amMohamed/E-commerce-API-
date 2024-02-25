from django.urls import path
from . import views


app_name = "accounts"


urlpatterns = [
    path("signup/", views.sign_up, name="signup"),
    path("current_user/", views.current_user, name="current_user"),
]
