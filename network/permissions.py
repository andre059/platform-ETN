from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import BasePermission


class IsThereDebtSupplier(BasePermission):
    """Проверяет, задолженность перед поставщиком"""

    def has_permission(self, request, view):
        if not request.product.debt:  # Проверяем, задолженный ли продукт
            return False
        elif request.product.debt:
            return True
        raise PermissionDenied("Продукт не задолженный")
