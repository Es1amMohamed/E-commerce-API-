from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import *
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.utils.crypto import get_random_string
from datetime import datetime, timedelta
from django.core.mail import send_mail

# Create your views here.


@api_view(["POST"])
def sign_up(request):
    data = request.data
    user = SignupSerializer(data=data)

    if user.is_valid():
        if not User.objects.filter(email=data["email"]).exists():
            user = User.objects.create(
                first_name=data["first_name"],
                last_name=data["last_name"],
                email=data["email"],
                username=data["email"],
                password=make_password(data["password"]),
            )

            return Response(
                {"message": "Your account created successfully"},
                status=status.HTTP_201_CREATED,
            )

        else:
            return Response(
                {"message": "Email already exists"}, status=status.HTTP_400_BAD_REQUEST
            )

    else:
        return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def current_user(request):
    user = UserSerializer(request.user)

    return Response(user.data)


def get_current_host(request):
    protocol = request.is_secure() and "https" or "http"
    host = request.get_host()
    return "{protocol}://{host}/".format(protocol=protocol, host=host)


@api_view(["PUT"])
def forget_password(request):
    data = request.data
    user = get_object_or_404(User, email=data["email"])
    token = get_random_string(length=40)
    expire = datetime.now() + timedelta(minutes=30)
    user.profile.reset_password_token = token
    user.profile.reset_password_expire = expire
    user.profile.save()
    host = get_current_host(request)
    link = "http://localhost:8000/accounts/reset-password/{token}/".format(token=token)
    body = "Your password reset link is {link}".format(link=link)
    send_mail(
        "Password Reset From Ecommerce",
        body,
        "ecommerce@ecommerce.com",
        [data["email"]],
    )

    return Response(
        {"message": "Password reset link sent to {email}".format(email=data["email"])}
    )


@api_view(["POST"])
def reset_password(request, token):
    data = request.data
    user = get_object_or_404(User, profile__reset_password_token=token)

    if user.profile.reset_password_expire.replace(tzinfo=None) < datetime.now():

        return Response(
            {"message": "Password reset link expired"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if data["password"] != data["confirm_password"]:
        return Response(
            {"message": "Password and confirm password does not match"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    user.password = make_password(data["password"])
    user.profile.reset_password_token = ""
    user.profile.reset_password_expire = None
    user.profile.save()
    user.save()

    return Response({"message": "Password reset successful"}, status=status.HTTP_200_OK)
