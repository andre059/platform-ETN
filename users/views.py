from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from users.models import User
from users.permissions import IsVerifiedUser
from users.serliazers import UserSerializers


class UserCreateAPIView(generics.CreateAPIView):
    """создание сущности"""

    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [IsAuthenticated]


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """отображение одной сущности"""

    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [IsVerifiedUser]


class UserUpdateAPIView(generics.UpdateAPIView):
    """редактирование сущности"""

    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [IsVerifiedUser]


class UserDestroyAPIView(generics.DestroyAPIView):
    """удаление сущности"""

    queryset = User.objects.all()
    permission_classes = [IsVerifiedUser]
