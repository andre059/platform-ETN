from rest_framework import generics

from network.models import Supplier, Product, NetworkElement
from network.permissions import IsThereDebtSupplier, SupplierPermission
from network.serliazers import SupplierSerializer, ProductSerializer, NetworkElementSerializer
from users.permissions import UserIsActive


class SupplierCreateAPIView(generics.CreateAPIView):
    """создание одной сущности"""

    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    permission_classes = [UserIsActive]


class SupplierListAPIView(generics.ListAPIView):
    """отображение списка сущностей"""

    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    permission_classes = [UserIsActive]


class SupplierRetrieveAPIView(generics.RetrieveAPIView):
    """отображение одной сущности"""

    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    permission_classes = [UserIsActive]


class SupplierUpdateAPIView(generics.UpdateAPIView):
    """редактирование одной сущности"""

    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    permission_classes = [IsThereDebtSupplier, UserIsActive, SupplierPermission]


class SupplierDestroyAPIView(generics.DestroyAPIView):
    """удаление одной сущности"""

    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    permission_classes = [IsThereDebtSupplier, UserIsActive, SupplierPermission]


class ProductListAPIView(generics.ListAPIView):
    """отображение списка сущностей"""

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [UserIsActive]


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    """отображение списка сущностей"""

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [UserIsActive]


class NetworkElementListAPIView(generics.ListAPIView):
    """отображение списка сущностей"""

    serializer_class = NetworkElementSerializer
    queryset = NetworkElement.objects.all()
    permission_classes = [UserIsActive]


class NetworkElementRetrieveAPIView(generics.RetrieveAPIView):
    """отображение списка сущностей"""

    serializer_class = NetworkElementSerializer
    queryset = NetworkElement.objects.all()
    permission_classes = [UserIsActive]
