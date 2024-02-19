from django.urls import path

from network.apps import NetworkConfig
from network.views import SupplierCreateAPIView, SupplierListAPIView, SupplierRetrieveAPIView, SupplierUpdateAPIView, \
    SupplierDestroyAPIView, ProductListAPIView, ProductRetrieveAPIView, NetworkElementListAPIView, \
    NetworkElementRetrieveAPIView

app_name = NetworkConfig.name

urlpatterns = [
    path('supplier/create/', SupplierCreateAPIView.as_view(), name='supplier_create'),
    path('supplier/', SupplierListAPIView.as_view(), name='supplier_list'),
    path('supplier/<int:pk>/', SupplierRetrieveAPIView.as_view(), name='supplier_retrieve'),
    path('supplier/update/<int:pk>/', SupplierUpdateAPIView.as_view(), name='supplier_update'),
    path('supplier/delete/<int:pk>/', SupplierDestroyAPIView.as_view(), name='supplier_delete'),

    path('product/', ProductListAPIView.as_view(), name='product_list'),
    path('product/<int:pk>/', ProductRetrieveAPIView.as_view(), name='product_retrieve'),

    path('networkelement/', NetworkElementListAPIView.as_view(), name='networkelement_list'),
    path('networkelement/<int:pk>/', NetworkElementRetrieveAPIView.as_view(), name='networkelement_retrieve'),
]
