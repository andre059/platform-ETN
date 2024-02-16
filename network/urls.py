from django.urls import path

from network.apps import NetworkConfig
from network.views import SupplierCreateAPIView, SupplierListAPIView, SupplierRetrieveAPIView, SupplierUpdateAPIView, \
    SupplierDestroyAPIView

app_name = NetworkConfig.name

urlpatterns = [
    path('supplier/create/', SupplierCreateAPIView.as_view(), name='supplier_create'),
    path('supplier/', SupplierListAPIView.as_view(), name='supplier_list'),
    path('supplier/<int:pk>/', SupplierRetrieveAPIView.as_view(), name='supplier_retrieve'),
    path('supplier/update/<int:pk>/', SupplierUpdateAPIView.as_view(), name='supplier_update'),
    path('supplier/delete/<int:pk>/', SupplierDestroyAPIView.as_view(), name='supplier_delete'),
]
