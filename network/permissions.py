from rest_framework.permissions import BasePermission, IsAuthenticated


class IsThereDebtSupplier(BasePermission):
    """Проверяет, задолженность перед поставщиком"""

    def has_permission(self, request, view):
        supplier = request.data.get('supplier')  # Получаем поставщика из запроса
        if supplier.get('debt_to_supplier') > 0:  # Проверяем задолженность перед поставщиком
            return False
        return True


class SupplierPermission(BasePermission):
    """
    Разрешение для представлений CRUD поставщика.
    """

    def has_permission(self, request, view):
        if request.method in ['POST', 'GET']:
            return True
        return IsAuthenticated().has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        return IsAuthenticated().has_permission(request, view)
