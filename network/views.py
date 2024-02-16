from django.shortcuts import render
from rest_framework import generics

from network.models import Supplier
from network.permissions import IsThereDebtSupplier
from network.serliazers import SupplierSerializer
from users.permissions import UserIsActive


class SupplierCreateAPIView(generics.RetrieveAPIView):
    """создание одной сущности"""

    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    permission_classes = [UserIsActive]


class SupplierListAPIView(generics.RetrieveAPIView):
    """отображение списка сущностей"""

    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    permission_classes = [UserIsActive]


class SupplierRetrieveAPIView(generics.RetrieveAPIView):
    """отображение одной сущности"""

    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    permission_classes = [UserIsActive]


class SupplierUpdateAPIView(generics.RetrieveAPIView):
    """редактирование одной сущности"""

    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    permission_classes = [IsThereDebtSupplier, UserIsActive]


class SupplierDestroyAPIView(generics.RetrieveAPIView):
    """удаление одной сущности"""

    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    permission_classes = [IsThereDebtSupplier, UserIsActive]
