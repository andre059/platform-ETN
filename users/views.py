from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.response import Response


from users.models import User
from users.permissions import IsVerifiedUser
from users.serliazers import UserSerializers


def welcome(request):
    return HttpResponse("Добро пожаловать в API приложение!")


class UserCreateAPIView(generics.CreateAPIView):
    """создание сущности"""

    """Создание пользователя"""
    queryset = User.objects.all()
    serializer_class = UserSerializers

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(serializer.validated_data['password'])
        user.save()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """отображение одной сущности"""

    queryset = User.objects.all()
    serializer_class = UserSerializers


class UserUpdateAPIView(generics.UpdateAPIView):
    """редактирование сущности"""

    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [IsVerifiedUser]


class UserDestroyAPIView(generics.DestroyAPIView):
    """удаление сущности"""

    queryset = User.objects.all()
    permission_classes = [IsVerifiedUser]

